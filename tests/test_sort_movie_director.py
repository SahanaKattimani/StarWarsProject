import pytest
from pages.movies_page import MoviesPage

def test_sort_movies_by_director_and_verify_last(driver):
    """
    UI Scenario 4: Sort movies by 'Director Name' and assert the last director in the list is 'Richard Marquand'.
    """
    movies_page = MoviesPage(driver)
    movies_page.navigate_to_movies_page()

    # Click the Title header to sort
    movies_page.sort_director_title()

    # Get all movie titles after sorting
    sorted_directors= movies_page.get_all_movie_directors()

    print(sorted_directors)

    # Check the expected last element based on that order.
    assert sorted_directors[-1] == "Richard Marquand", \
        f"Expected last movie to be 'Richard Marquand', but found '{sorted_directors[-1]}'"