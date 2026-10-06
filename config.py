import os
from dotenv import load_dotenv

# Load .env from the project root
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "movie_recommendation_secret_key")
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

    DATABASE = os.path.join("database", "users.db")

    MOVIES_DATASET = os.path.join("dataset", "movies.csv")
    RATINGS_DATASET = os.path.join("dataset", "ratings.csv")
    LINKS_DATASET = os.path.join("dataset", "links.csv")
    TAGS_DATASET = os.path.join("dataset", "tags.csv")

    MODEL_FOLDER = "model"

    SIMILARITY_MODEL = os.path.join(MODEL_FOLDER, "similarity.pkl")
    TFIDF_MODEL = os.path.join(MODEL_FOLDER, "tfidf_vectorizer.pkl")
    RECOMMENDER_MODEL = os.path.join(MODEL_FOLDER, "recommender.pkl")