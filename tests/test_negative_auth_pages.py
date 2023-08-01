from pages.auth_page import AuthPage
from settings import *

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.username.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.btn.click()

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_negative_auth_pages.py
