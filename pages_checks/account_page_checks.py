from pages.base_page import BasePage
from locators.locators_account_page import LocatorsAccountPage


class AccountPageChecks(BasePage):
    def check_balance(self, expected_balance: str):
        actual_balance = self.find_element(LocatorsAccountPage.BALANCE).text
        assert actual_balance == expected_balance, (f'Ожидаемый баланс {expected_balance} '
                                                    f'не созвпадает с текущим {actual_balance}')

    def check_notification(self, deposit: bool):
        text = self.find_element(LocatorsAccountPage.NOTIFICATION_SUCCESS).text
        if deposit:
            assert text == 'Deposit Successful'
        else:
            assert text == 'Transaction successful'
