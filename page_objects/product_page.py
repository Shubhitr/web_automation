import random
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from locators. product_page_locator import ProductPageLocator


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    product_name_locator = (By.XPATH, ProductPageLocator.product_name_title)
    add_to_cart_locator = (By.XPATH, ProductPageLocator.add_to_cart_button)
    multiple_add_to_cart_locator = (By.XPATH, ProductPageLocator.add_to_cart_xpath)

    def click_product_name(self):
        self.click_element(self.product_name_locator)

    def click_add_to_cart(self):
        self.click_element(self.add_to_cart_locator)

    def click_multiple_add_to_cart_button(self, count=None):
        # breakpoint()
        add_to_cart_element_l = self.find_elements(self.multiple_add_to_cart_locator)

        add_to_cart_element_l = random.choices(add_to_cart_element_l, k=count)
        for ele in add_to_cart_element_l:
            ele.click()



