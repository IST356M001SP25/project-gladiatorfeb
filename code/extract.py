import os
import requests
import pandas as pd

API_KEY = os.getenv("OMDB_API_KEY")

if API_KEY is None:
    raise ValueError("OMDb API key not found. Please set it in your environment variables.")

SEARCH_TERMS = ["Avengers", "Inception", "Frozen", "Barbie", "Oppenheimer"]

def fetch_movies(search_terms):
    movies = []
    for term in search_terms:
        url = f"http://www.omdbapi.com/?s={term}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            for item in data["Search"]:
                movies.append(item)
        else:
            print(f"No results for {term}: {data.get('Error')}")

    return pd.DataFrame(movies)

def save_to_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = fetch_movies(SEARCH_TERMS)
    
    if not df.empty:
        save_to_csv(df, "data/raw/trending_movies.csv")
        print("Movies saved to data/raw/trending_movies.csv")
    else:
        print("No movies to save. Please check the search terms.")
