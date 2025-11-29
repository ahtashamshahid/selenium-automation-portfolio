import pytest
from locators.home_locators import HomeLocators


@pytest.mark.usefixtures("driver", "home_page_ui")
class TestHomePageUI:
    """
    UI tests for validating the Home Page text,
    styles, spacing, and static content.
    """

    # ---------- TEXT VERIFICATION ----------

    def test_welcome_title_text(self):
        """Verify welcome title is correct."""
        assert self.home_page.get_welcome_title_text() == "Welcome to Notes App"

    def test_subtitle_text(self):
        """Verify subtitle text content."""
        assert self.home_page.get_subtitle_text() == "A Better Way To Track Your Tasks"

    def test_paragraph_content(self):
        """Verify main paragraph contains key content."""
        paragraph = self.home_page.get_paragraph_text()
        assert "Stay productive" in paragraph
        assert "Simplify your life" in paragraph


    # ---------- STYLE VERIFICATION ----------

    def test_title_css_classes(self):
        """Verify welcome title CSS class structure."""
        class_name = self.home_page.get_element_class(HomeLocators.TITLE_WELCOME)
        assert "fw-bold" in class_name
        assert "lh-1" in class_name

    def test_subtitle_spacing_class(self):
        """Verify subtitle spacing margin."""
        class_name = self.home_page.get_element_class(HomeLocators.TITLE_SUB)
        assert "mt-3" in class_name


    # ---------- VISUAL ELEMENTS ----------

    def test_main_image_is_visible(self):
        """Verify hero/landing image is visible."""
        assert self.home_page.is_main_image_visible()


    # ---------- LINKS & BUTTON TEXT ----------

    def test_login_button_text(self):
        """Verify Login button label."""
        assert self.home_page.get_login_button_text() == "Login"

    def test_register_button_text(self):
        """Verify Register button label."""
        assert self.home_page.get_register_button_text() == "Create an account"

    def test_forgot_password_link_text(self):
        """Verify Forgot Password link label."""
        assert self.home_page.get_forgot_password_text() == "Forgot your password?"


@pytest.mark.usefixtures("driver")
class TestHomePageFunctional:

    def test_login_button(self, home_page_functional):
        home_page_functional.click_login()
        assert "/login" in home_page_functional.get_current_url()

    def test_register_button_navigation(self, home_page_functional):
        home_page_functional.click_register()
        assert "/register" in home_page_functional.get_current_url()

    def test_forgot_password_navigation(self, home_page_functional):
        home_page_functional.click_forgot_password()
        assert "/forgot-password" in home_page_functional.get_current_url()

    def test_google_login_navigation(self, home_page_functional):
        home_page_functional.click_google_login()
        assert "google" in home_page_functional.get_current_url().lower()



