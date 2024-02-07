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
                    TransactionsPageLocators.TRANSACTION_DATE['By'],
                    TransactionsPageLocators.TRANSACTION_DATE['selector']).text,
                'amount': transaction.find_element(
                    TransactionsPageLocators.TRANSACTION_AMOUNT['By'],
                    TransactionsPageLocators.TRANSACTION_AMOUNT['selector']).text,
                'type': transaction.find_element(
                    TransactionsPageLocators.TRANSACTION_TYPE['By'],
                    TransactionsPageLocators.TRANSACTION_TYPE['selector']).text,
                }
            if verify_transaction(actual_transaction, expected_transaction):
                success = True
                break
        if not success:
            raise InterruptedError('Информация о транзакции не найдена')
