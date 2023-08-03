from pages.footer_page import *
import time

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_elements_footer.py




def test_window_cookies(web_browser):
    """Проверка, что при нажатии на гипертекст "Cookies"  в футере страницы,
        открывается окошко с описанием значения и работы куки."""
    page = FooterPage(web_browser)
    page.footer_cookies.scroll_to_element()
    page.footer_cookies.click()
    time.sleep(2)
    assert page.window_cookies.is_visible()


def test_btn_privacy_policy(web_browser):
    """Проверка, что при нажатии на гипертекст " Политикой конфиденциальности"  в футере страницы,
        открывается страница с документацией пользовательского соглашения."""
    page = FooterPage(web_browser)
    page.privacy_policy.scroll_to_element()
    page.privacy_policy.click()
    page.window_handler()
    time.sleep(2)
    page_url = page.get_current_url()
    document_url = 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    assert page_url == document_url


def test_btn_user_agreement(web_browser):
    """Проверка, что при нажатии на гипертекст "Пользовательским соглашением" в футере страницы,
        открывается страница с документацией пользовательского соглашения."""
    page = FooterPage(web_browser)
    page.user_agreement.scroll_to_element()
    page.user_agreement.click()
    page.window_handler()
    time.sleep(2)
    page_url = page.get_current_url()
    document_url = 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    assert page_url == document_url

# pytest --driver Chrome --driver-path \driver\chromedriver.exe tests\test_elements_footer.py
