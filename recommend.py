import joblib
from rapidfuzz import process
from utils.tmdb_by_id import get_movie_details
import utils.tmdb_by_id
print(utils.tmdb_by_id.__file__)
movies = joblib.load("model/recommender.pkl")
similarity = joblib.load("model/similarity.pkl")


def recommend(movie_name, top_n=10):

    movie_name = movie_name.lower().strip()

    from rapidfuzz import process

    titles = movies["title"].tolist()

    titles = movies["title"].tolist()

    best_match = process.extractOne(
        movie_name,
        titles,
        score_cutoff=60
    )

    if best_match is None:
        return None

    movie_title = best_match[0]

    if best_match is None:
         return None

    movie_title = best_match[0]

    matches = movies[movies["title"] == movie_title]

    movie_index = matches.index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for idx, score in distances[1:top_n + 1]:

        movie = movies.iloc[idx]

        try:
            tmdb = get_movie_details(movie["tmdbId"])
        except Exception:
            tmdb = None

        recommendations.append({

        "movieId": int(movie["movieId"]),

        "title": movie["title"],

        "genres": movie["genres"],

        "rating": round(movie["average_rating"], 2),

        "poster": tmdb["poster"] if tmdb else "",

        "overview": tmdb["overview"] if tmdb else "",

        "release_date": tmdb["release_date"] if tmdb else "",

        "tmdb_rating": tmdb["tmdb_rating"] if tmdb else "N/A"
        })

     
    print("Returning", len(recommendations), "movies")
    return recommendations