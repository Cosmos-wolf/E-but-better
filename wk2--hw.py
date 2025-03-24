favorite_movies = []

for i in range(5):
    movie = input(f"Enter your favorite movie {i+1}: ")
    favorite_movies.append(movie)

print("\nYour favorite movies in reverse order are:")
for movie in reversed(favorite_movies):
    print(movie)
