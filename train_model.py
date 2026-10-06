import os
import joblib

from utils.preprocessing import preprocess_movies
from utils.similarity import build_similarity_model

from config import Config


def train():

    print("=" * 50)
    print("Loading dataset...")

    movies = preprocess_movies()

    print(f"Movies Loaded : {len(movies)}")

    print("Building similarity model...")

    similarity = build_similarity_model(movies)

    os.makedirs(Config.MODEL_FOLDER, exist_ok=True)

    joblib.dump(movies, Config.RECOMMENDER_MODEL)

    print("Model Saved Successfully")

    print(f"Similarity Matrix Shape : {similarity.shape}")

    print("=" * 50)


if __name__ == "__main__":
    train()