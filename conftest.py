import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators_and_testdata import *


@pytest.yield_fixture(autouse=True, scope="class")
def data_bag(request):
    data_bag = {**context_data}
    yield data_bag

@pytest.yield_fixture(autouse=True, scope="session")
def driver(request):
    chrome_options = Options()
#    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
#    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome("driver/chromedriver.exe", options=chrome_options)
    yield driver
    request.addfinalizer(driver.quit)
