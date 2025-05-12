import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Trending Movies Sentiment Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/movies_with_sentiment.csv")

df = load_data()

st.sidebar.header("Filter")
selected_sentiment = st.sidebar.selectbox("Select Sentiment", ["all"] + df["sentiment"].unique().tolist())

if selected_sentiment != "all":
    df = df[df["sentiment"] == selected_sentiment]

st.subheader("Sentiment Distribution")
st.plotly_chart(px.histogram(df, x="sentiment"))

st.subheader("Movie Ratings vs Sentiment")
st.plotly_chart(px.scatter(df, x="vote_average", y="popularity", color="sentiment", hover_name="title"))
