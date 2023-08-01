from selenium.webdriver.common.by import By

class AuthLocators:
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_MAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')
    # Поле ввода логина
    INPUT_USERNAME = (By.ID, 'username')
    # Поле ввода пароля
    INPUT_PASSWORD = (By.ID, 'password')
    # Кнопка маски пароля
    PASSWORD_MASK = (By.CSS_SELECTOR, 'div.rt-input__action>svg>path')
    # Кнопка "запомнить меня"
    CHECKBOX = (By.CLASS_NAME, 'rt-checkbox__label')
    # Забыл пароль
    BTN_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    # Кнопка "войти"
    BTN_LOGIN = (By.ID, 'kc-login')
    # Войти через соцсети
    ICON_VK = (By.ID, 'oidc_vk')
    ICON_OK = (By.ID, 'oidc_ok')
    ICON_MAIL = (By.ID, 'oidc_mail')
    ICON_YA = (By.ID, 'oidc_ya')
    # Кнопка "Зарегистрироваться"
    BTN_REGISTER = (By.ID, 'kc-register')
    # Пользовательское соглашение
    BTN_USER_AGREEMENT = (By.CSS_SELECTOR, 'div.auth-policy>a')

class NewUserLocators:
        # Поле ввода имя
    INPUT_NAME = (By.NAME, 'firstName')
        # Поле ввода фамилия
    INPUT_SURNAME = (By.NAME,'lastName')
        # Поле ввода Регион
    INPUT_REGION = (By.CSS_SELECTOR,'//div[@class="rt-select rt-select--search register-form__dropdown"]/div/div/input')
        # Кнопка выпадающего списка Регион
    BTN_REGION = (By.CSS_SELECTOR, '//*[@class="rt-base-icon rt-base-icon--fill-path rt-select__arrow"]')
    # меняется на (By.CSS_SELECTOR, '//*[@class="rt-base-icon rt-base-icon--fill-path rt-select__arrow rt-select__arrow--rotate"]')
        #Поле ввода email или мобильный телефон
    INPUT_NEW_USERNAME = (By.ID, 'address')
        # Поле ввода пароля
    INPUT_NEW_PASSWORD = (By.XPATH,'//input[@id="password" and @type="password"]') # type="text" без маски, type="password" с маской
    INPUT_NEW_PASSWORD_MASK = (By.XPATH,'//input[@id="password" and @type="text"]')
        # Поле ввода повторить пароль
    INPUT_PASSWORD_CONFIRMATION = (By.XPATH,'//input[@id="password-confirm" and @type="password"]') # type="text" без маски, type="password" с маской
    INPUT_PASSWORD_CONFIRMATION_MASK = (By.XPATH,'//input[@id="password-confirm" and @type="text"]')
        # Кнопка зарегистрироваться
    BTN_REGISTER = (By.NAME,'register')
        # Маска пароля
    PASSW_MASK = (By.XPATH, '//form/div[4]/div[1]/div/div[2]/svg/path')
        # Маска подтверждения пароля
    CONF_PASSW_MASK = (By.XPATH, '//form/div[4]/div[2]/div/div[2]/svg/path')
        # Предупреждение
    WARNING = (By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')
        # Предупреждение имя
    WARNING_NAME = (By.XPATH, '//form/div[1]/div[1]/span')
        # Предупреждение фамилия
    WARNING_SURNAME = (By.XPATH, '//form/div[1]/div[2]/span')
        # Предупреждение юзернейм
    WARNING_USERNAME = (By.XPATH, '//form/div[3]/div/span')
        # Предупреждение
    WARNING_NEW_PASSWORD = (By.XPATH, '//form/div[4]/div[1]/span')
        # Предупреждение подтверждения пароля
    WARNING_PASSWORD_CONFIRMATION = (By.XPATH, '//form/div[4]/div[2]/span')
        # Пользовательское соглашение
    BTN_USER_AGREEMENT = (By.CSS_SELECTOR, 'div.auth-policy>a')

class FooterLocators:
    FOOTER_COOKIES = (By.CLASS_NAME, 'rt-footer-left__item-accent'[0])
    PRIVACY_POLICY = (By.CLASS_NAME, 'rt-footer-left__item-accent'[1])
    USER_AGREEMENT = (By.CLASS_NAME, 'rt-footer-left__item-accent'[2])
    NUM_SUPPORT_SERVICE = (By.CLASS_NAME, 'rt-footer-right__support-phone')

#ссылки
# https://lk.rt.ru/ - авторизация по коду
# https://my.rt.ru/ - авторизация без лицевого счета и кнопка "войти по временному коду"
# https://start.rt.ru  - управление своими счетами
# https://lk.smarthome.rt.ru/ умный дом авторизация по коду
# https://key.rt.ru/ - ростелеком ключ
