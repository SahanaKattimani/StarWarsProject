from selenium.webdriver.common.by import By


class MoviesPageLocators:
    """Locators for the main Movies listing page."""
    TITLE_HEADER = (By.XPATH, "//th")
    MOVIE_TITLES = (By.XPATH, "//tbody//a[@class='underline font-medium']")
    MOVIE_TITLE_LINK_BY_TEXT = lambda title: (By.XPATH, f"//a[text()='{title}']")