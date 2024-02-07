from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser, url: str):
        self.driver = browser
        self.url = url

    def goto(self, url: str = None):
        url = url or self.url
        self.driver.get(url)

    def find_element(self, element_locator: dict):
        return self.driver.find_element(element_locator['By'], element_locator['selector'])

    def find_elements(self, elements_locators: dict):
        return self.driver.find_elements(elements_locators['By'], elements_locators['selector'])

    def click(self, button_locator: dict):
        button = self.find_element(button_locator)
        button.click()

    def select_option(self, select_locator: dict, option: str):
        select_element = self.find_element(select_locator)
        select = Select(select_element)
        select.select_by_visible_text(option)

    def fill_in_field(self, field_locator: dict, value: str):
        field = self.find_element(field_locator)
        field.clear()
        field.send_keys(value)
