from pages.base_page import WebPage
from pages.elements import WebElement


class RegistrationPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    register = WebElement(id='kc-register')
        # Поле ввода имя
    INPUT_NAME = WebElement(name= 'firstName')
        # Поле ввода фамилия
    INPUT_SURNAME = WebElement(name= 'lastName')
        # Поле ввода Регион
    INPUT_REGION = WebElement(css_selector = '//div[@class="rt-select rt-select--search register-form__dropdown"]/div/div/input')
        # Кнопка выпадающего списка Регион
    BTN_REGION = WebElement(css_selector ='//*[@class="rt-base-icon rt-base-icon--fill-path rt-select__arrow"]')
        # меняется на (By.CSS_SELECTOR, '//*[@class="rt-base-icon rt-base-icon--fill-path rt-select__arrow rt-select__arrow--rotate"]')
        # Поле ввода email или мобильный телефон
    INPUT_NEW_USERNAME = WebElement(id ='address')
        # Поле ввода пароля
    INPUT_NEW_PASSWORD = WebElement(id="password") ## type="text" без маски, type="password" с маской

        # Поле ввода повторить пароль
    INPUT_PASSWORD_CONFIRMATION = WebElement(id="password-confirm")  # type="text" без маски, type="password" с маской

        # Кнопка зарегистрироваться
    BTN_REGISTER = WebElement(name= 'register')
        # Маска пароля
    PASSW_MASK = WebElement(xpath= '//form/div[4]/div[1]/div/div[2]/svg/path')
        # Маска подтверждения пароля
    CONF_PASSW_MASK = WebElement(xpath= '//form/div[4]/div[2]/div/div[2]/svg/path')
        # Предупреждение
    WARNING = WebElement(class_name= 'rt-input-container__meta rt-input-container__meta--error')
        # Предупреждение имя
    WARNING_NAME = WebElement(xpath= '//form/div[1]/div[1]/span')
        # Предупреждение фамилия
    WARNING_SURNAME = WebElement(xpath= '//form/div[1]/div[2]/span')
        # Предупреждение юзернейм
    WARNING_USERNAME = WebElement(xpath= '//form/div[3]/div/span')
        # Предупреждение
    WARNING_NEW_PASSWORD = WebElement(xpath= '//form/div[4]/div[1]/span')
        # Предупреждение подтверждения пароля
    WARNING_PASSWORD_CONFIRMATION = WebElement(xpath='//form/div[4]/div[2]/span')
        # Пользовательское соглашение
    BTN_USER_AGREEMENT = WebElement(css_selector = 'div.auth-policy>a')