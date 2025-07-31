import pytest
from pages.movies_page import MoviesPage

def test_view_empire_strikes_back_species(driver):
    """
    UI Scenario 2: View the movie 'The Empire Strikes Back' and check if the 'Species' list has 'Wookie'.
    """
    movies_page = MoviesPage(driver)
    movies_page.navigate_to_movies_page()

    # Click on "The Empire Strikes Back" to view its details
    movie_details_page = movies_page.click_movie_title("The Empire Strikes Back")

    # Get the list of species
    species_list = movie_details_page.get_species_list()

    # Assert 'Wookie' is in the species list
    assert "Wookie" in species_list, \
        f"Expected 'Wookie' to be in species list for 'The Empire Strikes Back', but found {species_list}"