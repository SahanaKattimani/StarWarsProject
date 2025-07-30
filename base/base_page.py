# base/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """Waits for an element to be present and returns it."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not found within timeout.")

    def find_elements(self, locator):
        """Waits for elements to be present and returns them."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Elements with locator {locator} not found within timeout.")

    def click(self, locator):
        """Waits for an element to be clickable and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Waits for an element to be visible and sends text to it."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Waits for an element to be visible and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def navigate_to(self, url):
        """Navigates the browser to the specified URL."""
        self.driver.get(url)