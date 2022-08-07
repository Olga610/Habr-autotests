import time

import pytest
from selenium.webdriver.chrome import webdriver


def setup():
    print('setup')
    driver = webdriver.WebDriver(executable_path="chromedriver.exe")
    driver.get("https://habr.com")
    time.sleep(2)

    return driver

def tear_down(driver):
    print('tear_down')
    driver.quit()

@pytest.fixture
def driver():
    obj = setup()

    yield obj

    tear_down(obj)
