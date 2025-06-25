import streamlit as st
import pandas as pd
import plotly.express as px

# Load Excel file
df = pd.read_excel("analysis_output.xlsx")

st.set_page_config(layout="wide")
st.title("📰 Text Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_ids = st.sidebar.multiselect("Select URL IDs", df["URL_ID"].unique())
if selected_ids:
    df = df[df["URL_ID"].isin(selected_ids)]

# Metrics at top
col1, col2, col3 = st.columns(3)
col1.metric("Avg Polarity", round(df["POLARITY SCORE"].mean(), 3))
col2.metric("Avg Subjectivity", round(df["SUBJECTIVITY SCORE"].mean(), 3))
col3.metric("Avg Fog Index", round(df["FOG INDEX"].mean(), 2))

# Sentiment Overview
st.subheader("📊 Sentiment Score Comparison")
fig_sentiment = px.bar(
    df,
    x="URL_ID",
    y=["POSITIVE SCORE", "NEGATIVE SCORE"],
    barmode="group",
    title="Positive vs. Negative Sentiment per Article"
)
st.plotly_chart(fig_sentiment, use_container_width=True)

# Fog Index Trend
st.subheader("📈 Readability - Fog Index")
fig_fog = px.line(df, x="URL_ID", y="FOG INDEX", markers=True)
st.plotly_chart(fig_fog, use_container_width=True)

# Word Count Histogram
st.subheader("🔤 Word Count & Complexity")
col4, col5 = st.columns(2)
with col4:
    fig_wordcount = px.histogram(df, x="WORD COUNT", nbins=20)
    st.plotly_chart(fig_wordcount, use_container_width=True)

with col5:
    fig_wordlen = px.histogram(df, x="AVG WORD LENGTH", nbins=20)
    st.plotly_chart(fig_wordlen, use_container_width=True)

# Data Table
st.subheader("📋 Full Data Table")
st.dataframe(df)

# Download
st.download_button(
    label="📥 Download Filtered Results",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_analysis.csv",
    mime="text/csv"
)
