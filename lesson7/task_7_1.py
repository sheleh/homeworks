# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.

def movie(movie_name=False):
    if not movie_name or movie_name[0] == ' ':
        movie_name = input('Please enter your favorite movie name: ')
    print(f'The name of my favorite movie is {movie_name.title()}')


movie('kill bill')
