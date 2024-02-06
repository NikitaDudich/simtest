from selenium.webdriver.common.by import By


class TransactionsPageLocators:
    TRANSACTIONS = By.CSS_SELECTOR, 'table tbody tr'
    TRANSACTION_DATE = By.CSS_SELECTOR, 'td:nth-child(1)'
    TRANSACTION_AMOUNT = By.CSS_SELECTOR, 'td:nth-child(2)'
    TRANSACTION_TYPE = By.CSS_SELECTOR, 'td:nth-child(3)'
