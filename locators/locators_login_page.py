from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = By.CSS_SELECTOR, "[ng-click='customer()']"
    CUSTOMER_NAME = By.CLASS_NAME, "fontBig"
    CUSTOMER_SELECT_MENU = By.ID, "userSelect"
    LOGIN_BUTTON = By.CSS_SELECTOR, "button[type='submit']"
