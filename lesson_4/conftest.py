import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

browser = testdata["browser"]
url = testdata['url']
un = testdata['username']
pw = testdata['password']


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def right_word():
    return "молоко"


@pytest.fixture()
def wrong_word():
    return "малако"


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username': un, 'password': pw})
    token = {}
    if 'token' in obj_data.json():
        token = obj_data.json()['token']
    else:
        print(f'my_token = {obj_data.json()["error"]}')
    return token