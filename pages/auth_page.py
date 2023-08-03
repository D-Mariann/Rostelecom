from pages.base_page import WebPage, BasePage
from pages.objects import AuthLocators
from pages.elements import WebElement
import time,os


class SmokeAuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.INPUT_USERNAME)
        self.password = driver.find_element(*AuthLocators.INPUT_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.BTN_LOGIN)
        time.sleep(3)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()




class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    #Authorization
    username = WebElement(id = 'username')
    password = WebElement(id = 'password')
    captcha = WebElement(id = "captcha")
    btn_login= WebElement(id = 'kc-login')
    password_mask = WebElement(css_selector = 'div.rt-input__action>svg>path') #'rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye rt-input__eye
    checkbox = WebElement(class_name = 'rt-checkbox__label')
    forgot_password = WebElement(id = 'forgot_password')

    #Warning
    captcha_warning = WebElement(id = 'form-error-message')
    phone_warning = WebElement(xpath='//form/div[1]/div[2]/span')

    register = WebElement(id = 'kc-register')

    name_input_phone = WebElement(class_name = 'rt-input__placeholder rt-input__placeholder--top')
    #tab
    tab_phone = WebElement(id = 't-btn-tab-phone')
    tab_mail = WebElement(id = 't-btn-tab-mail')
    tab_login = WebElement(id = 't-btn-tab-login')
    tab_LS = WebElement(id = 't-btn-tab-ls')
    # Войти через соцсети
    icon_VK = WebElement(id = 'oidc_vk')
    icon_OK = WebElement(id = 'oidc_ok')
    icon_MAIL = WebElement(id = 'oidc_mail')
    icon_YA = WebElement(id = 'oidc_ya')

    user_agreement = WebElement(css_selector = 'div.auth-policy>a')


