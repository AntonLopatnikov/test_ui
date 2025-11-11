import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")                    # Без GUI
    options.add_argument("--no-sandbox")                 # Для CI
    options.add_argument("--disable-dev-shm-usage")     # Избежание проблем с памятью
    options.add_argument("--disable-gpu")               # Отключить GPU
    options.add_argument("--remote-debugging-pipe")    # Альтернатива удалённой отладке
    options.add_argument("--disable-features=VizDisplayCompositor")  # Для стабильности в headless

    # Явный путь к Chrome (если установлен через apt)
    options.binary_location = "/usr/bin/google-chrome"


    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
