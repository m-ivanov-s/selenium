import requests

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
from zeep import Client, Settings
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    wsdl = testdata['wsdl']
    un = testdata['username']
    pw = testdata['password']
    url = testdata['url']
    url1 = testdata['url1']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])

    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")

        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False

        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)

        if not button:
            return False

        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)

        field = self.find_element(locator, time=3)

        if not field:
            return False

        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None

        logging.debug(f"We find text {text} in field {field}")
        return text


# ENTER TEXT

    def enter_login(self, word):
        # logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="logging form")

    def enter_pass(self, word):
        # logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="pass form")

    def enter_title(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word, description="logging_form")

    def enter_description(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], word, description="description form")

    def enter_content(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content form")

    def enter_contact_name(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="contact name form")

    def enter_contact_mail(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_MAIL[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_MAIL)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_MAIL"], word, description="contact mail form")

    def enter_contact_content(self, word):
        # logging.info(f"Send '{word}' to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        # login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word, description="contact content form")

# CLICK

    def click_login_button(self):
        # logging.info("Click loging button")
        # self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_btn(self):
        # logging.info("Click new post button")
        # self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new_post")

    def click_save_btn(self):
        # logging.info("Click save button")
        # self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save")

    def click_contact_send_btn(self):
        # logging.info("Click send contact button")
        # self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND).click()
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND"], description="send")

    def click_contact_link(self):
        # logging.info("Click contact link")
        # self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact_link")

# GET TEXT
    def get_error_text(self):
        # error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        # text = error_field.text
        # logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        # return text
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error label")

    def get_user_text(self):
        # user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        # text = user_field.text
        # logging.info(f"We find text {text} in user field {TestSearchLocators.LOCATOR_HELLO[1]}")
        # return text
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"], description="username")

    def get_res_text(self):
        # user_field = self.find_element(TestSearchLocators.LOCATOR_RES_LBL, time=2)
        # text = user_field.text
        # logging.info(f"We find text {text} in res field {TestSearchLocators.LOCATOR_RES_LBL[1]}")
        # return text
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RES_LBL"], description="result")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

# LESSON 1
    def check_words(self, word):
        box = client.service.checkText(word)
        if box:
            # print(box)
            return box[0]['s']

    def token_auth(token):
        response = requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
        content_var = [item['content'] for item in response.json()['data']]
        return content_var
        # return response.json()['data']
        # return response.json()['data'][0]['id']
