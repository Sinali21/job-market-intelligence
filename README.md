# 💼 AI-Powered Job Market Intelligence Platform
### Sri Lanka IT Job Market Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Overview

Sri Lankan students often graduate without knowing **what skills employers actually demand right now**. This platform solves that problem by analyzing thousands of real job postings using **NLP and Machine Learning** to extract actionable insights about the IT job market.

> **"What should I learn next?"** — This platform answers that question with real data.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🔥 **Most Demanded Skills** | Top skills employers are looking for right now |
| 💰 **Salary Trends** | Average salaries by job cluster and role |
| 📊 **Job Clustering** | K-Means groups similar jobs automatically |
| 📚 **Topic Modeling** | LDA discovers hidden themes in job descriptions |
| 🎯 **Skill Gap Analyzer** | Enter your skills → get personalized gap analysis |
| 🚀 **Career Recommendations** | AI-powered career path suggestions |
| 🔎 **Job Data Explorer** | Search and filter 4,300+ real job postings |

---

## 🖥️ Dashboard Preview

### Main Dashboard
- **4 metric cards** — Total jobs, titles, companies, countries
- **Top 15 skills chart** — Most demanded skills with percentages
- **Salary by cluster** — Which job type pays the most
- **Job distribution** — Pie chart of job categories
- **Topic distribution** — Hidden themes in job market

### Skill Gap Analyzer
Enter your skills and instantly see:
- ✅ Skills you already have that employers want
- ⚠️ Skills you are missing
- 🎯 Best career path based on your profile
- 💰 Expected salary in your best-fit cluster

---

## 🛠️ Tech Stack

### Languages & Frameworks
- **Python 3.9+** — Core language
- **Streamlit** — Web dashboard framework

### Data & NLP
- **Pandas & NumPy** — Data manipulation
- **NLTK** — Text preprocessing, tokenization, lemmatization
- **Scikit-learn** — TF-IDF vectorization

### Machine Learning Models
- **TF-IDF** — Term frequency analysis for skill importance
- **K-Means Clustering** — Groups similar jobs into categories
- **LDA (Latent Dirichlet Allocation)** — Topic modeling

### Visualization
- **Matplotlib** — Charts and graphs
- **Seaborn** — Statistical visualizations

---

## 📁 Project Structure

```
job_market_intelligence_platform/
│
├── app.py                          ← Streamlit dashboard
│
├── notebooks/
│   ├── 01_data_collection.ipynb   ← Load & explore dataset
│   ├── 02_preprocessing.ipynb     ← Text cleaning & NLP
│   ├── 03_skill_extraction.ipynb  ← Skill extraction & analysis
│   ├── 04_model_training.ipynb    ← TF-IDF, K-Means, LDA
│   └── 05_insights.ipynb          ← Salary, gaps, recommendations
│
├── data/
│   ├── raw/
│   │   └── jobs_raw.csv           ← Selected columns from dataset
│   └── processed/
│       ├── jobs_cleaned.csv       ← Cleaned & preprocessed data
│       ├── jobs_with_skills.csv   ← Data with extracted skills
│       └── model_results.csv      ← Final data with ML results
│
├── outputs/
│   ├── top_skills.png             ← Top skills chart
│   ├── skill_categories.png       ← Skill categories pie chart
│   ├── clusters.png               ← Job clusters chart
│   ├── topics.png                 ← LDA topics chart
│   ├── salary_by_cluster.png      ← Salary analysis chart
│   └── skill_gap.png              ← Skill gap analysis chart
│
└── requirements.txt               ← All dependencies
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sinali21/job-market-intelligence.git
cd job-market-intelligence
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the Dataset
- Download from [Kaggle — Job Description Dataset](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
- Place `job_descriptions.csv` in `data/raw/`

### 4. Run the Notebooks in Order
```
01_data_collection.ipynb
02_preprocessing.ipynb
03_skill_extraction.ipynb
04_model_training.ipynb
05_insights.ipynb
```

### 5. Launch the Dashboard
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🔬 NLP & ML Pipeline

```
Raw Job Data (1.6M rows)
        ↓
Data Selection & Sampling (10,000 IT jobs)
        ↓
Text Preprocessing
  → Remove special characters
  → Lowercase normalization
  → Stopword removal
  → Lemmatization
        ↓
Skill Extraction
  → Pattern matching against skills dictionary
  → 105 unique skills across 11 categories
        ↓
TF-IDF Vectorization
  → 100 most important terms
        ↓
K-Means Clustering (K=6)
  → Design & UI/UX
  → Software Development
  → Data & Analytics
  → Network & Security
  → Database & Systems
  → Marketing & Architecture
        ↓
LDA Topic Modeling (6 topics)
  → Engineering & Systems
  → Data & Business Analytics
  → Application Development
  → UI/UX Design
  → Network & Security
  → Testing & Performance
        ↓
Insights & Recommendations
```

---

## 📊 Key Findings

### Top 5 Most Demanded Skills
| Rank | Skill | % of Jobs |
|---|---|---|
| 1 | Problem Solving | 17.5% |
| 2 | Security | 17.4% |
| 3 | Communication | 16.4% |
| 4 | Infrastructure | 13.2% |
| 5 | Data Analysis | 11.8% |

### Salary Insights
| Cluster | Average Salary |
|---|---|
| Data & Analytics | $82,959 |
| Network & Security | $82,665 |
| Software Development | $82,129 |
| Database & Systems | $82,058 |

### Skill Categories Distribution
| Category | Demand |
|---|---|
| Soft Skills | 58.0% |
| Design | 57.4% |
| Security | 43.8% |
| Data Science & ML | 40.9% |
| Cloud & DevOps | 38.3% |

---

## 🚀 How to Use the Skill Gap Analyzer

1. Open the dashboard at `http://localhost:8501`
2. Scroll down to **Skill Gap Analyzer**
3. Type your skills separated by commas:
   ```
   python, sql, javascript, communication
   ```
4. Instantly see:
   - Which of your skills are in demand
   - What skills you are missing
   - Your best career path match
   - Expected salary range

---

## 🔮 Future Improvements

- [ ] Scrape real-time data from TopJobs.lk and XpressJobs.lk
- [ ] Add BERT model for more accurate skill extraction
- [ ] Add time-series analysis for emerging skills
- [ ] Deploy on Streamlit Cloud for public access
- [ ] Add more Sri Lanka specific job portals
- [ ] Implement user accounts to save skill profiles
- [ ] Add course recommendations for skill gaps

---

## 📚 What I Learned

- Web scraping and data collection techniques
- NLP text preprocessing pipeline
- Unsupervised ML — K-Means clustering
- Topic modeling with LDA
- TF-IDF for feature extraction
- Data visualization with Matplotlib & Seaborn
- Building interactive dashboards with Streamlit
- End-to-end data science project workflow

---

## 👩‍💻 Author

**Sinali**
- GitHub: [@Sinali21](https://github.com/Sinali21)
- LinkedIn: [www.linkedin.com/in/sinali21] (https://linkedin.com)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Dataset: [Kaggle — Job Description Dataset](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
- Built with: Python, Streamlit, NLTK, Scikit-learn

---

⭐ **If you found this project helpful, please give it a star!** ⭐
