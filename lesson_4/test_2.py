import time
from testpage import OperationsHelper
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]


def test_step1(browser):
    logging.info("test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("test2 starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_error_text() == f"Hello, {name}"


def test_step3(browser):
    logging.info("test3 starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enetr_description("testdesc")
    testpage.click_save_btn(name)
    time.sleep(2)
    assert testpage.get_res_text() == f"Hello, {name}"


def test_step4(browser):
    logging.info("test4 starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)

    testpage.enter_contact_name("testname")
    testpage.enter_contact_mail("test@test.ru")
    testpage.enter_contact_content("testcontactcontent")
    time.sleep(2)
    testpage.click_contact_send_btn()
    time.sleep(2)

    assert testpage.get_allert() == "Form successfully submitted"


def test_lesson1_1(right_word, wrong_word):
    assert right_word in OperationsHelper.check_words(wrong_word)


def test_lesson1_2(login):
    assert 'content' in OperationsHelper.token_auth(login)
