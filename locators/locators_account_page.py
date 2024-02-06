from selenium.webdriver.common.by import By


class LocatorsAccountPage:
    BALANCE = By.CSS_SELECTOR, 'div[ng-hide="noAccount"] > .ng-binding:nth-child(2)'
    DEPOSIT_INPUT = By.CSS_SELECTOR, 'form[ng-submit="deposit()"] input[type="number"]'
    WITHDRAWL_INPUT = By.CSS_SELECTOR, 'form[ng-submit="withdrawl()"] input[type="number"]'
    DEPOSIT_BUTTON = By.CSS_SELECTOR, 'button[ng-click="deposit()"]'
    WITHDRAWL_BUTTON = By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]'
    TRANSACTIONS_BUTTON = By.CSS_SELECTOR, 'button[ng-click="transactions()"]'
    SUBMIT_BUTTON = By.CSS_SELECTOR, 'button[type="submit"]'

    NOTIFICATION_SUCCESS = By.CLASS_NAME, 'error'
