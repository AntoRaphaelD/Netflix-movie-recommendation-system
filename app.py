import streamlit as st
import pandas as pd
import pickle
import requests

# --- API and Data Loading ---

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):

    """Fetches a movie poster URL from the TMDB API."""
    try:
        api_key = st.secrets["TMDB_API_KEY"]
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Found" # Placeholder image
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None
    except KeyError:
        st.error("TMDB_API_KEY not found in secrets.toml. Please add it.")
        return None


# Load the data and similarity matrix
try:
    df = pd.read_csv('movies_df.csv')
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Data files not found. Make sure 'movies_df.csv' and 'similarity.pkl' are present.")
    st.stop()


# --- Recommendation Logic ---

def recommend(movie):
    """Recommends 5 movies and fetches their posters."""
    try:
        movie_index = df[df['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return [], []

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movies_list:
        movie_id = df.iloc[i[0]].movie_id
        recommended_titles.append(df.iloc[i[0]].title)
        # Fetch poster from API
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters


# --- Streamlit UI ---

st.set_page_config(layout="wide")
st.title('🎬 Movie Recommendation System')
st.markdown("Select a movie from the dropdown to get the top 5 similar movie recommendations.")

# Movie selection dropdown
movie_list = df['title'].values
selected_movie = st.selectbox('Select a movie you like:', movie_list)

# Recommendation button
if st.button('Recommend', type="primary"):
    with st.spinner('Finding recommendations...'):
        names, posters = recommend(selected_movie)

        if names: # Check if recommendations were found
            st.subheader("Here are your recommendations:")
            # Create 5 columns to display movies
            cols = st.columns(5, gap="medium")

            for i in range(5):
                with cols[i]:
                    st.text(names[i])
                    if posters[i]:
                        st.image(posters[i])
        else:
            st.warning("Could not generate recommendations. Please try another movie.")

# Add TMDB attribution as required by their terms of use
st.markdown("""
<hr>
<p style='text-align: center; font-size: 0.8em;'>
This service uses the TMDb API but is not endorsed or certified by TMDb.
</p>
""", unsafe_allow_html=True)