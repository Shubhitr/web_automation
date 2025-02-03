from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.naukri_page_locator import NaukriPageLocator


class NaukriPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    select_login_button_locator = (By.XPATH, NaukriPageLocator.select_login_button_xpath)
    login_email_adrress_locator = (By.XPATH, NaukriPageLocator.login_user_email_xpath)
    login_password_locator = (By.XPATH, NaukriPageLocator.login_user_password_xpath)
    click_login_button_locator = (By.XPATH, NaukriPageLocator.click_login_button_xpath)
    click_profile_button_locator = (By.XPATH, NaukriPageLocator.click_naukri_profile_xpath)
    upload_button_locator = (By.XPATH, "//input[@class='dummyUpload typ-14Bold']")

    def select_login_button(self):
        self.click_element(self.select_login_button_locator)

    def enter_email_add(self, text):
        self.enter_text(self.login_email_adrress_locator, text)

    def enter_password(self, text):
        self.enter_text(self.login_password_locator, text)

    def click_login_button(self):
        self.click_element(self.click_login_button_locator)

    def click_view_profile(self, text):
        loca_l = list(self.click_profile_button_locator)
        loca_l[1] = loca_l[1].format(text)
        self.click_element(loca_l)
        print(self.find_element(self.upload_button_locator).get_attribute('value'))


