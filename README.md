<div align="center">

# ⚖️ Screendit — News Spin & Fact Alignment AI

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Outfit&weight=700&size=32&duration=3500&pause=1000&color=8E44AD&center=true&vCenter=true&width=900&height=50&lines=Exposing+Media+Bias+with+AI+⚖️;Fact+Alignment+→+Contrast+Analysis;BGE-M3+Neural+Network+%7C+NLP+Engine)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-SpaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

<br/>

[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Screendit_AI-8e44ad?style=for-the-badge&labelColor=0c1445)](https://screendit-project.streamlit.app/)
[![GitHub Stars](https://img.shields.io/github/stars/mayank-goyal09/Screendit?style=for-the-badge&color=ffd700)](https://github.com/mayank-goyal09/Screendit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mayank-goyal09/Screendit?style=for-the-badge&color=87ceeb)](https://github.com/mayank-goyal09/Screendit/network)

<br/>

![Screendit Banner](C:\Users\mayank goyal\.gemini\antigravity\brain\5433b3d2-0ba1-490a-b168-1cc0460111bf\screendit_banner_1776792652585.png)

<br/>

### 🧠 **Using BGE-M3 Embeddings to align facts and expose bias** 

### **From URL Scraping → Real-Time Contrast Analysis** 🌍

</div>

---

## ⚡ **THE ANALYSIS AT A GLANCE**

<table>
<tr>
<td width="50%">

### 🎯 **What This Project Does**

Screendit is an **AI-powered journalist helper** designed to compare two news articles covering the same event. It uses **BGE-M3 (State-of-the-art semantic embeddings)** and **SpaCy** to align matching factual statements and highlight contrasting "spin" words.

**The Complete Pipeline:**
- 📡 **Web Scraping** → Real-time article extraction via BeautifulSoup
- 🔄 **Semantic Alignment** → Multi-stage cosine similarity matching
- 🧠 **Bias Detection** → Extracting contrasting adjectives and entities
- 📊 **Visualization** → Interactive Plotly gauges and glassmorphism UI
- 🚀 **Deployment** → Optimized for high-speed inference

</td>
<td width="50%">

### ✨ **Key Highlights**

| Feature | Details |
|---------|---------|
| ⚖️ **Alignment Sensitivity** | User-adjustable similarity threshold |
| 🚩 **Spin Highlighting** | Real-time extraction of biased framing |
| 📊 **Dashboard** | High-level factual match statistics |
| 🧠 **Model Type** | BGE-M3 (Semantic) + SpaCy (Syntactic) |
| 📉 **Accuracy** | High-precision sentence alignment |
| 🎨 **UI Design** | Premium "Warm White" & Glassmorphism |
| 📱 **Responsive** | Fully optimized for mobile/desktop |
| ⚡ **Latency** | Cached models for lightning-fast results |

</td>
</tr>
</table>

---

## 🛠️ **TECHNOLOGY STACK**

<div align="center">

![Tech Stack](https://skillicons.dev/icons?i=python,tensorflow,github,vscode)

</div>

| **Category** | **Technologies** | **Purpose** |
|:------------:|:-----------------|:------------|
| 🐍 **Core Language** | Python 3.8+ | Primary development language |
| 🧠 **NLP Engine** | SpaCy (en_core_web_sm) | Sentence tokenization & POS tagging |
| 🌍 **Embeddings** | Sentence-Transformers (BGE-M3) | High-fidelity semantic vectorization |
| 🎨 **Frontend** | Streamlit | Interactive web application |
| 📈 **Visualization** | Plotly | Dynamic gauge charts & stat cards |
| 🌐 **Scraping** | BeautifulSoup4 / Requests | News article extraction |
| 🚀 **Deployment** | Streamlit Cloud | Production hosting |

---

## 🔬 **HOW SCREENDIT WORKS**

```mermaid
graph LR
    A[🌐 Article URLs] --> B[📥 BeautifulSoup Scraping]
    B --> C[✂️ SpaCy Tokenization]
    C --> D[🔢 BGE-M3 Vectorization]
    D --> E[📐 Cosine Similarity Match]
    E --> F[🚩 Spin Extraction]
    F --> G[📱 Screendit Dashboard]
    
    style A fill:#8e44ad,color:#fff
    style D fill:#f093fb,color:#fff
    style G fill:#4facfe,color:#fff
```

### **The Pipeline Breakdown:**

<table>
<tr>
<td>

#### 📡 **1. Intelligent Extraction**
Automated article fetching that ignores ads and navigation, focusing purely on narrative content.

</td>
<td>

#### 🔄 **2. Semantic Alignment**
Every sentence in Source A is compared against Source B to find its most accurate factual counterpart.

</td>
</tr>
<tr>
<td>

#### 🧠 **3. Spin Recognition**
The engine identifies unique framing words (adjectives/verbs) that Source A uses but Source B does not, and vice-versa.

</td>
<td>

#### 📊 **4. Investigative UI**
Interactive results display each factual match side-by-side with localized "Alignment Scores."

</td>
</tr>
</table>

---

## 📂 **PROJECT STRUCTURE**

```
⚖️ Screendit/
│
├── 📊 app.py               # Main Streamlit application & UI
├── ⚙️ engine.py            # Cached AI model loading & NLP logic
├── 🧠 main.ipynb           # Experimental development & EDA
│
├── 📦 requirements.txt     # Project dependencies
└── 📖 README.md            # You are here! 🎉
```

---

## 🚀 **QUICK START GUIDE**

<div align="center">

![Quick Start](https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif)

</div>

### **Step 1: Clone the Repository** 📥

```bash
git clone https://github.com/mayank-goyal09/Screendit.git
cd Screendit
```

### **Step 2: Create Virtual Environment** 🐍

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies** 📦

```bash
pip install -r requirements.txt
```

### **Step 4: Launch Screendit** ⚖️

```bash
streamlit run app.py
```

---

## 📚 **SKILLS DEMONSTRATED**

| **Category** | **Skills** |
|:-------------|:-----------|
| 🧠 **Deep Learning** | Semantic embedding models (BGE-M3), Vector similarity |
| 📊 **NLP** | POS tagging, named entity recognition, sentence segmentation |
| 🔧 **Data Engineering** | Web scraping, data cleaning, caching pipelines |
| 🎨 **UI/UX Design** | Custom CSS, glassmorphism, interactive charts |
| 📈 **Data Visualization** | Specialized Plotly indicators, high-density stat cards |
| 🚀 **MLOps** | Resource optimization, model caching, cloud deployment |

---

## 🔮 **FUTURE ENHANCEMENTS**

- [ ] 🤖 **LLM Summarization**: Automated bias summaries for each article.
- [ ] 📈 **Sentiment Analysis**: Dynamic sentiment trends across the article timeline.
- [ ] 🕵️‍♂️ **Author Profile**: Tracking "Spin History" for specific journalists.
- [ ] 🌐 **Multi-Language Support**: Comparing news across different languages.

---

## 👨‍💻 **CONNECT WITH ME**

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?style=for-the-badge&logo=github)](https://github.com/mayank-goyal09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mayank_Goyal-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mayank-goyal-4b8756363/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Site-8e44ad?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mayank-portfolio-delta.vercel.app/)

**Mayank Goyal**  
📊 Data Analyst | 🧠 NLP Enthusiast | ⚖️ Media Analysis Specialist

</div>

---

<div align="center">

### ⚖️ **Built with AI & ❤️ by Mayank Goyal**

*"Exposing the spin, uncovering the truth."* ⚖️🧠

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:8e44ad,100:4facfe&height=120&section=footer)

</div>
