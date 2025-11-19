from pages.login_page import LoginPage

def test_invalid_login_shows_error(driver):
    page = LoginPage(driver)
    page.open("https://the-internet.herokuapp.com/login")
    page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in page.get_error()
