from locators.login_page_locator import LoginPageLocator
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    login_user_name_loc = (By.XPATH, LoginPageLocator.login_user_name_xpath)
    # not using self but calling this locator using self why?
    login_password_loc = (By.XPATH, LoginPageLocator.login_password_xpath)
    login_button_loc = (By.XPATH, LoginPageLocator.login_button_xpath)


    def enter_user_name(self, text):
        self.enter_text(self.login_user_name_loc, text)

    def enter_user_password(self, text):
        self.enter_text(self.login_password_loc, text)

    def click_login_button(self):
        self.click_element(self.login_button_loc)
