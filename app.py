from flask import Flask, render_template, request, jsonify
from config import Config
from recommend import recommend as recommend_movies
from utils.database import initialize_database
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database when app starts
initialize_database()


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):

    from recommend import movies
    from utils.tmdb_by_id import get_movie_details

    movie = movies[movies["movieId"] == movie_id]

    if movie.empty:
        return render_template("error.html"), 404

    movie = movie.iloc[0]

    tmdb = get_movie_details(movie["tmdbId"])

    data = {
        "movieId": int(movie["movieId"]),
        "title": movie["title"],
        "genres": movie["genres"],
        "rating": round(movie["average_rating"], 2),
        **tmdb
    }

    return render_template("movie.html", movie=data)
@app.route("/recommend", methods=["POST"])
def recommend_route():

    movie = request.form.get("movie")

    if not movie:
        return jsonify({
            "status": "error",
            "message": "Movie name is required."
        }), 400

    recommendations = recommend_movies(movie)

    if not recommendations:
        return jsonify({
            "status": "error",
            "message": "Movie not found."
        }), 404

    return jsonify({
        "status": "success",
        "movie": movie,
        "recommendations": recommendations
    })

from rapidfuzz import process
from recommend import movies


@app.route("/search")
def search():

    query = request.args.get("q", "").strip()

    if len(query) < 2:
        return jsonify([])

    titles = movies["title"].tolist()

    results = process.extract(
        query,
        titles,
        limit=8
    )

    suggestions = [
        title for title, score, _ in results
        if score >= 60
    ]

    return jsonify(suggestions)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error.html"), 500


if __name__ == "__main__":
    app.run(debug=True)