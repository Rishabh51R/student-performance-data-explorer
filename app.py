import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    h1 {
        color: #1f3c88;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Student Performance Dashboard")
st.write("Explore and analyze student performance data.")

# Load dataset
df = pd.read_csv("student_performance.csv")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Average Final Score", round(df["final_score"].mean(), 2))

with col3:
    st.metric("Highest Score", df["final_score"].max())

with col4:
    st.metric("Average Study Hours", round(df["study_hours"].mean(), 2))

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    fig1 = px.scatter(
        df,
        x="study_hours",
        y="final_score",
        title="Study Hours vs Final Score",
        color="gender"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(
        df,
        x="final_score",
        title="Final Score Distribution",
        nbins=10
    )
    st.plotly_chart(fig2, use_container_width=True)

# Data table
st.subheader("📊 Student Data")
st.dataframe(df, use_container_width=True)
