import os
from allure import step, attach, attachment_type
import pytest
from selenium import webdriver

from pages.base_page import BasePage
from pages.transactions_page import TransactionsPage
from pages_checks.login_page_checks import LoginPageChecks
from pages_checks.account_page_checks import AccountPageChecks, LocatorsAccountPage

from utils import urls


def pytest_addoption(parser):
    parser.addoption('--browser-name', action='store', default='chrome',
                     help='Запуск тестов в указанном браузере: chrome / firefox / safari')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=attachment_type.PNG
            )
        except Exception as e:
            print(f'Fail to take screen-shot: {e}')

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    with step('Опеределение браузера для теста'):
        browser_name = request.config.getoption('--browser-name')
        if browser_name.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_name.lower() == 'safari':
            options = webdriver.SafariOptions()

        else:  # chrome
            options = webdriver.ChromeOptions()

        driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options,
        )

        driver.implicitly_wait(5)

        yield driver

        driver.quit()


@pytest.fixture(scope='session')
def base_page(browser):
    page = BasePage(browser, url=urls.BASE_URL)
    page.goto()

    yield page

    page.driver.close()


@pytest.fixture()
def login_page(base_page):
    page = LoginPageChecks(base_page.driver, url=urls.VISITOR_PAGES_URLS['login'])

    yield page


@pytest.fixture()
def account_page(login_page):
    page = AccountPageChecks(login_page.driver, url=urls.VISITOR_PAGES_URLS['account'])

    yield page


@pytest.fixture()
def transactions_page(account_page):
    account_page.click(LocatorsAccountPage.TRANSACTIONS_BUTTON)
    page = TransactionsPage(account_page.driver, url=urls.VISITOR_PAGES_URLS['transactions'])

    yield page
