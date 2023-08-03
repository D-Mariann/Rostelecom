from pages.base_page import WebPage
from pages.elements import WebElement



class FooterPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)


    privacy_policy = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[1]')
    user_agreement = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[2]')
    footer_cookies = WebElement(id="cookies-tip-open")
    window_cookies = WebElement(class_name="rt-cookies-tip__desc-container")



