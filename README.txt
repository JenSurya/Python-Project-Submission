# Movie Recommendation Bot

This project is a movie recommendation bot that fetches movie data from the TMDB based on user-selected genres and filters the movies based on user-specified criteria such as popularity, rating and release year.

## Project Structure

- `python_project_submission.py`: Main script to handle user interaction and fetch movie data.
- `movies_list.py`: Module to fetch and process movie data.
- `genres.py`: Module to fetch and cache movie genres.

## Setup

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required packages using pip:
    ```sh
    pip install requests pandas
    ```

## Usage

1. Run the main script:
    ```sh
    python python_project_submission.py
    ```

2. Follow the prompts to select a genre and filter criteria.

## Modules

### `python_project_submission.py`

This is the main script that handles user interaction. It performs the following tasks:
- Fetches available genres.
- Displays available genres to the user.
- Gets user input for genre selection.
- Fetches movies for the selected genre.
- Processes movie data.
- Gets user input for filtering criteria.
- Filters movies based on criteria.
- Suggests movies to the user.
- Provides a random movie suggestion.

### `movies_list.py`

This module contains functions to fetch and process movie data:
- `fetch_movie_data(genre_id)`: Fetches movies based on the genre ID from the TMDB API.
- `process_movie_data(movies)`: Processes the fetched movie data into a Pandas DataFrame.
- `filter_movies(df, criteria, value)`: Filters the DataFrame based on user-specified criteria.
- `suggest_movies(df)`: Prints the list of filtered movies.
- `random_movie_suggestion(df)`: Provides a random movie suggestion from the filtered list.

### `genres.py`

This module fetches and caches movie genres from the TMDB API:
- `fetch_genres()`: Fetches the list of genres from the TMDB API and caches the result.

## API Key

In this project, we used the TMDB API to fetch movie data. Ensure you have a valid API key and replace the placeholder in the code with your actual API key.
