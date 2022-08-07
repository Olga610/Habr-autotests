from first_try import *


def test_empty_search(driver):
    click_search_form(driver)

    type_text(driver, 'asdfgfdsa')

    click_search_button(driver)

    count_articles_number(driver)

    check_empty_page_text(driver)


def check_empty_page_text(driver):
    empty_res_locator = By.XPATH, '(//*[@data-test-id="empty-placeholder-text"])'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')
    time.sleep(1)

if __name__ == '__main__':
    driver_object = setup()

    try:
        test_empty_search(driver_object)
    except NoSuchElementException as error:
        print('Test failed, {error}')

    tear_down(driver_object)
