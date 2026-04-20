import streamlit as st
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
import numpy as np
import plotly.graph_objects as go
import time

# --- 🎨 1. STREAMLIT UI LAYOUT & CUSTOM CSS ---
st.set_page_config(layout="wide", page_title="Screendit | News Spin Comparator", page_icon="⚖️")

# Custom CSS for Warm White Background, Purple Cards & Buttons
st.markdown("""
<style>
    /* Main Background and Top Header */
    .stApp, header[data-testid="stHeader"] {
        background-color: #fdfbf7 !important; /* Warm white */
        color: #333333;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #fbf5fa !important; /* Very light purple/warm white */
        border-right: 1px solid #e1d5e6 !important;
    }

    /* Force dark text for sidebar labels and content, but avoid aggressive wildcard */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] div {
        color: #333333 !important;
    }

    /* Fix Input Box Visibility (so links are visible when pasted) */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #e1d5e6 !important;
        caret-color: #333333 !important;
    }
    .stTextInput input:focus {
        border-color: #8e44ad !important;
        box-shadow: 0 0 5px rgba(142, 68, 173, 0.4) !important;
    }
    
    /* Ensure other widgets are readable */
    .stSlider div[data-testid="stThumbValue"] {
        color: #8e44ad !important;
    }

    /* Highlight tags for Spin Words */
    mark.spin-a {
        background-color: #ffe0e0; /* Soft red for Source A */
        color: #c0392b;
        padding: 0 4px;
        border-radius: 4px;
        font-weight: 500;
    }
    mark.spin-b {
        background-color: #e0ffe0; /* Soft green for Source B */
        color: #27ae60;
        padding: 0 4px;
        border-radius: 4px;
        font-weight: 500;
    }

    /* Summary Dashboard */
    .summary-container {
        display: flex;
        justify-content: space-around;
        background: linear-gradient(135deg, #4a235a, #8e44ad);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(105, 56, 137, 0.2);
    }
    .summary-stat {
        text-align: center;
    }
    .summary-val {
        font-size: 2.2em;
        font-weight: 800;
        display: block;
    }
    .summary-label {
        font-size: 0.9em;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Floating Effect for Match Cards */
    .result-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(105, 56, 137, 0.08);
        border-left: 6px solid #8e44ad;
        margin-bottom: 25px;
        transition: all 0.3s ease;
        border: 1px solid #f0e6f2;
    }
    .result-card:hover {
        transform: scale(1.01);
        box-shadow: 0 10px 30px rgba(105, 56, 137, 0.12);
        border-left: 6px solid #4a235a;
    }
    
    .source-badge-a { color: #c0392b; font-weight: 700; font-size: 0.9em; letter-spacing: 1px; }
    .source-badge-b { color: #27ae60; font-weight: 700; font-size: 0.9em; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

# --- 🧠 2. CACHED ENGINE (Latency Optimization) ---
@st.cache_resource(show_spinner="Initializing AI Engine...")
def load_resources():
    model = SentenceTransformer('BAAI/bge-m3')
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        import os
        os.system("python -m spacy download en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return model, nlp

model, nlp = load_resources()

# --- ⚙️ 3. CORE LOGIC FUNCTIONS ---
@st.cache_data(show_spinner=False, ttl=3600)
def fetch_article(url):
    """Fetches and parses an article into sentences with caching for latency optimization."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        paras = soup.find_all('p')
        text = " ".join([p.get_text().strip() for p in paras])
        # Use SpaCy for proper sentence tokenization
        doc = nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 40]
        return sentences
    except Exception as e:
        return None

def highlight_text(text, words, css_class):
    """Highlights specific words in text using HTML tags."""
    import re
    if not words:
        return text
    # Sort words by length descending to avoid partial matches on longer words
    sorted_words = sorted(words, key=len, reverse=True)
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_words)) + r')\b', re.IGNORECASE)
    return pattern.sub(f'<mark class="{css_class}">\\1</mark>', text)

def get_spin_words(sent1, sent2):
    # Extract unique adjectives and entities that create "Spin"
    doc1 = nlp(sent1)
    doc2 = nlp(sent2)
    
    # Filter for adjectives, proper nouns, and verbs that carry framing/spin
    words1 = {t.text.lower() for t in doc1 if (t.pos_ in ["ADJ", "PROPN", "ADV", "VERB"]) and not t.is_stop and t.is_alpha}
    words2 = {t.text.lower() for t in doc2 if (t.pos_ in ["ADJ", "PROPN", "ADV", "VERB"]) and not t.is_stop and t.is_alpha}
    
    spin_a = list(words1 - words2)
    spin_b = list(words2 - words1)
    
    # Generate highlighted HTML
    html_a = highlight_text(sent1, spin_a, "spin-a")
    html_b = highlight_text(sent2, spin_b, "spin-b")
    
    return spin_a, spin_b, html_a, html_b

def create_semi_donut(score, title="Match Prediction"):
    """Creates a semi-donut gauge chart using Plotly."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score * 100,
        number = {'suffix': "%", 'font': {'color': '#4a235a', 'size': 35}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title, 'font': {'size': 18, 'color': '#4a235a'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#4a235a"},
            'bar': {'color': "#8e44ad"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e1d5e6",
            'steps': [
                {'range': [0, 50], 'color': '#fdedec'},
                {'range': [50, 80], 'color': '#f5eef8'},
                {'range': [80, 100], 'color': '#ebdef0'}],
        }
    ))
    fig.update_layout(
        font={'color': "#4a235a", 'family': "Arial"},
        margin=dict(l=20, r=20, t=50, b=20),
        height=220,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- 🚀 4. MAIN APP LOGIC ---

st.title("⚖️ Screendit")
st.markdown("### Match predictions, factual alignments, and contrast analysis. Powered by AI.")

# Sidebar Inputs
st.sidebar.header("Step 1: Input Sources")
url_a = st.sidebar.text_input("Article URL A", placeholder="e.g. https://www.bbc.com/news/...", help="Paste the full URL of the first article")
url_b = st.sidebar.text_input("Article URL B", placeholder="e.g. https://www.cnn.com/...", help="Paste the full URL of the second article")
similarity_threshold = st.sidebar.slider("Alignment Sensitivity", 0.4, 1.0, 0.70, help="Lower values show more distant matches, higher values require stricter alignment.")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Director's Tip:** We use caching to ensure fast repeated queries. Words highlighted as 'spin' map to the contrasting sentiment or framing used by each author.")

if st.sidebar.button("🚀 Analyze Contrast & Spin"):
    if url_a and url_b:
        progress_bar = st.progress(0, text="Fetching articles...")
        start_time = time.time()
        
        sents_a = fetch_article(url_a)
        progress_bar.progress(25, text="Fetching secondary article...")
        sents_b = fetch_article(url_b)
        
        if sents_a and sents_b:
            progress_bar.progress(50, text="Calculating semantic embeddings...")
            
            # Sub-function for embedding generation
            @st.cache_data(show_spinner=False)
            def get_embeddings(sentences):
                return model.encode(sentences)

            emb_a = get_embeddings(sents_a)
            emb_b = get_embeddings(sents_b)
            
            progress_bar.progress(75, text="Computing similarity matrices...")
            sim_matrix = cosine_similarity(emb_a, emb_b)
            
            progress_bar.progress(100, text="Analysis complete!")
            time.sleep(0.5)
            progress_bar.empty()

            st.success(f"Analysis completed in {time.time() - start_time:.2f} seconds.")
            st.divider()
            
            st.subheader("📊 Fact Alignment & Contrast Analysis")
            
            # 1. First, compute all matches to calculate global stats
            matches = []
            total_spin_count = 0
            
            for i, row in enumerate(sim_matrix):
                best_match_idx = np.argmax(row)
                score = row[best_match_idx]
                if score >= similarity_threshold:
                    spin_a, spin_b, html_a, html_b = get_spin_words(sents_a[i], sents_b[best_match_idx])
                    matches.append({
                        'score': score,
                        'html_a': html_a,
                        'html_b': html_b,
                        'spin_a': spin_a,
                        'spin_b': spin_b
                    })
                    total_spin_count += len(spin_a) + len(spin_b)

            if matches:
                # 2. Display Summary Dashboard
                avg_similarity = np.mean([m['score'] for m in matches])
                st.markdown(f"""
                <div class="summary-container">
                    <div class="summary-stat">
                        <span class="summary-val">{len(matches)}</span>
                        <span class="summary-label">Factual Alignments</span>
                    </div>
                    <div class="summary-stat">
                        <span class="summary-val">{int(avg_similarity * 100)}%</span>
                        <span class="summary-label">Avg. Similarity</span>
                    </div>
                    <div class="summary-stat">
                        <span class="summary-val">{total_spin_count}</span>
                        <span class="summary-label">Spin Points Found</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # 3. Display Matches
                for i, match in enumerate(matches):
                    # Display the semi-donut chart for the match score
                    col_chart, col_content = st.columns([1, 4])
                    
                    with col_chart:
                        st.plotly_chart(create_semi_donut(match['score'], title="Alignment"), use_container_width=True, config={'displayModeBar': False}, key=f"chart_{i}")
                        
                    with col_content:
                        st.markdown(f'<div class="result-card">', unsafe_allow_html=True)
                        cc1, cc2 = st.columns(2)
                        
                        with cc1:
                            st.markdown('<span class="source-badge-a">🚩 SOURCE A</span>', unsafe_allow_html=True)
                            st.markdown(f'<p style="font-size: 1.05em; line-height: 1.6;">{match["html_a"]}</p>', unsafe_allow_html=True)
                                
                        with cc2:
                            st.markdown('<span class="source-badge-b">🚩 SOURCE B</span>', unsafe_allow_html=True)
                            st.markdown(f'<p style="font-size: 1.05em; line-height: 1.6;">{match["html_b"]}</p>', unsafe_allow_html=True)
                                
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("No matching factual sentences found at this sensitivity level. Try lowering the 'Alignment Sensitivity' in the sidebar.")
            
        else:
            progress_bar.empty()
            st.error("Could not fetch one or both articles. Please check the URLs or ensure the sites allow automated scraping.")
    else:
        st.warning("Please enter both URLs to begin the analysis.")