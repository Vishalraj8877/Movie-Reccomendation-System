from recommend import recommend

movies = recommend("Toy Story")

for movie in movies:
    print(movie["title"])
    print(movie["poster"])