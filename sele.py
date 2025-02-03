from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
d.get("https://www.google.com")

d.execute_script("window.open('https://demo.automationtesting.in/Register.html', '_blank');")
# ele = d.find_element(By.XPATH, "")
tabs = d.window_handles
print("All Tabs:", tabs)
d.switch_to.window(tabs[0])
print("Switched Back to First Tab:", d.title)
ele = WebDriverWait(d, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Gmail']")))
ele.click()
d.switch_to.window(tabs[1])
dropdown = Select(WebDriverWait(d, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='Skills']"))))
dropdown.select_by_visible_text("AutoCAD")
all_option = dropdown.options
for option in all_option:
    print(option.text)

breakpoint()
