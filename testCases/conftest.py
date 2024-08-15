from selenium import webdriver
import pytest
headless_option =webdriver.ChromeOptions()
headless_option.add_argument("headless")

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=headless_option)
    return driver
