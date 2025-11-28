import pytest


@pytest.mark.usefixtures("driver")
class TestHomePage:

    def test_home_page_elements_visible(self, home_page):
        assert home_page.is_welcome_title_visible()
        assert home_page.is_sub_title_visible()
        assert home_page.is_main_image_visible()

    def test_login_button_navigation(self, home_page):
        home_page.click_login()
        assert "/login" in home_page.get_current_url()

    def test_register_button_navigation(self, home_page):
        home_page.click_register()
        assert "/register" in home_page.get_current_url()

    def test_forgot_password_navigation(self, home_page):
        home_page.click_forgot_password()
        assert "/forgot-password" in home_page.get_current_url()

    def test_google_login_navigation(self, home_page):
        home_page.click_google_login()
        assert "google" in home_page.get_current_url().lower()



