import streamlit as st
import pandas as pd

st.title("Dataset Overview")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Branches", df["branch"].nunique())
    c4.metric("States", df["state"].nunique())

    st.dataframe(df.head(20))

    st.subheader("Data Types")
    st.write(df.dtypes)
