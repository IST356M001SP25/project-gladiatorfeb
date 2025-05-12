import pandas as pd
import os
from textblob import TextBlob

def analyze_sentiment(text):
    if not isinstance(text, str):
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def transform_movie_data(input_file="data/raw/trending_movies.csv", output_file="data/processed/movies_with_sentiment.csv"):
    df = pd.read_csv(input_file)
    df['sentiment'] = df['overview'].apply(analyze_sentiment)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    return df

if __name__ == "__main__":
    transform_movie_data()
