import requests
import pandas as pd
#Pandas to process the movie data.

API_KEY = 'e3bd1daa94b3b517d13d8f4cff921430'
BASE_URL = 'https://api.themoviedb.org/3/discover/movie'

def fetch_movie_data(genre_id):

    #Fetching movies based on the genre ID from the TMDB API.
    
    #Args - genre_id: The ID of the genre to fetch movies for
    
    #Returns - Movies: A list of movies in the specific genre.
    
    try:
        response = requests.get(BASE_URL, params={'api_key': API_KEY, 'with_genres': genre_id})
        response.raise_for_status()
        movies = response.json().get('results', [])
        return movies
    except requests.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return []

def process_movie_data(movies):
    #Pandas implementation to process the movie data.
    
    #Args - movies : To get the list of movies to process.
    
    #Returns - pd.DataFrame: A DataFrame containing the processed movie data.
    
    movie_list = []
    for movie in movies:
        movie_list.append({
            'Title': movie.get('title'),
            'Genre': ', '.join([str(genre_id) for genre_id in movie.get('genre_ids', [])]),
            'Release Year': movie.get('release_date', '').split('-')[0],
            'Popularity': movie.get('popularity'),
            'Rating': movie.get('vote_average') * 10
        })
    return pd.DataFrame(movie_list)

def filter_movies(df, criteria, value):
    #Filters the DataFrame based on user entered criteria
    
    #Args:
    #  df (pd.DataFrame): The DataFrame containing movie data
    #  criteria (str): The criteria to filter by ('popularity', 'rating', or 'year')
    # value (float or int): The value to filter by
    
    #Returns: pd.DataFrame: The filtered DataFrame.

    if criteria == 'popularity':
        return df[df['Popularity'] >= value]
    elif criteria == 'rating':
        return df[df['Rating'] >= value]
    elif criteria == 'year':
        return df[df['Release Year'] == str(value)]
    else:
        print("Invalid criteria. Please choose from 'popularity', 'rating', or 'year'.")
        return df

def suggest_movies(df):
    
    #Prints the list of filtered movies.
    
    #Args:
    #df (pd.DataFrame): The DataFrame containing filtered movie data.
    
    try:
        print(df[['Title', 'Rating', 'Popularity', 'Release Year']])
    except Exception as e:
        print(f"Error during suggestion: {e}")

def random_movie_suggestion(df):
    #Prints the random movie suggestion from the filtered list.
    
    try:
        if not df.empty:
            random_movie = df.sample(n=1).iloc[0]
            print(f"Random Movie Suggestion: {random_movie['Title']} ({random_movie['Release Year']}) - Rating: {random_movie['Rating']}")
        else:
            print("No movies found for the selected criteria.")
    except Exception as e:
        print(f"Error during random suggestion: {e}")