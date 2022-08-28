import time
from locators import *

from selenium.common.exceptions import NoSuchElementException

class MainPage:
    url = "https://habr.com"

    def __init__(self, webdriver):
        self.__webdriver = webdriver

    def open(self):
        self.__webdriver.get(self.url)

    @property
    def search_icon(self):
        return self.__webdriver.find_element(*search_icon_locator)

    def click_search(self):
        self.search_icon.click()
        time.sleep(2)

        return SearchResultsPage(self.__webdriver)

class SearchResultsPage:
    url = "https://habr.com/ru/search"

    def __init__(self, webdriver):
        self.__webdriver = webdriver

    @property
    def search_input(self):
        return self.__webdriver.find_element(*search_input_locator)

    @property
    def search_button(self):
        return self.__webdriver.find_element(*search_button_locator)


    def search(self, search_text):
        self.search_input.send_keys(text_to_search)
        self.search_button.click()

        time.sleep(2)


    def count_pages_number(self):
        last_page_number = self.__webdriver.find_element(*last_page_locator)
        element_text = last_page_number.text
        print(f'number of pages is {element_text}')
        time.sleep(1)

    def go_to_last_page(self):
        last_page = self.__webdriver.find_element(*last_page_locator)
        last_page.click()
        time.sleep(6)

    def count_articles_number(self):
        articles = self.__webdriver.find_elements(*article_locator)
        print(f'number of articles is {len(articles)}')
        time.sleep(1)

    def check_empty_page_text(self):
        empty_results = self.__webdriver.find_element(*empty_res_locator)
        print(f'Text on page: {empty_results.text}')
        time.sleep(1)
