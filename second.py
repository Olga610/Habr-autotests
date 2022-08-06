import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

# settings
driver = webdriver.WebDriver(executable_path="chromedriver.exe")
driver.get("https://habr.com")
time.sleep(2)

# поиск
search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
search_button = driver.find_element(*search_button_locator)
search_button.click()
time.sleep(2)

# ввод текста
search_input_locator = By.CSS_SELECTOR, 'input.tm-input-text-decorated__input'
search_input = driver.find_element(*search_input_locator)
text_to_search = 'asdfgfdsa'
search_input.send_keys(text_to_search)
time.sleep(2)

# нажатие на иконку поиска
search_icon_locator = By.CLASS_NAME, 'tm-search__icon'
search_icon = driver.find_element(*search_icon_locator)
search_icon.click()
time.sleep(2)

# кол-во записей
article_locator = By.TAG_NAME, 'article'
articles = driver.find_elements(*article_locator)
print(f'number of articles is {len(articles)}')
time.sleep(1)

# проверяем текст, когда поиск не дал результатов
empty_res_locator = By.XPATH, '(//*[@data-test-id="empty-placeholder-text"])'
empty_results = driver.find_element(*empty_res_locator)
print(f'Text on page: {empty_results.text}')
time.sleep(1)

driver.quit()
