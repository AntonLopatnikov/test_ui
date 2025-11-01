from selenium.webdriver.remote.webdriver import WebDriver

class BasePages:

    base_url = "https://www.ivi.ru"
    this_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
            if self.this_url:
                self.driver.get(f'{self.base_url}{self.this_url}')
            else:
                self.driver.get(self.base_url)


