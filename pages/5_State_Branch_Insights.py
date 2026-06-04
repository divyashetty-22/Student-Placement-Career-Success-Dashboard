import streamlit as st
import pandas as pd
import plotly.express as px

st.title("State & Branch Insights")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="state"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    state_rate = (
        df.groupby("state")
        ["salary_lpa"]
        .mean()
        .reset_index()
        .sort_values(
            "salary_lpa",
            ascending=False
        )
    )

    fig = px.bar(
        state_rate.head(15),
        x="state",
        y="salary_lpa",
        title="Top States by Average Salary"
    )

    st.plotly_chart(fig, use_container_width=True)

    branch_count = (
        df["branch"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    branch_count.columns = [
        "Branch",
        "Students"
    ]

    fig2 = px.bar(
        branch_count,
        x="Branch",
        y="Students",
        title="Most Popular Branches"
    )

    st.plotly_chart(fig2, use_container_width=True)
