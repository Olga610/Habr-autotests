from page import *

def test_pagination_to_last_page(driver):
    page = MainPage(driver)
    page.open()

    click_search_form(driver)
    type_text(driver, 'QA')
    click_search_button(driver)
    go_to_last_page(driver)

    import time
    time.sleep(6)