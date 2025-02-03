import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver

d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
d.get("https://www.flipkart.com")
# open the new window
d.execute_script("window.open('https://www.amazon.com')")
d.maximize_window()



d.execute_script("window.open('https://mypage.rediff.com/login')")
d.execute_script("window.open('https://demo.automationtesting.in/Register.html')")


tab_l = d.window_handles
print(tab_l)
d.switch_to.window(tab_l[0])
d.switch_to.window(tab_l[1])

# USing Select for dropdown

ele = d.find_element(By.XPATH, "//select[@id='Skills']")
drop_drown = Select(ele)
drop_drown.select_by_visible_text("Android")
options = drop_drown.options

for item in options:
    print(item.text)
    drop_drown.select_by_visible_text(item.text)
    breakpoint()

# drop_drown.deselect_by_visible_text("Android")
# drop_drown.sel



# Alert_POPUP
# ele_a = WebDriverWait(d,10).until(EC.visibility_of_element_located((By.XPATH, "//button[@onclick='jsPrompt()']")))
# ele_a.click()
# alert_popup= d.switch_to.alert

# alert_popup.accept()
# alert_popup.send_keys()
# alert_popup.dismiss()
# a = alert_popup.text

# Syntax: https://username:password@adcuratio.com


# ele_a.click()



ele = d.find_elements(By.XPATH, "")
# WebDriverWait(d,10).until(EC.presen)




# d.execute_script("window.open('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')")







# d.find_element(By.XPATH, "//div//a[@href = '/account/login?ret=/']").click()

