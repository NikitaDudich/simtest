from selenium.webdriver.common.by import By


class LocatorsAccountPage:
    BALANCE = {
        'By': By.CSS_SELECTOR,
        'selector': 'div[ng-hide="noAccount"] > .ng-binding:nth-child(2)',
    }
    DEPOSIT_INPUT = {
        'By': By.CSS_SELECTOR,
        'selector': 'form[ng-submit="deposit()"] input[type="number"]',
    }
    WITHDRAWL_INPUT = {
        'By': By.CSS_SELECTOR,
        'selector': 'form[ng-submit="withdrawl()"] input[type="number"]',
    }
    DEPOSIT_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': 'button[ng-click="deposit()"]',
    }
    WITHDRAWL_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': 'button[ng-click="withdrawl()"]',
    }
    SUBMIT_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': 'button[type="submit"]',
    }
    TRANSACTIONS_BUTTON = {
        'By': By.CSS_SELECTOR,
        'selector': 'button[ng-click="transactions()"]',
    }
    NOTIFICATION_SUCCESS = {
        'By': By.CLASS_NAME,
        'selector': 'error',
    }
