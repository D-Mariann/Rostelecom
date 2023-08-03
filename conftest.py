import pytest
import allure
import uuid
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.auth_page import AuthPage

# @pytest.fixture
# def add_cookies_to_file():
#     browser = webdriver.Chrome()
#     browser.set_window_size(1400, 1000)
#
#     page = AuthPage(browser)
#     page.email.send_keys('rrraaa@yandex.ru')
#     page.password.send_keys("123321")
#     page.btn.click()
#
#     # Save cookies of the brother after login
#     with open('my_cookies.txt', 'wb') as cookies:
#         pickle.dump(browser.get_cookies(), cookies)


@pytest.fixture
def driver():

    s = Service('\driver\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    # driver.set_window_size(1080, 800)
    driver.maximize_window()
    return driver


@pytest.fixture
def web_browser(request, driver): #передаем сюда каждый тесткейс, вызывается до тесткейса
    browser = driver
    # browser.set_window_size(1400, 1000)

    # Вернуть объект браузера
    yield browser #тут переходим внутрь тесткейса

    # Этот код выполнится после отрабатывания теста:
    if request.node.rep_call.failed:
        # Сделать скриншот, если тест провалится:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Создаем папку screenshots и кладем туда скриншот с генерированным именем:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Для дебагинга, печатаем информацию в консоль
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass # just ignore any errors here


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call): #при каждом упавшем тесткейсе, делается скрин, пишется в консоль логи браузера, url, скрин
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep #сохр эту переменную в статус тесткейса


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    return chrome_options


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
