import pytest


LOGIN_URL = "https://practice.expandtesting.com/notes/app/login"   # Update if needed
VALID_EMAIL = "ahtashamshahid0@gmail.com"
VALID_PASSWORD = "d34DZxF@86HB8Q"
INVALID_EMAIL = "wrong@example.com"
INVALID_PASSWORD = "WrongPass"

@pytest.mark.usefixtures("driver")
class TestLoginNegative:
    """Negative login tests: open login page once"""

    @pytest.fixture(scope="class", autouse=True)
    def open_login_page_once(self, login_page):
        """Open the login page once for all negative tests"""
        login_page.open_login_page(LOGIN_URL)
        return login_page

    def test_invalid_email(self, login_page):
        login_page.login(INVALID_EMAIL, VALID_PASSWORD)
        assert login_page.get_alert_message() == "Incorrect email address or password"
        login_page.clear_fields()

    def test_invalid_password(self, login_page):
        login_page.login(VALID_EMAIL, INVALID_PASSWORD)
        assert login_page.get_alert_message() == "Incorrect email address or password"
        login_page.clear_fields()

    def test_invalid_email_password(self, login_page):
        login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
        assert login_page.get_alert_message() == "Incorrect email address or password"
        login_page.clear_fields()

    def test_close_error_toast(self, login_page):
        login_page.close_alert_message()
        assert not login_page.is_visible(login_page.ALERT_MESSAGE)

    # @pytest.mark.skip(reason="Not ready yet")
    def test_empty_fields(self, login_page):
        # Submit empty form, No email or password
        login_page.open_login_page(LOGIN_URL)
        login_page.click_login()
        assert login_page.get_error_message() is not None

        # Get error messages
        errors = login_page.get_error_message()
        
        # # Assert that errors are shown
        # assert errors is not None
        assert errors["email"] == "Email address is required"
        assert errors["password"] == "Password is required"

    def test_only_email(self, login_page):
        login_page.open_login_page(LOGIN_URL)
        login_page.enter_email(VALID_EMAIL)
        login_page.click_login()
        assert login_page.get_error_message() is not None
        # Get error messages
        errors = login_page.get_error_message()
        assert errors["password"] == "Password is required"

    def test_only_password(self, login_page):
        login_page.open_login_page(LOGIN_URL)
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_login()
        assert login_page.get_error_message() is not None
        # Get error messages
        errors = login_page.get_error_message()
        assert errors["email"] == "Email address is required"

@pytest.mark.usefixtures("driver")
class TestLoginPositive:
    """Positive login tests: valid credentials"""

    @pytest.fixture(scope="class", autouse=True)
    def login_once(self, login_page):
        """Login once for all positive tests"""
        login_page.open_login_page(LOGIN_URL)
        login_page.login(VALID_EMAIL, VALID_PASSWORD)
        login_page.wait_for_login_success()
        return login_page

    def test_valid_login(self, login_once):
        assert login_once.wait_for_login_success() is True

    def test_forgot_password_link(self, login_page):
        
        # Verify link is visible
        assert login_page.is_forgot_password_visible()

        # Verify link text
        assert login_page.get_forgot_password_text() == "Forgot password"

        # Click link
        login_page.click_forgot_password()

        # Verify URL changed
        assert "forgot-password" in login_page.get_current_url().lower()

        # Verify Reset Password page elements
        assert login_page.is_reset_page_loaded()

        # Verify href attribute
        expected_url = "/notes/app/forgot-password"
        assert expected_url in login_page.get_forgot_password_href()
      

    # def test_register_link(self, login_page):
    #     login_page.open_login_page(LOGIN_URL)
    #     login_page.click_register()
    #     assert "register" in login_page.driver.current_url.lower()

    # # ----------------------------------
    # # Google OAuth Button
    # # ----------------------------------
    # def test_google_login_button(self, login_page):
    #     login_page.open_login_page(LOGIN_URL)
    #     login_page.click_google_login()
    #     assert "google" in login_page.driver.current_url.lower()

    # # ----------------------------------
    # # LinkedIn OAuth Button
    # # ----------------------------------
    # def test_linkedin_login_button(self, login_page):
    #     login_page.open_login_page(LOGIN_URL)
    #     login_page.click_linkedin_login()
    #     assert "linkedin" in login_page.driver.current_url.lower()

    # # ----------------------------------
    # # SQL Injection Attempt
    # # ----------------------------------
    # def test_sql_injection(self, login_page):
    #     login_page.open_login_page(LOGIN_URL)
    #     login_page.login("admin' OR 1=1--", "abc")
    #     assert login_page.get_error_message() is not None

    # # ----------------------------------
    # # XSS Attempt
    # # ----------------------------------
    # def test_xss(self, login_page):
    #     login_page.open_login_page(LOGIN_URL)
    #     login_page.login("<script>alert(1)</script>", "pass")
    #     assert login_page.get_error_message() is not None
