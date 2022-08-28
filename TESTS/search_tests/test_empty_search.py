from page_objects.page import *

def test_empty_search(page):
    page.search('asdfgfdsa')

    assert page.count_articles_number() == 0

def test_empty_search_text(page):
    page.search('asdfgfdsa')

    assert len(page.get_empty_page_text()) > 0
