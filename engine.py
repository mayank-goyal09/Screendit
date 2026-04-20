import streamlit as st
from sentence_transformers import SentenceTransformer
import spacy

# ✅ This is the 'Secret Sauce' for Speed!
@st.cache_resource
def load_models():
    # Load the heavy BGE-M3 model once
    model = SentenceTransformer('BAAI/bge-m3')
    # Load SpaCy
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        import os
        os.system("python -m spacy download en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return model, nlp

# (Copy-paste your fetch_article_text, get_clean_prose, 
# and align_sentences functions here)