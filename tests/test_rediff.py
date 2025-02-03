from page_objects import rediff_page_path_axes
from page_objects.rediff_page_path_axes import RediffPage


def test_rediff_axes(driver):

    rd = RediffPage(driver)
    rd.open_url("https://money.rediff.com/gainers")
    # rd.select_Indiahomeloan_locator (directly pass the locator without making the function)
    rd.click_Indiahome_loan()
    breakpoint()