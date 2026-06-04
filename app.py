# ─────────────────────────────────────────────
# AI-Powered Job Market Intelligence Platform
# Sri Lanka — Streamlit Dashboard
# ─────────────────────────────────────────────

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

# ── PAGE SETTINGS ────────────────────────────
st.set_page_config(
    page_title = "Job Market Intelligence — Sri Lanka",
    page_icon  = "💼",
    layout     = "wide"
)

# ── PATHS ────────────────────────────────────
BASE_PATH       = 'D:/Sinali/projects/job_market_intelligence_platform'
PROCESSED_PATH  = f'{BASE_PATH}/data/processed'
OUTPUT_PATH     = f'{BASE_PATH}/outputs'

# ── LOAD DATA ────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(f'{PROCESSED_PATH}/model_results.csv')
    df['all_skills_str'] = df['all_skills_str'].fillna('')
    df['salary']         = df['salary'].fillna('Not Specified')
    return df

df = load_data()

# ── HEADER ───────────────────────────────────
st.title("💼 AI-Powered Job Market Intelligence")
st.subheader("Sri Lanka IT Job Market Analysis Dashboard")
st.markdown("---")

# ── TOP METRICS ──────────────────────────────
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs Analyzed",  f"{len(df):,}")
col2.metric("Unique Job Titles",    f"{df['title'].nunique():,}")
col3.metric("Unique Companies",     f"{df['company'].nunique():,}")
col4.metric("Countries Covered",    f"{df['country'].nunique():,}")

st.markdown("---")

# ── SIDEBAR ──────────────────────────────────
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("Use filters to explore the data")

# Cluster filter
all_clusters    = ['All'] + sorted(df['cluster_name'].dropna().unique().tolist())
selected_cluster = st.sidebar.selectbox("Select Job Cluster", all_clusters)

# Filter data based on selection
if selected_cluster == 'All':
    filtered_df = df
else:
    filtered_df = df[df['cluster_name'] == selected_cluster]

st.sidebar.markdown(f"**Showing {len(filtered_df):,} jobs**")

# ── TOP SKILLS SECTION ───────────────────────
st.header("🔥 Most Demanded Skills")

# Count skills
all_skills_flat = []
for skills_str in filtered_df['all_skills_str']:
    skills = [s.strip() for s in str(skills_str).split(',') if s.strip()]
    all_skills_flat.extend(skills)

skill_counts = Counter(all_skills_flat)
skills_df    = pd.DataFrame(
    skill_counts.most_common(15),
    columns=['skill', 'count']
)
skills_df['percentage'] = (skills_df['count'] / len(filtered_df) * 100).round(1)

# Chart
fig, ax = plt.subplots(figsize=(10, 6))
colors  = plt.cm.viridis_r(np.linspace(0.2, 0.8, len(skills_df)))

bars = ax.barh(
    skills_df['skill'][::-1],
    skills_df['percentage'][::-1],
    color=colors
)

for bar, val in zip(bars, skills_df['percentage'][::-1]):
    ax.text(
        bar.get_width() + 0.2,
        bar.get_y() + bar.get_height()/2,
        f'{val}%',
        va='center',
        fontsize=9
    )

ax.set_xlabel('% of Job Postings')
ax.set_title('Top 15 Most Demanded Skills')
plt.tight_layout()

st.pyplot(fig)
st.markdown("---")

# ── SALARY & CLUSTER SECTION ─────────────────
st.header("💰 Salary & Job Clusters")

col1, col2 = st.columns(2)

# ── LEFT: Salary by Cluster ───────────────────
with col1:
    st.subheader("Average Salary by Cluster")

    def extract_salary(salary_str):
        import re
        if pd.isna(salary_str) or salary_str == 'Not Specified':
            return np.nan
        numbers = re.findall(r'\d+', str(salary_str))
        if len(numbers) >= 2:
            return (int(numbers[0]) * 1000 + int(numbers[1]) * 1000) / 2
        return np.nan

    df['salary_avg']          = df['salary'].apply(extract_salary)
    salary_by_cluster         = df.groupby('cluster_name')['salary_avg'].mean().sort_values(ascending=False)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    colors2   = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(salary_by_cluster)))

    bars2 = ax2.barh(
        salary_by_cluster.index[::-1],
        salary_by_cluster.values[::-1],
        color=colors2
    )

    for bar, val in zip(bars2, salary_by_cluster.values[::-1]):
        ax2.text(
            bar.get_width() + 0.3,
            bar.get_y() + bar.get_height()/2,
            f'${val:,.0f}',
            va='center',
            fontsize=8
        )

    ax2.set_xlabel('Average Salary (USD)')
    plt.tight_layout()
    st.pyplot(fig2)

# ── RIGHT: Jobs per Cluster ───────────────────
with col2:
    st.subheader("Jobs per Cluster")

    cluster_counts = filtered_df['cluster_name'].value_counts()

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    colors3   = plt.cm.Set2(np.linspace(0, 1, len(cluster_counts)))

    ax3.pie(
        cluster_counts.values,
        labels=cluster_counts.index,
        autopct='%1.1f%%',
        colors=colors3,
        startangle=90
    )
    ax3.set_title('Job Distribution by Cluster')
    plt.tight_layout()
    st.pyplot(fig3)

st.markdown("---")

# ── TOPIC SECTION ────────────────────────────
st.header("📚 Job Market Topics")

topic_counts = filtered_df['dominant_topic_name'].value_counts()

fig4, ax4 = plt.subplots(figsize=(10, 4))
colors4   = plt.cm.Paired(np.linspace(0, 1, len(topic_counts)))

bars4 = ax4.bar(
    topic_counts.index,
    topic_counts.values,
    color=colors4,
    edgecolor='white',
    linewidth=1.5
)

for bar, val in zip(bars4, topic_counts.values):
    ax4.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 5,
        str(val),
        ha='center',
        fontsize=9,
        fontweight='bold'
    )

ax4.set_title('Topic Distribution Across IT Jobs')
ax4.set_ylabel('Number of Jobs')
plt.xticks(rotation=15, ha='right')
plt.tight_layout()

st.pyplot(fig4)
st.markdown("---")

# ── SKILL GAP ANALYZER ───────────────────────
st.header("🎯 Skill Gap Analyzer")
st.markdown("**Enter your skills and find out what you are missing!**")

# Text input for user skills
user_input = st.text_input(
    "Enter your skills (comma separated)",
    placeholder="e.g. python, sql, javascript, communication"
)

if user_input:
    # Process user skills
    user_skills = [s.strip().lower() for s in user_input.split(',')]

    # Get top demanded skills
    all_skills_flat2 = []
    for skills_str in df['all_skills_str']:
        skills = [s.strip() for s in str(skills_str).split(',') if s.strip()]
        all_skills_flat2.extend(skills)

    skill_counts2   = Counter(all_skills_flat2)
    top_20_demanded = dict(skill_counts2.most_common(20))

    # Find gaps
    gaps    = {}
    matched = {}

    for skill, count in top_20_demanded.items():
        pct = round(count / len(df) * 100, 1)
        if skill.lower() in user_skills:
            matched[skill] = pct
        else:
            gaps[skill] = pct

    # ── SHOW RESULTS ─────────────────────────
    col1, col2, col3 = st.columns(3)

    col1.metric("Skills You Have",    f"{len(matched)} / 20")
    col2.metric("Skill Gaps Found",   f"{len(gaps)} / 20")
    col3.metric("Coverage",           f"{round(len(matched)/20*100)}%")

    st.markdown("---")

    col_left, col_right = st.columns(2)

    # ── LEFT: Skills you have ─────────────────
    with col_left:
        st.subheader("✅ Skills You Have")
        if matched:
            for skill, pct in matched.items():
                st.success(f"**{skill}** — demanded in {pct}% of jobs")
        else:
            st.warning("None of your skills matched top 20 demanded skills")

    # ── RIGHT: Skill gaps ─────────────────────
    with col_right:
        st.subheader("⚠️ Skills to Learn")
        if gaps:
            for skill, pct in list(gaps.items())[:10]:
                st.error(f"**{skill}** — demanded in {pct}% of jobs")

    st.markdown("---")

    # ── CAREER RECOMMENDATION ─────────────────
    st.subheader("🚀 Career Recommendation")

    # Match user to best cluster
    cluster_match = {}
    for cluster in df['cluster_name'].dropna().unique():
        cluster_jobs   = df[df['cluster_name'] == cluster]
        cluster_skills = []
        for skills_str in cluster_jobs['all_skills_str']:
            skills = [s.strip().lower() for s in str(skills_str).split(',') if s.strip()]
            cluster_skills.extend(skills)

        cluster_skill_set = set(cluster_skills)
        match_count       = len(set(user_skills) & cluster_skill_set)
        cluster_match[cluster] = match_count

    best_match = max(cluster_match, key=cluster_match.get)

    st.success(f"🎯 Based on your skills, you are best suited for: **{best_match}**")

    # Show avg salary for best match
    best_salary = df[df['cluster_name'] == best_match]['salary_avg'].mean()
    st.info(f"💰 Average salary in {best_match}: **${best_salary:,.0f}**")

st.markdown("---")

# ── DATA EXPLORER ────────────────────────────
st.header("🔎 Explore Job Data")

# Search box
search = st.text_input(
    "Search by job title or company",
    placeholder="e.g. Software Engineer or Google"
)

# Apply search filter
if search:
    explore_df = filtered_df[
        filtered_df['title'].str.contains(search, case=False, na=False) |
        filtered_df['company'].str.contains(search, case=False, na=False)
    ]
else:
    explore_df = filtered_df

st.markdown(f"**Showing {len(explore_df):,} jobs**")

# Show table
st.dataframe(
    explore_df[[
        'title',
        'company',
        'location',
        'salary',
        'work_type',
        'cluster_name',
        'all_skills_str'
    ]].head(50),
    use_container_width=True
)

st.markdown("---")

# ── FOOTER ───────────────────────────────────
st.markdown("""
    <div style='text-align: center; color: gray; padding: 20px'>
        <p>AI-Powered Job Market Intelligence Platform</p>
        <p>Built with Python, Streamlit, NLP & Machine Learning</p>
    </div>
""", unsafe_allow_html=True)