import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)

def test_windows():
    d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    d.get("https://www.flipkart.com")
    d.maximize_window()
    print(d.title)

    expected_title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"

    assert d.title == expected_title, "title not meatched"

    # d.execute_script("https://www.amazon.com/Best-Sellers/zgbs')")
    d.execute_script("window.open('https://the-internet.herokuapp.com/javascript_alerts')")
    tabs = d.window_handles
    print(tabs)
    d.switch_to.window(tabs[1])
    # breakpoint()
#alertpopup:
    element_iden = d.find_element(By.XPATH, "//button[normalize-space(text())= 'Click for JS Prompt']")

    element_iden.is_selected()
    print("element_iden.is_selected()")
    element_iden.click()
    alert_window = d.switch_to.alert
    time.sleep(5)
    print(alert_window.text)
    alert_window.send_keys("welcome")
    # alert_window.dismiss()
    breakpoint()
#     alert_window.sendkeys("welcome")
#     alert_window.accept



















# # is_displayed()
#     search_box = d.find_element(By.XPATH, "//div//input[@type = 'text']")
#     search_box.is_displayed()
#     logger.info("searchbox_displayed")
#     # breakpoint()


    d.execute_script("window.open('https://practice.expandtesting.com/checkboxes')")
    # # expected_title = ""
    # print(d.title)
    # time.sleep(2)
    # checkbox_element_l = WebDriverWait(d, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//label[@class='form-check-label']")))
    # for item in checkbox_element_l:
    #     print(item.text)
    #     selection_radio_button = "//label[normalize-space(text())='{}']//preceding-sibling::input".format(item.text)
    #     radio_button = d.find_element(By.XPATH, selection_radio_button)
    #     radio_button.click()
    #     radio_button.is_selected()
    #     logger.info("radio_button is selected")
    # breakpoint()


# find_elements:


