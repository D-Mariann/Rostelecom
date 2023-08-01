from pages.auth_page import AuthPage
import time
from settings import *

def test_authorisation_with_valid_email(web_browser):

    page = SmokeAuthPage(web_browser)
    page.enter_username(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(10)

    assert page.get_relative_link() == '/account_b2c/page'



def test_authorisation_with_valid_phone(web_browser):

    page = SmokeAuthPage(web_browser)
    page.enter_username(valid_phone)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(10)

    assert page.get_relative_link() == '/account_b2c/page'

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_smoke.py
