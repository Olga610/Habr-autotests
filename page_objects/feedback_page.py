from locators.locators import *
from page_objects.base_page import HabrBase


class FeedbackPage(HabrBase):
    url = 'https://habr.com/ru/feedback/'

    @property
    def submit_button(self):
        return self.webdriver.find_element(*submit_button)

    @property
    def email_error_message(self):
        return self.webdriver.find_element(*email_error)

    @property
    def message_error_message(self):
        return self.webdriver.find_element(*message_error)

    @property
    def personal_agreement_error_message(self):
        return self.webdriver.find_element(*agreement_error)
    