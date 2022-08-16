import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def count_pages_number(driver):
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'number of pages is {element_text}')
    time.sleep(1)

def go_to_last_page(driver):
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page = driver.find_element(*last_page_locator)
    last_page.click()
    time.sleep(6)

def count_articles_number(driver):
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'number of articles is {len(articles)}')
    time.sleep(1)


def click_search_button(driver):
    search_icon_locator = By.CLASS_NAME, 'tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)


def type_text(driver, text):
    search_input_locator = By.CSS_SELECTOR, 'input.tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = text
    search_input.send_keys(text_to_search)
    time.sleep(2)


def click_search_form(driver):
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(2)

def check_empty_page_text(driver):
    empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')
    time.sleep(1)
