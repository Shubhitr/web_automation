from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.rediff_page_locator import RediffPageLocator


class RediffPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    select_Indiahomeloan_locator = (By.XPATH, RediffPageLocator.select_Indiahomeloan_xpath)


    def click_Indiahome_loan(self):
        self.click_element(self.select_Indiahomeloan_locator)