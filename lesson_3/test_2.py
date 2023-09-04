from lesson_2.testpage import OperationsHelper
import logging

def test_step1(browser):
    logging.info("test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
