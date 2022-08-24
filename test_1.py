from page import *

def test_basic_search(driver):
    page = MainPage(driver)
    page.open()

    click_search_form(driver)
    type_text(driver, 'QA')
    click_search_button(driver)
    count_articles_number(driver)
    count_pages_number(driver)
