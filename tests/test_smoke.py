from pages.auth_page import AuthPage
import time
from settings import *

def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.enter_username(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    time.sleep(10)

    #assert page.get_current_url() == 'https://b2c.passport.rt.ru'



