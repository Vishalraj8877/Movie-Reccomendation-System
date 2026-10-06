import joblib

movies = joblib.load("model/recommender.pkl")
similarity = joblib.load("model/similarity.pkl")

print(type(movies))
print(type(similarity))
print(similarity.shape)