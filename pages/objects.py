from selenium.webdriver.common.by import By

class AuthLocators:
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_MAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')
    INPUT_USERNAME = (By.ID, 'username')
    INPUT_PASSWORD = (By.ID, 'password')
    PASSWORD_MASK = (By.CSS_SELECTOR, 'div.rt-input__action>svg>path')
    CHECKBOX = (By.CLASS_NAME, 'rt-checkbox__label')
    BTN_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    BTN_LOGIN = (By.ID, 'kc-login')

    ICON_VK = (By.ID, 'oidc_vk')
    ICON_OK = (By.ID, 'oidc_ok')
    ICON_MAIL = (By.ID, 'oidc_mail')
    ICON_YA = (By.ID, 'oidc_ya')
    BTN_REGISTER = (By.ID, 'kc-register')
    BTN_USER_AGREEMENT = (By.CSS_SELECTOR, 'div.auth-policy>a')

class FooterLocators:
    FOOTER_COOKIES = (By.CLASS_NAME, 'rt-footer-left__item-accent'[0])
    PRIVACY_POLICY = (By.CLASS_NAME, 'rt-footer-left__item-accent'[1])
    USER_AGREEMENT = (By.CLASS_NAME, 'rt-footer-left__item-accent'[2])
    NUM_SUPPORT_SERVICE = (By.CLASS_NAME, 'rt-footer-right__support-phone')

