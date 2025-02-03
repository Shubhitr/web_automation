import logging
import os
import pytest
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage
from utils.file_ops_utils import FileOps
global_driver = None
logger = logging.getLogger(__name__)

@pytest.mark.login
def test_flipkart_login(driver):
    global global_driver
    global_driver = driver
    wd = LoginPage(driver)
    wd.open_url("https://www.saucedemo.com/")
    wd.enter_user_name("standard_user")
    logger.info("User name entered successfully")
    wd.enter_user_password("secret_sauce")
    logger.info("Password entered successfully")
    wd.click_login_button()
    logger.error("Click button failed")
    file_obj = FileOps()
    file_path = os.getcwd()+"/tests/"
    file_obj.write_file(file_path+"title.txt", wd.get_title())
    assert wd.get_title() == 'Swag Labs', "Error in Title"

# @pytest.mark.login
# def test_add_product_in_cart():
#     global global_driver
#     wd1 = ProductPage(global_driver)
#     # wd1.click_product_name()
#     wd1.click_multiple_add_to_cart_button(3)
#     # breakpoint()



