from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': '[ng-click="customer()"]',
    }
    CUSTOMER_NAME = {
        'By': By.CLASS_NAME,
        'selector': 'fontBig',
    }
    CUSTOMER_SELECT_MENU = {
        'By': By.ID,
        'selector': 'userSelect',
    }
    LOGIN_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': 'button[type="submit"]',
    }
