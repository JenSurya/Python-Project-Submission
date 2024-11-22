import genres as genres_list
import movies_list as movies_list

def main():
    #Main function to fetching genres and movies list based on user input

    # Fetching available genres
    genres = genres_list.fetch_genres()
    if not genres:
        return

    # Displaying available genres
    print("Available genres:")
    for genre in genres:
        print(genre)

    while True:
        # Getting genre from User
        genre_name = input("Please specify the genre for which you would like recommendations, or type 'exit' to terminate the session: ").strip()
        if genre_name.lower() == 'exit':
            break
        genre_id = genres.get(genre_name)
        if not genre_id:
            print("The selected genre is invalid. Kindly re-enter a valid option.")
            continue

        # Fetching movies based on the selected genre
        movies = movies_list.fetch_movie_data(genre_id)
        if not movies:
            print("No movies found for the selected genre.")
            continue

        # Processing movie data
        movie_df = movies_list.process_movie_data(movies)

        # Getting user input for filtering criteria
        criteria = input("Please specify the criteria for filtering (e.g., popularity, rating, year): ").strip().lower()
        if criteria in ['popularity', 'rating']:
            try:
                value = float(input(f"Please enter the minimum {criteria}: ").strip())
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
        elif criteria == 'year':
            try:
                value = int(input(f"Please enter the release year: ").strip())
            except ValueError:
                print("Invalid input. Please enter a valid year.")
                continue
        else:
            print("Invalid criteria. Please choose from 'popularity', 'rating', or 'year'.")
            continue

        # Filtering movies based on chosen criteria
        filtered_movies = movies_list.filter_movies(movie_df, criteria, value)
        if filtered_movies.empty:
            print("No movies found for the selected criteria.")
            continue

        # Suggesting random movies for the user
        movies_list.suggest_movies(filtered_movies)
        movies_list.random_movie_suggestion(filtered_movies)

if __name__ == "__main__":
    main()