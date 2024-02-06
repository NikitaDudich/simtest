from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser, url: str):
        self.driver = browser
        self.url = url

    def goto(self, url: str = None):
        url = url or self.url
        self.driver.get(url)

    def find_element(self, element_locator):
        return self.driver.find_element(element_locator[0], element_locator[1])

    def find_elements(self, elements_locators):
        return self.driver.find_elements(elements_locators[0], elements_locators[1])

    def click(self, button_locator):
        button = self.find_element(button_locator)
        button.click()

    def select_option(self, select_locator, option: str):
        select_element = self.find_element(select_locator)
        select = Select(select_element)
        select.select_by_visible_text(option)

    def fill_in_field(self, field_locator, value: str):
        field = self.find_element(field_locator)
        field.clear()
        field.send_keys(value)
