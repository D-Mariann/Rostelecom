from pages.base_page import WebPage
from pages.objects import AuthLocators
from pages.elements import WebElement
import time,os

class AuthPage(WebElement):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.INPUT_USERNAME)
        self.passw = driver.find_element(*AuthLocators.INPUT_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.BTN_LOGIN)
        time.sleep(3)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()


