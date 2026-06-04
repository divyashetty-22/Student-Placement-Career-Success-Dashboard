import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Salary Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="salary"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    placed = df[df["salary_lpa"] > 0]

    fig = px.histogram(
        placed,
        x="salary_lpa",
        nbins=30,
        title="Salary Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    branch_salary = (
        placed.groupby("branch")["salary_lpa"]
        .mean()
        .reset_index()
        .sort_values(
            "salary_lpa",
            ascending=False
        )
    )

    fig2 = px.bar(
        branch_salary.head(10),
        x="branch",
        y="salary_lpa",
        title="Top 10 Branches by Salary"
    )

    st.plotly_chart(fig2, use_container_width=True)
