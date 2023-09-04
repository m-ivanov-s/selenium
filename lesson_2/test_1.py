# файд больше не используется, т.к. он переписан в файл testpage
import yaml
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])

def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn_selector = """button"""
    btn = site.find_element("css", btn_selector)
    btn.click()

    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    # print(err_label.text)
    assert err_label.text == "401"
#login > div.submit.svelte-uwkxn9 > button > div
test_step1()

#login > div:nth-child(1) > label > span.mdc-text-field__ripple

# css_selector = 'span.mdc-text-field__ripple'
# print(site.get_element_property("css", css_selector, "height"))

# //*[@id="login"]/div[3]/button/div

# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))