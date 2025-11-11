import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-pipe")
    options.binary_location = "/usr/bin/google-chrome"

    # Автоматически скачать и использовать совместимый ChromeDriver
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().download_and_install(),
        options=options
    )
    yield driver
    driver.quit()

