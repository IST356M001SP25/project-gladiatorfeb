# About My Project

Student Name:  Hassatou Daramey
Student Email:  hndarame@syr.edu

### What it does
# About the Project

## Overview
This project explores popular movies using the **OMDb API**. I built a data pipeline that extracts movie data based on trending search terms (e.g., "Barbie", "Oppenheimer", "Inception"), transforms it into a cleaner format, and visualizes it using **Streamlit**.

The goal was to practice the full data pipeline, including data extraction, transformation, analysis, and building an interactive dashboard.

## Technologies Used
- Python
- Pandas
- Plotly Express
- Streamlit
- OMDb API
- Pytest

## Project Structure

project/
│
├── code/
│ ├── extract.py # Grabs data from OMDb API and saves it to CSV
│ ├── transform.py # Cleans and processes the movie data
│ └── dashboard.py # Streamlit dashboard for data exploration
│
├── tests/
│ └── test_transform.py # Tests for transformation logic
│
├── cache/
│ ├── trending_movies.csv # Raw extracted data
│ └── transformed_movies.csv # Cleaned dataset
│
├── about-project.md # Project overview
└── reflection.md # Reflection on learning and challenges

### How you run my project


## How to Run

1. **Extract the data**  
   Run the following in your terminal:
   ```bash
   python code/extract.py

### Other things you need to know