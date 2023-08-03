from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
from generator import StringForTest
from settings import *
import time
import pytest

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_negative_auth_page.py

fix = StringForTest()

@pytest.mark.parametrize('incorrect_phone'
        , [fix.generate_string(255), fix.generate_string(1001), fix.russian_chars(), fix.russian_chars().upper(),
           fix.chinese_chars(), fix.special_chars(), fix.generate_num(11), fix.generate_num(10), ' ']
        , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials',
                '11 digits', '10 digits', 'spase'])
@pytest.mark.parametrize('incorrect_password'
        , [fix.generate_string(255), fix.generate_string(1001), fix.russian_chars(), fix.russian_chars().upper(),
           fix.chinese_chars(), fix.special_chars(), fix.generate_num(11), fix.generate_num(10), ' ']
        , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials',
               '11 digits', '10 digits', 'spase'])
def test_negative_authorisation_with_incorrect_phone(web_browser, incorrect_phone, incorrect_password):
    """Проверка, что нельзя войти в ЛК с некорректными данными."""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.username.send_keys(incorrect_phone)
    page.password.send_keys(incorrect_password)
    page.btn_login.click()
    page.wait_page_loaded()


    assert page.get_relative_link() != '/account_b2c/page'


@pytest.mark.parametrize('phone'
        , [valid_phone, fix.generate_num(10) ]
        , ids=[' valid_phone','10 digits' ])
@pytest.mark.parametrize('password'
    , [ valid_password, 'qwerty'
   ]
    , ids=[ valid_password, 'qwerty'
   ])
@pytest.mark.parametrize('incorrect_captcha'
    , [ fix.generate_num(5), fix.generate_num(8)
   ]
    , ids=[ 'incorrect_captcha', 'incorrect_captcha'
   ])
def test_negative_authorisation_with_incorrect_phone(web_browser, phone, password,incorrect_captcha):
    """Проверка, что нельзя войти в ЛК с некорректной капчей."""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.username.send_keys(phone)
    page.password.send_keys(password)
    page.captcha.send_keys(incorrect_captcha)
    page.btn_login.click()
    page.wait_page_loaded()

    assert page.get_relative_link() != '/account_b2c/page'



@pytest.mark.parametrize('incorrect_phone'
    , [fix.xss_application_html(), fix.application_svg(), fix.xss_application_js(),
        fix.sql_application_js(), fix.payload(), fix.script()
       ]
    , ids=[
        'xss_application_html', 'application_svg', 'xss_application_js', 'sql_application_js', 'Payload', 'script'
    ])
@pytest.mark.parametrize('incorrect_password'
    , [fix.xss_application_html(), fix.application_svg(), fix.xss_application_js(),
        fix.sql_application_js(), fix.payload(), fix.script()
       ]
    , ids=[
        'xss_application_html', 'application_svg', 'xss_application_js', 'sql_application_js', 'Payload', 'script'
     ])
def test_negative_authorisation_code_injection(web_browser, incorrect_phone, incorrect_password):
    """Проверка, что поля ввода устойчивы к инъекциям кода"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.username.send_keys(incorrect_phone)
    page.password.send_keys(incorrect_password)
    page.btn_login.click()
    page.wait_page_loaded()
    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/login'
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate'
    assert page.get_relative_link() != '/account_b2c/page'



@pytest.mark.parametrize('valid_username'
    , [valid_email, valid_phone
       ],
    ids=[
        valid_email, valid_phone
    ])
@pytest.mark.parametrize('incorrect_password'
, [fix.generate_string(255), fix.generate_string(1001), fix.russian_chars(), fix.russian_chars().upper(),
    fix.chinese_chars(), fix.special_chars(), fix.generate_num(11), fix.generate_num(10), ' ', '123456',
   '123456789', 'qwerty', '12345', 'password', '12345678', 'qwerty123', '1q2w3e', '111111', '1234567890',
   'qwertyuiop', 'iloveyou', 'Aa123456', 'P@ssw0rd'
   ])
def test_authorisation(web_browser,valid_username, incorrect_password):
    """Проверка, что невозможно войти в сущестующий аккаунт с некорректным паролем"""

    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.username.send_keys(valid_username)
    page.password.send_keys(incorrect_password)
    page.btn_login.click()
    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page'



@pytest.mark.parametrize('captcha'
    , [fix.xss_application_html(), fix.application_svg(), fix.xss_application_js(),
        fix.sql_application_js(), fix.payload(), fix.script()
       ]
    , ids=[
        'xss_application_html', 'application_svg', 'xss_application_js', 'sql_application_js',
        'Payload', 'application script'
     ])
def test_authorisation(web_browser, captcha):
    """Проверка, что поле капчи устойчиво к инъекциям кода"""


    page = AuthPage(web_browser)
    page.wait_page_loaded()

    page.username.send_keys(valid_email)
    page.password.send_keys(valid_password)
    assert page.captcha.find()
    page.captcha.send_keys(captcha)
    page.btn_login.click()

    time.sleep(5)

    assert page.get_relative_link() != '/account_b2c/page'





# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_negative_auth_page.py
