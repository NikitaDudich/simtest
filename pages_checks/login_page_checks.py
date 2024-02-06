from pages.base_page import BasePage
from locators.locators_login_page import LoginPageLocators


class LoginPageChecks(BasePage):
    def check_log_in_succeed(self, expected_owner: str):
        account_owner = self.find_element(LoginPageLocators.CUSTOMER_NAME).text
        assert account_owner == expected_owner, (f'Имя владельца аккаунта {account_owner} '
                                                 f'не совпадает с заданным {expected_owner}')
