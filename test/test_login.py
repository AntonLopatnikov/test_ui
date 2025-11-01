from ..pages.pages_login import PagesLogin




def test_login(driver):
    login_page = PagesLogin(driver)
    login_page.open_page()
    login_page.fill_login_form("hgfhgfhgfhghf.com")
    login_page.error_test('некорректный формат логина')


