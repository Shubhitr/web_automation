from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    # Explanation..?
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_json(self):
        pass




