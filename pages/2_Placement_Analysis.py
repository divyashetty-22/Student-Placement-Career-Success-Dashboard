import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Placement Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="placement"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    placement = (
        df["placement_status"]
        .value_counts()
        .reset_index()
    )

    placement.columns = ["Status", "Count"]

    fig = px.pie(
        placement,
        names="Status",
        values="Count",
        title="Placement Status Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(placement)
