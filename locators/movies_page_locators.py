# locators/movies_page_locators.py
from selenium.webdriver.common.by import By


class MoviesPageLocators:
    """Locators for the main Movies listing page."""
    TITLE_HEADER = (By.XPATH, "//th") # Table header for sorting by Title
    MOVIE_TITLES = (By.XPATH, "//tbody//a[@class='underline font-medium']") # All movie title links in the table body
    MOVIE_TITLE_LINK_BY_TEXT = lambda title: (By.XPATH, f"//a[text()='{title}']") # Specific movie title link by its text (dynamic locator)