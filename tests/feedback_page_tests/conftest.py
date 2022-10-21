import pytest

from page_objects.feedback_page import FeedbackPage


@pytest.fixture
def feedback_page(driver):
    page = FeedbackPage(driver)

    page.open()

    return page