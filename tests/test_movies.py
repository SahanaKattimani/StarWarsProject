# tests/test_movies.py
import pytest
from pages.movies_page import MoviesPage

def test_sort_movies_by_title_and_verify_last(driver):
    """
    UI Scenario 1: Sort movies by 'Title' and assert the last movie in the list is 'The Phantom Menace'.
    """
    movies_page = MoviesPage(driver)
    movies_page.navigate_to_movies_page()

    # Click the Title header to sort
    movies_page.sort_movies_by_title()

    # Get all movie titles after sorting
    sorted_titles = movies_page.get_all_movie_titles()

    # Check the expected last element based on that order.
    assert sorted_titles[-1] == "The Phantom Menace", \
        f"Expected last movie to be 'The Phantom Menace', but found '{sorted_titles[-1]}'"