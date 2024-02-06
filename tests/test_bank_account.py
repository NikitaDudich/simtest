import datetime
import pytest
from allure import step
from time import sleep

from locators.locators_login_page import LoginPageLocators
from locators.locators_account_page import LocatorsAccountPage

from utils.classes import Transaction
from utils.utils_functions import attach_csv_to_allure

deposit = Transaction(transaction_type='Credit', date=datetime.datetime.now())
withdrawl = Transaction(transaction_type='Debit', date=datetime.datetime.now())


@pytest.fixture(scope='module')
def fibonacci_number():
    current_date = datetime.datetime.now()
    day = current_date.day + 1

    fib1 = fib2 = 1
    while day > 0:
        fib1, fib2 = fib2, fib1 + fib2
        day -= 1
    return str(fib2)


class TestBankAccount:

    @pytest.fixture(scope='class', autouse=True)
    def attach_csv_to_report(self):
        yield
        attach_csv_to_allure()

    def test_sign_in(self, login_page):
        with step('Нажать на кнопку "Customer Login"'):
            login_page.click(LoginPageLocators.CUSTOMER_LOGIN_BUTTON)

        with step('Авторизоваться за посетителя'):
            customer = 'Harry Potter'  # можно параметризовать
            login_page.select_option(LoginPageLocators.CUSTOMER_SELECT_MENU, customer)
            login_page.click(LoginPageLocators.LOGIN_BUTTON)

        with step('Проверить, что открылся аккаунт нужного посетителя'):
            login_page.check_log_in_succeed(customer)

    def test_deposit_money(self, account_page, fibonacci_number):
        with step('Внести деньги на счёт'):
            account_page.click(LocatorsAccountPage.DEPOSIT_BUTTON)
            account_page.fill_in_field(LocatorsAccountPage.DEPOSIT_INPUT, fibonacci_number)
            account_page.click(LocatorsAccountPage.SUBMIT_BUTTON)
            deposit.date = datetime.datetime.now()
            deposit.amount = fibonacci_number

            # TODO: решить проблему с тем, что список транзакций не успевает подтягиваться без sleep()
            sleep(1)

        with step('Проверить, что деньги внесены'):
            account_page.check_balance(fibonacci_number)
            account_page.check_notification(deposit=True)

    def test_withdrawl_money(self, account_page, fibonacci_number):
        with step('Снять деньги со счёта'):
            account_page.click(LocatorsAccountPage.WITHDRAWL_BUTTON)
            account_page.fill_in_field(LocatorsAccountPage.WITHDRAWL_INPUT, fibonacci_number)
            account_page.click(LocatorsAccountPage.SUBMIT_BUTTON)
            withdrawl.date = datetime.datetime.now()
            withdrawl.amount = fibonacci_number

        with step('Проверить, что деньги сняты'):
            account_page.check_balance('0')
            account_page.check_notification(deposit=False)

            # TODO: решить проблему с тем, что список транзакций не успевает подтягиваться без sleep()
            sleep(3)

    def test_transactions_info(self, transactions_page):
        transactions_page.find_transaction(deposit)
        transactions_page.find_transaction(withdrawl)
