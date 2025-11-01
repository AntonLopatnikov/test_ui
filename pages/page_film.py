from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..pages.base_pages import BasePages


class PageFilm(BasePages):

    this_url = '/movies'

    def check_text_header(self, text):
        header_text = WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[class="headerBarWithSuggestion__title"]'))
        )
        assert header_text.text == text


