Student Name: Hassatou Daramey  
Student Email: hndarame@syr.edu  

# About the Project

## Overview
This project explores popular movies using the OMDb API. I built a data pipeline that extracts movie data based on trending search terms (e.g., "Barbie", "Oppenheimer", "Inception"), transforms it into a cleaner format, and visualizes it using Streamlit.

The goal was to practice the full data pipeline, including:
- Data extraction from an API (OMDb)
- Data transformation with pandas
- Data visualization using Plotly and Streamlit
- Testing Python functions with Pytest

## Technologies Used
- Python  
- Pandas  
- Plotly Express  
- Streamlit  
- OMDb API  
- Pytest  

## Project Structure
project/
├── code/
│ ├── extract.py # Grabs data from OMDb API and saves it to CSV
│ ├── transform.py # Cleans and processes the movie data
│ └── dashboard.py # Streamlit dashboard for data exploration
├── tests/
│ └── test_transform.py # Unit tests for transformation logic
├── cache/
│ ├── trending_movies.csv # Raw extracted data (backup)
│ └── transformed_movies.csv # Cleaned dataset used in the dashboard
├── about-project.md # Project overview
└── reflection.md # Reflection on learning and challenges


## How to Run the Project

1. **Add your OMDb API key:**
   Open `extract.py` and replace this line:
   ```python
   API_KEY = "your_omdb_api_key"
