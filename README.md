# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on movie metadata like genres, keywords, cast, and crew. Built with Python, scikit-learn, and deployed as an interactive web application using Streamlit.

## Features

- **Content-Based Filtering**: Recommends movies based on content similarity
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Movie Posters**: Fetches real-time movie posters from TMDB API
- **5 Recommendations**: Returns top 5 similar movies for any selected film
- **4800+ Movies**: Trained on TMDB 5000 Movie Dataset
- **Text Processing**: Uses TF-IDF vectorization and stemming for better results

## Demo

<img width="1919" height="734" alt="image" src="https://github.com/user-attachments/assets/38a246f6-5c34-4fbc-bc3d-a9f931e73633" />
<img width="1876" height="882" alt="image" src="https://github.com/user-attachments/assets/50b14d06-406c-4cdb-8628-ead4729e4a77" />

## Dataset

This project uses the **TMDB 5000 Movie Dataset** containing:
- 4,806 movies
- Movie metadata (genres, keywords, cast, crew)
- Movie overviews and descriptions

**Dataset Source**: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


## Project Structure

```
movie-recommender-system/
│
├── MRS.ipynb                 # Jupyter notebook with complete analysis
├── app.py                    # Streamlit web application
├── movies_df.csv             # Processed movie data
├── similarity.pkl            # Precomputed similarity matrix
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore               # Git ignore file
│
├── .streamlit/
│   └── secrets.toml         # API keys (not in git)
│
├── tmdb_5000_movies.csv     # Original datasets
└── tmdb_5000_credits.csv
```

## How It Works

### 1. Data Processing
- Merges movie and credits datasets
- Extracts relevant features (genres, keywords, cast, crew)
- Processes text data (lowercase, remove spaces)

### 2. Feature Engineering
- Combines multiple features into a single 'tags' column
- Applies stemming using NLTK's PorterStemmer
- Creates a unified text representation for each movie

### 3. Vectorization
- Uses **TF-IDF Vectorization** to convert text to numerical vectors
- Removes English stop words
- Creates a document-term matrix

### 4. Similarity Calculation
- Computes **Cosine Similarity** between all movie vectors
- Stores similarity matrix for fast recommendations

### 5. Recommendation
- Finds the input movie's index
- Retrieves top 5 most similar movies
- Fetches movie posters from TMDB API

## Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **scikit-learn**: Machine learning (TF-IDF, Cosine Similarity)
- **NLTK**: Natural language processing (Stemming)
- **Streamlit**: Web application framework
- **Requests**: HTTP library for API calls
- **TMDB API**: Movie posters and metadata

---
