import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Skills Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="ai"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    fig = px.scatter(
        df.sample(min(3000, len(df))),
        x="prompt_engineering_skill",
        y="salary_lpa",
        color="placement_status",
        title="Prompt Engineering Skill vs Salary"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.scatter(
        df.sample(min(3000, len(df))),
        x="AI_tool_usage_frequency",
        y="adaptability_score",
        color="placement_status",
        title="AI Tool Usage vs Adaptability"
    )

    st.plotly_chart(fig2, use_container_width=True)
