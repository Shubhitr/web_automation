from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service as ChromeService
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.find_element(By.XPATH, "//input[@placeholder = 'Username']").send_keys("admin123")
d.find_element(By.XPATH, "//input[@placeholder = 'Password']").send_keys( "Admin")
d.find_element(By.XPATH, "//button[@type = 'submit']").click()
act_tilte = d.title
except_tilte = "OrangeHRM"
if act_tilte == except_tilte:
    print("test cases pass")
else:
  print("test cases fail")

# open the new windows
d.execute_script("window.open('https://practice.expandtesting.com/dropdown#google_vignette')")
window_tabs = d.window_handles

print(window_tabs)
d.switch_to.window(window_tabs[0])



