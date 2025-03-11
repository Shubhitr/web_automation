from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from conftest import driver

# driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def find_element(locator):
    return WebDriverWait(d, 20).until(EC.visibility_of_element_located(locator))

        # find_element((By.XPATH, "//input[@placeholder = 'Username']")).send_keys("Admin")
        # find_element((By.XPATH, "//input[@placeholder = 'Password']")).send_keys( "admin123")
        # find_element((By.XPATH, "//button[@type = 'submit']")).click()
        #
        # act_tilte = d.title
        # except_tilte = "OrangeHRM"
        # if act_tilte == except_tilte:
        #     print("test cases pass")
        # else:
        #   print("test cases fail")

# open the new windows
#         d.execute_script("window.open('https://money.rediff.com/gainers')")
#         breakpoint()
#         window_tabs = d.window_handles
#
#         print(window_tabs)
#         d.switch_to.window(window_tabs[2])


# learn : get attribute and text
# https://money.rediff.com/gainers

    # driver_obj = d.find_element(By.XPATH, '//a[@href = "//money.rediff.com/companies/indegene/11140174]')
    # text_ = driver_obj.text #Returns only visible text of an element.
    # print(text_)

# <a id="my-link" href="https://example.com" target="_blank">Click here</a>
#     driver_ = d.find_element(By.XPATH, '//a[@id = "my-link"]')
#     get_att_ = driver_.get_attribute("href")
#     print(get_att_)  # Output: https://example.com

# ALERT_WINDOW:
# https://www.tutorialspoint.com/selenium/practice/alerts.php

        # d.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
        #
        # find_element((By.XPATH, "//button[@onclick = 'myPromp()']")).click()
        # breakpoint()
        # alert_window = d.switch_to.alert
        # print(alert_window.text)
        # alert_window.send_keys("hello")
        # alert_window.accept()

# MOUSE_ACTION:









