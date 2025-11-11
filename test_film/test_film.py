from ..pages.page_film import PageFilm
from time import sleep
import pytest

@pytest.mark.regression
def test_film(driver):
    film_page = PageFilm(driver)
    film_page.open_page()
    film_page.check_text_header('Фильмы смотреть онлайн')