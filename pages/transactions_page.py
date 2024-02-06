from pages.base_page import BasePage
from locators.locators_transactions_page import TransactionsPageLocators
from utils.utils_functions import verify_transaction


class TransactionsPage(BasePage):
    def find_transaction(self, expected_transaction):
        success = False
        transactions_list = self.find_elements(TransactionsPageLocators.TRANSACTIONS)
        for transaction in transactions_list:
            actual_transaction = {
                'date': transaction.find_element(
                    TransactionsPageLocators.TRANSACTION_DATE[0],
                    TransactionsPageLocators.TRANSACTION_DATE[1]).text,
                'amount': transaction.find_element(
                    TransactionsPageLocators.TRANSACTION_AMOUNT[0],
                    TransactionsPageLocators.TRANSACTION_AMOUNT[1]).text,
                'type': transaction.find_element(
                    TransactionsPageLocators.TRANSACTION_TYPE[0],
                    TransactionsPageLocators.TRANSACTION_TYPE[1]).text,
                }
            if verify_transaction(actual_transaction, expected_transaction):
                success = True
                break
        if not success:
            raise InterruptedError('Информация о транзакции не найдена')
