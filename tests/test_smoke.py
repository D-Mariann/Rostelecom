from pages.auth_page import SmokeAuthPage, AuthPage
import time
from settings import *

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_smoke.py


def test_authorisation_with_valid_email(web_browser):

    page = SmokeAuthPage(web_browser)
    page.enter_username(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(5)

    assert page.get_relative_link() == '/account_b2c/page'



def test_authorisation_with_valid_phone(web_browser):

    page = SmokeAuthPage(web_browser)
    page.enter_username(valid_phone)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(5)

    assert page.get_relative_link() == '/account_b2c/page'

def test_authorisation_with_valid_email(web_browser):
    """Авторизация по корректным данным почты аккаута"""


    page = AuthPage(web_browser)
    page.wait_page_loaded()

    page.username.send_keys(valid_email)
    page.password.send_keys(valid_password)
    if page.captcha.find():
        page.btn_login.click()
        assert page.captcha_warning.find()
        assert page.get_relative_link() != '/account_b2c/page'
    else:
        page.btn_login.click()
        time.sleep(5)
        assert page.get_relative_link() == '/account_b2c/page'


def test_authorisation_with_valid_email(web_browser):
    """Авторизация по корректным данным номера телефона аккаута"""


    page = AuthPage(web_browser)
    page.wait_page_loaded()

    page.username.send_keys(valid_phone)
    page.password.send_keys(valid_password)
    if page.captcha.find():
        page.btn_login.click()
        # assert page.check_js_errors() == AssertionError
        assert page.captcha_warning.find()
        assert page.get_relative_link() != '/account_b2c/page'
    else:
        page.btn_login.click()
        time.sleep(5)
        assert page.get_relative_link() == '/account_b2c/page'

#
#
#
#

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_smoke.py
