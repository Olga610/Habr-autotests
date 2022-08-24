import time
from locators import *

from selenium.common.exceptions import NoSuchElementException

class MainPage:
    url = "https://habr.com"

    def __init__(self, webdriver):
        self.__webdriver = webdriver

    def open(self):
        self.__webdriver.get(self.url)

def count_pages_number(driver):
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'number of pages is {element_text}')
    time.sleep(1)

def go_to_last_page(driver):
    last_page = driver.find_element(*last_page_locator)
    last_page.click()
    time.sleep(6)

def count_articles_number(driver):
    articles = driver.find_elements(*article_locator)
    print(f'number of articles is {len(articles)}')
    time.sleep(1)


def click_search_button(driver):
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(2)


def type_text(driver, text):
    search_input = driver.find_element(*search_input_locator)
    text_to_search = text
    search_input.send_keys(text_to_search)
    time.sleep(2)


def click_search_form(driver):
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(2)

def check_empty_page_text(driver):
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')
    time.sleep(1)
