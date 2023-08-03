from generator import *
from pages.auth_page import AuthPage
from generator import StringForTest
from settings import *
import time
import pytest

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_elements_auth_page.py


fix = StringForTest()

@pytest.mark.parametrize('phone'
        , ['89268422684', '79268422684','+79268422684', '9268422684'
           ]
        , ids=['89268422684', '79268422684','+79268422684', '9268422684'
               ])
def test_input_format_phone(web_browser, phone):
    """Проверка единого формата отображения ввода корректного номера телефона."""

    page = AuthPage(web_browser)
    page.username.send_keys(phone)

    def val_phone(phone):
        ph = ['+7']
        if len(phone) == 11:
            ph.append(phone[1:])
        elif len(phone) == 12:
            ph.append(phone[2:])
        else:
            ph.append(phone[0:])
        ph = ''.join(ph)
        return ph

    val_phone = val_phone(phone)
    correct_phone = []
    correct_phone.append(page.username.get_attribute('value'))
    correct_phone = ''.join(correct_phone).replace('-','').replace(' ','')
    assert val_phone == correct_phone

@pytest.mark.parametrize('phone'
        , [fix.generate_num(9), fix.generate_num(8), fix.generate_num(7), fix.generate_num(6),
           fix.generate_num(5), fix.generate_num(4), fix.generate_num(3), fix.generate_num(2),
            fix.generate_num(1)
           ]
        , ids=['9 digits', '8 digits', '7 digits', '6 digits', '5 digits', '4 digits', '3 digits'
               '2 digits', '1 digit'
               ])
def test_warning_format_phone(web_browser, phone):
    """Проверка, что появляется предупреждение при неверном формате введенного телефона."""

    page = AuthPage(web_browser)
    page.username.send_keys(phone)
    page.username.enter_element()
    time.sleep(5)
    page.phone_warning.find()

    assert page.phone_warning.is_visible()


@pytest.mark.parametrize('phone'
         , [valid_phone, '89268422684'
           ]
        , ids=[valid_phone,'89268422684'
                ])
@pytest.mark.parametrize('password'
    , [ valid_password, #'qwerty'
   ]
    , ids=[ valid_password, #'qwerty'
   ])
@pytest.mark.parametrize('incorrect_captcha'
    , [ fix.generate_num(5), fix.generate_num(8)
   ]
    , ids=[ 'incorrect_captcha', 'incorrect_captcha'
   ])
def test_warning_captcha(web_browser, phone, password, incorrect_captcha):
    """Проверка, что появляется предупреждение при неверном вводе капчи."""

    page = AuthPage(web_browser)
    page.username.send_keys(phone)
    page.password.send_keys(password)
    assert page.captcha.find()
    page.captcha.send_keys(incorrect_captcha)
    page.btn_login.click()
    time.sleep(5)

    assert page.captcha_warning.is_visible()


def test_password_mask(web_browser):
    """Проверка, что скрывающая пароль маска в поле для пароля работает."""
    password = 'A56842gf'
    page = AuthPage(web_browser)
    page.password.send_keys(password)
    assert page.password.get_attribute('type') == "password"
    page.password_mask.click()
    assert page.password.get_attribute('type') == "text"


def test_btn_forgot_password(web_browser):
    """Проверка, что при нажатии кнопки "забыл пароль",
    открывается страница восстановления пароля."""

    page = AuthPage(web_browser)
    page.forgot_password.scroll_to_element()
    page.forgot_password.click()
    time.sleep(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'


def test_btn_forgot_password(web_browser):
    """Проверка, что при нажатии кнопки "зарегистрироваться",
    открывается страница регистрации."""

    page = AuthPage(web_browser)
    page.register.scroll_to_element()
    page.register.click()
    time.sleep(2)

    assert page.get_relative_link() == 'auth/realms/b2c/login-actions/registration'


# @pytest.mark.xfail(reason = 'Не происходит перенаправления')
def test_icon_vk(web_browser):
    """Проверка, что при нажатии на иконку "VK",
    открывается страница для входа через соц.сеть ВК."""

    page = AuthPage(web_browser)
    page.icon_VK.scroll_to_element()
    page.icon_VK.click()
    time.sleep(2)
    url = page.get_current_url()
    page_url = get_url_with_path(url)
    vk_url = 'id.vk.com/auth'

    assert page_url == vk_url


# @pytest.mark.xfail(reason = 'Не происходит перенаправления')
def test_icon_ok(web_browser):
    """Проверка, что при нажатии на иконку "ОК",
    открывается страница для входа через соц.сеть "Одноклассники"."""

    page = AuthPage(web_browser)
    page.icon_OK.scroll_to_element()
    page.icon_OK.click()
    time.sleep(2)
    url = page.get_current_url()
    page_url = get_url_with_path(url)
    ok_url = 'connect.ok.ru/dk'

    assert page_url == ok_url


# @pytest.mark.xfail(reason = 'Не происходит перенаправления')
def test_icon_mail(web_browser):
    """Проверка, что при нажатии на иконку "@",
    открывается страница для входа через почту "Мой Мир"."""

    page = AuthPage(web_browser)
    page.icon_MAIL.scroll_to_element()
    page.icon_MAIL.click()
    time.sleep(2)
    url = page.get_current_url()
    page_url = get_url_with_path(url)
    mail_url = 'connect.mail.ru/oauth/authorize'

    assert page_url == mail_url

# @pytest.mark.xfail(reason = 'Не происходит перенаправления')
def test_icon_mail(web_browser):
    """Проверка, что при нажатии на гипертекст "пользовательского соглашения",
    открывается страница с документацией пользовательского соглашения."""

    page = AuthPage(web_browser)
    page.user_agreement.scroll_to_element()
    page.user_agreement.click()
    page.window_handler()
    time.sleep(2)
    page_url = page.get_current_url()
    document_url = 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    assert page_url == document_url


def test_auth_tab_phone(web_browser):
    """Проверка, что при вводе номера телефона -
    таб выбора аутентификаци меняется автоматически на номер телефона."""

    inactive_tab_class = "rt-tab rt-tab--small"
    active_tab_class = "rt-tab rt-tab--small rt-tab--active"

    page = AuthPage(web_browser)
    page.username.send_keys('9268514125')
    page.password.click()
    assert page.tab_phone.get_attribute('class') == active_tab_class
    assert page.tab_mail.get_attribute('class') == inactive_tab_class
    assert page.tab_login.get_attribute('class') == inactive_tab_class
    assert page.tab_LS.get_attribute('class') == inactive_tab_class


def test_auth_tab_mail(web_browser):
    """Проверка, что при вводе почты -
    таб выбора аутентификаци меняется автоматически на почту."""

    inactive_tab_class = "rt-tab rt-tab--small"
    active_tab_class = "rt-tab rt-tab--small rt-tab--active"
    page = AuthPage(web_browser)
    page.username.send_keys('example@mail.ru')
    page.password.click()
    assert page.tab_mail.get_attribute('class') == active_tab_class
    assert page.tab_phone.get_attribute('class') == inactive_tab_class
    assert page.tab_login.get_attribute('class') == inactive_tab_class
    assert page.tab_LS.get_attribute('class') == inactive_tab_class

def test_auth_tab_login(web_browser):
    """Проверка, что при вводе логина -
    таб выбора аутентификаци меняется автоматически на логин."""

    inactive_tab_class = "rt-tab rt-tab--small"
    active_tab_class = "rt-tab rt-tab--small rt-tab--active"
    page = AuthPage(web_browser)
    page.username.send_keys('somelogin')
    page.password.click()
    assert page.tab_login.get_attribute('class') == active_tab_class
    assert page.tab_mail.get_attribute('class') == inactive_tab_class
    assert page.tab_phone.get_attribute('class') == inactive_tab_class
    assert page.tab_LS.get_attribute('class') == inactive_tab_class


def test_auth_tab_LS(web_browser):
    """Проверка, что при вводе номера лицевого счета -
    таб выбора аутентификаци меняется автоматически на лицевой счет."""

    inactive_tab_class = "rt-tab rt-tab--small"
    active_tab_class = "rt-tab rt-tab--small rt-tab--active"

    page = AuthPage(web_browser)
    page.username.send_keys('123456789102')
    page.password.click()

    assert page.tab_LS.get_attribute('class') == active_tab_class
    assert page.tab_mail.get_attribute('class') == inactive_tab_class
    assert page.tab_login.get_attribute('class') == inactive_tab_class
    assert page.tab_phone.get_attribute('class') == inactive_tab_class




# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_elements_auth_page.py