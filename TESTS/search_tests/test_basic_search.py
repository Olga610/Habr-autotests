from page_objects.page import *

def test_articles_number_on_page(page):
    page.search('selenium')

    assert page.count_articles_number() == 20

def test_pages_number_on_page(page):
    page.search('selenium')

    assert page.count_pages_number() == 50

