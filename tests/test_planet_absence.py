import pytest
from pages.movies_page import MoviesPage

def test_planet_camino_not_in_phantom_menace(driver):
    """
    UI Scenario 3: Assert that 'Planets' 'Camino' is not part of the movie 'The Phantom Menace'.
    """
    movies_page = MoviesPage(driver)
    movies_page.navigate_to_movies_page()

    # Click on "The Phantom Menace" to view its details
    movie_details_page = movies_page.click_movie_title("The Phantom Menace")

    # Get the list of planets
    planets_list = movie_details_page.get_planets_list()

    # Assert 'Camino' is NOT in the planets list
    assert "Camino" not in planets_list, \
        f"Expected 'Camino' NOT to be in planets list for 'The Phantom Menace', but it was found."