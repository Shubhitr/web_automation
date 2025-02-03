import time

from page_objects.naukri_page import NaukriPage

def test_naukri_login(driver):

    np = NaukriPage(driver)
    np.open_url("https://www.naukri.com/")
    np.select_login_button()
    np.enter_email_add("shubhitrivedi40@gmail.com")
    np.enter_password("Dodo@0000")
    np.click_login_button()
    time.sleep(2)
    # np.open_url("https://www.naukri.com/mnjuser/profile")
    resume_path = "../Shubhi_Trivedi_Resume.pdf"
    # Formatting xpath in below function
    np.click_view_profile('profile')
    # chatbox how to handle it, searched at chatghpt and answer is here: assert not driver.find_element(By.CLASS_NAME, 'chatbox').is_displayed()
    breakpoint()

