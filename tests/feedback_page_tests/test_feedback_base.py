from page_objects.feedback_page import FeedbackPage

def test_errors_on_empty_fields(feedback_page):
    page: FeedbackPage = feedback_page

    page.submit_button.click()

    assert page.email_error_message.is_displayed()
    assert page.message_error_message.is_displayed()
    assert page.personal_agreement_error_message.is_displayed()



def test_number_of_feedback_subject(feedback_page):
    pass


def test_change_subject(feedback_page):
     pass