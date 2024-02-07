from selenium.webdriver.common.by import By


class TransactionsPageLocators:
    TRANSACTIONS = {
        'By': By.CSS_SELECTOR,
        'selector': 'table tbody tr',
    }
    TRANSACTION_DATE = {
        'By': By.CSS_SELECTOR,
        'selector': 'td:nth-child(1)',
    }
    TRANSACTION_AMOUNT = {
        'By': By.CSS_SELECTOR,
        'selector': 'td:nth-child(2)',
    }
    TRANSACTION_TYPE = {
        'By': By.CSS_SELECTOR,
        'selector': 'td:nth-child(3)',
    }