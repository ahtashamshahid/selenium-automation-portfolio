import pytest
import time
from pages.register_page import RegisterPage

REGISTER_URL = "https://practice.expandtesting.com/notes/app/register"   # Update if needed

ERROR_MESSAGES = {
        "email_invalid": "Email address is invalid",
        "email_required": "Email address is required",
        "name_required": "User name is required",
        "password_required": "Password is required",
        "confirm_password_required": "Confirm Password is required",
        "password_not_matched": "Passwords don't match!",
    }

# ----------------------------------------------
# TEST DATA AS DICTIONARIES
# ----------------------------------------------

valid_test_data = {"name": "John Doe","password": "Password123"}

# -------------------------------------------------------
# UI TEST CASES
# -------------------------------------------------------

@pytest.mark.usefixtures("driver")
class TestRegisterUI:
        
    @pytest.fixture(scope="class", autouse=True)
    def open_register_page_once(self, register_page):
        """Open page once before all UI tests."""
        register_page.go_to(REGISTER_URL)
    
    def test_register_ui_elements_visible(self, register_page):
        """Verify that all UI fields and buttons exist.""" 
        assert register_page.is_visible(RegisterPage.EMAIL)
        assert register_page.is_visible(RegisterPage.NAME)
        assert register_page.is_visible(RegisterPage.PASSWORD)
        assert register_page.is_visible(RegisterPage.CONFIRM_PASSWORD)

# -------------------------------------------------------
# FUNCTIONAL NEGATIVE TESTS CASSES
# -------------------------------------------------------

class TestRegisterNegative:

    def test_registration_with_empty_fields(self, register_page):
        """Verify error messages when nothing is filled and submitted."""
        register_page.go_to(REGISTER_URL)
        register_page.click_register()
        assert register_page.get_error_message() is not None
        errors = register_page.get_error_message()
        assert errors["email"] == ERROR_MESSAGES["email_required"]
        assert errors["name"] == ERROR_MESSAGES["name_required"]
        assert errors["password"] == ERROR_MESSAGES["password_required"]
        assert errors["confirm_password"] == ERROR_MESSAGES["confirm_password_required"]

    def test_registration_invalid_email(self, register_page):
        """Verify invalid email is rejected."""
        register_page.go_to(REGISTER_URL)
        register_page.enter_email("invalid-email")
        register_page.enter_name("Test User")
        register_page.enter_password("Password123")
        register_page.enter_confirm_password("Password123")
        register_page.click_register()
        assert register_page.get_error_message() is not None
        errors = register_page.get_error_message()
        assert errors["email"] == ERROR_MESSAGES["email_invalid"]
        
    def test_registration_password_not_matching(self, register_page):
        """Verify registration fails when passwords do not match."""
        register_page.go_to(REGISTER_URL)
        email = f"user_{int(time.time())}@mail.com"
        register_page.enter_email(email)
        register_page.enter_name("John Doe")
        register_page.enter_password("Password123")
        register_page.enter_confirm_password("differentPassword")
        register_page.click_register()
        assert register_page.get_error_message() is not None
        errors = register_page.get_error_message()
        assert errors["confirm_password"] == ERROR_MESSAGES["password_not_matched"]

# -------------------------------------------------------
# FUNCTIONAL POSITIVE TEST CASSES
# -------------------------------------------------------

class TestRegisterPositive:
    @pytest.mark.skip(reason="Not ready yet")
    def test_successful_user_registration(self, register_page):
        """Verify that a user can register successfully with valid data or with multiple data sets using dictionary-based test data."""
        register_page.go_to(REGISTER_URL)
        email = f"user_{int(time.time())}@mail.com"
        register_page.enter_email(email)
        register_page.enter_name(valid_test_data["name"])
        register_page.enter_password(valid_test_data["password"])
        register_page.enter_confirm_password(valid_test_data["password"])
        register_page.click_register()
        # After successful registration, user should be redirected
        assert register_page.wait_for_registartion_success()

