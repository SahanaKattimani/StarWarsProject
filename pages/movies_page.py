from base.base_page import BasePage
from locators.movies_page_locators import MoviesPageLocators
from pages.movie_details_page import MovieDetailsPage

class MoviesPage(BasePage):

    URL = "http://localhost:3000/"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_movies_page(self):
        """Navigates to the movies listing page and waits for the title header to be present."""
        self.navigate_to(self.URL)
        self.find_element(MoviesPageLocators.TITLE_HEADER) # Ensure the page is loaded

    def sort_movies_by_title(self):
        """Clicks the 'Title' header to sort the movies."""
        self.click(MoviesPageLocators.TITLE_HEADER)

    def get_all_movie_titles(self):
        """Retrieves a list of all movie titles displayed in the table."""
        title_elements = self.find_elements(MoviesPageLocators.MOVIE_TITLES)
        return [element.text for element in title_elements]

    def click_movie_title(self, movie_title):
        """Clicks on a specific movie title link to navigate to its details page."""
        locator = MoviesPageLocators.MOVIE_TITLE_LINK_BY_TEXT(movie_title)
        self.click(locator)
        return MovieDetailsPage(self.driver)