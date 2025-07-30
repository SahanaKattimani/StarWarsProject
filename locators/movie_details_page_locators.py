# locators/movie_details_page_locators.py
from selenium.webdriver.common.by import By

class MovieDetailsPageLocators:
    # Main movie title on the details page
    MOVIE_DETAIL_TITLE = (By.XPATH, f"//*[contains(text(), 'The Empire Strikes Back')]")
    # List of species associated with the movie
    SPECIES_LIST_ITEMS = (By.XPATH, "//div/following-sibling::ul/li")
    # List of planets associated with the movie
    PLANETS_LIST_ITEMS = (By.XPATH, "//h1[contains(text(), 'Planets')]/../following-sibling::ul/li")
    # Back button link to return to the movies list
    BACK_TO_MOVIES_LINK = (By.XPATH, "//a")