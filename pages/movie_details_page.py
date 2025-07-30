# pages/movie_details_page.py
from base.base_page import BasePage
from locators.movie_details_page_locators import MovieDetailsPageLocators

class MovieDetailsPage(BasePage):
    """Page Object for the Movie Details page."""

    def __init__(self, driver):
        super().__init__(driver)
        # Optionally, add a check to ensure the movie details page is loaded
        self.find_element(MovieDetailsPageLocators.MOVIE_DETAIL_TITLE)

    def get_movie_detail_title(self):
        """Retrieves the title of the movie on the details page."""
        return self.get_text(MovieDetailsPageLocators.MOVIE_DETAIL_TITLE)

    def get_species_list(self):
        """Retrieves a list of species associated with the movie."""
        species_elements = self.find_elements(MovieDetailsPageLocators.SPECIES_LIST_ITEMS)
        return [element.text for element in species_elements]

    def get_planets_list(self):
        """Retrieves a list of planets associated with the movie."""
        planet_elements = self.find_elements(MovieDetailsPageLocators.PLANETS_LIST_ITEMS)
        return [element.text for element in planet_elements]

    def go_back_to_movies_list(self):
        """Clicks the back button/link to return to the main movies list."""
        self.click(MovieDetailsPageLocators.BACK_TO_MOVIES_LINK)
        from pages.movies_page import MoviesPage # Import here to avoid circular dependency
        return MoviesPage(self.driver)