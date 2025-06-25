# 📰 Text Analysis & Sentiment Dashboard

A Python-based project that scrapes article content from URLs, performs text cleaning, sentiment scoring, and readability analysis — all visualized in a Streamlit dashboard.

## 🔍 Overview

This project includes:
- ✅ Automated article scraping using `requests` + `BeautifulSoup`
- ✅ Text preprocessing with stopword removal
- ✅ Sentiment scoring using positive/negative word dictionaries
- ✅ Readability metrics: Fog Index, Avg Word Length, Complex Words %
- ✅ Export to Excel
- ✅ Interactive dashboard built in Streamlit

## 📊 Dashboard Preview
![text_analysis1](https://github.com/user-attachments/assets/5a706390-879e-4623-a63f-abd43e264ecf)
![text_analysis2](https://github.com/user-attachments/assets/eff163d7-7890-4b10-94aa-bb71873a50b1)
![text_analysis3](https://github.com/user-attachments/assets/7e3e922a-8e1a-4c0b-86ad-7c794e5beefc)


### 🌐 Try it Live
https://text-analysis-dashboard-n2ggygfsadib83tmmsdgho.streamlit.app/

---

## 📁 Files in This Repo

| File | Description |
|------|-------------|
| `streamlit_app.py` | Streamlit dashboard code |
| `analysis_output.xlsx` | Processed text metrics (example data) |
| `requirements.txt` | Python dependencies for the app |

---

## 📦 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/text-analysis-dashboard.git
cd text-analysis-dashboard
