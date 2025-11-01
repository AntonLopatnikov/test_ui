from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..pages.base_pages import BasePages


class PagesLogin(BasePages):

    def fill_login_form(self,login):
        try:
            exit_banner = self.driver.find_element(By.CSS_SELECTOR, ".nbl-simpleControlButton__caption")
            exit_banner.click()
        except:
            pass

        open_login = self.driver.find_element(By.CSS_SELECTOR, ".headerAvatar__signInContainer")
        open_login.click()
        click_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[type="button"]'))
        )
        click_button.click()
        input_email = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.nbl-input__editbox'))
        )
        input_email.send_keys(login)
        click_button_login = self.driver.find_element(By.CSS_SELECTOR, '[data-test="button_continue"]')
        click_button_login.click()

    def error_test(self,text):
        error_checking = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="chatError__subtitle"]'))
        )
        assert error_checking.text == text




