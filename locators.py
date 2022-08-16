from selenium.webdriver.common.by import By

last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
article_locator = By.TAG_NAME, 'article'
search_icon_locator = By.CLASS_NAME, 'tm-search__icon'
search_input_locator = By.CSS_SELECTOR, 'input.tm-input-text-decorated__input'
search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'