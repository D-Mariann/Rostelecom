from pages.base_page import WebPage
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
        self.requests = requests
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


    username = WebElement(*AuthLocators.INPUT_USERNAME)

    password = WebElement(*AuthLocators.INPUT_PASSWORD)

    btn = WebElement(*AuthLocators.BTN_LOGIN)

