from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-testid='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-testid='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-testid='login-submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='logout']")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "[data-testid='alert-message']")
    FORGOT_PASSWORD_LINK = (By.ID, "forgotPasswordLink")

    # --- Reset Password Page Locators ---
    RESET_PAGE_HEADER = (By.XPATH, "//h1[text()='Reset your password']")
    RESET_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-testid='forgot-password-email']")
    RESET_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='forgot-password-submit']")
    RESET_BACK_TO_LOGIN = (By.CSS_SELECTOR, "a[data-testid='login-view']")

    # Error Messages
    EMAIL_ERROR = (By.CSS_SELECTOR, '#email + .invalid-feedback')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '#password + .invalid-feedback')

    ALERT_CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-testid='alert-close']")

    # GOOGLE_BTN = (By.XPATH, "//*[@data-testid='login-with-google']")
    # LINKEDIN_BTN = (By.XPATH, "//*[@data-testid='login-with-linkedin']")
    REGISTER_LINK = (By.XPATH, "//*[@data-testid='register-view']")

     # After login - nav bar locators
    HOME_LINK = (By.CSS_SELECTOR, "a[data-testid='home']")
    PROFILE_LINK = (By.CSS_SELECTOR, "a[data-testid='profile']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='logout']")

    # Actions
    def open_login_page(self, url):
        self.go_to(url)

    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def clear_fields(self):
        self.type(self.EMAIL_INPUT, "", clear_first=True)
        self.type(self.PASSWORD_INPUT, "", clear_first=True)

    def wait_for_login_success(self, timeout=10):
        """
        Waits until all required navigation elements after login are visible.
        Returns True only if Home, Profile, and Logout appear.
        """
        locators = [
            self.HOME_LINK,
            self.PROFILE_LINK,
            self.LOGOUT_BUTTON
        ]

        try:
            for locator in locators:
                self.wait_until_visible(locator)
            return True
        except TimeoutException:
            return False
        
    def get_alert_message(self): 
        if self.is_visible(self.ALERT_MESSAGE): 
            return self.get_text(self.ALERT_MESSAGE) 
        return None

    def get_error_message(self):
        """
        Collect all visible field-level error messages using BasePage methods.
        Return a dictionary like:
        {
            'email': 'Email is required',
            'password': 'Password is required'
        }
        or None if no errors exist.
        """
        error_locators = {
            "email": self.EMAIL_ERROR,
            "password": self.PASSWORD_ERROR,
        }

        errors = {}

        for field, locator in error_locators.items():
            if self.is_visible(locator):
                errors[field] = self.get_text(locator)

        return errors if errors else None

    def refresh_page(self):
        self.driver.refresh()

    def close_alert_message(self):
        if self.is_visible(self.ALERT_MESSAGE):
            self.click(self.ALERT_CLOSE_BUTTON)

    def is_forgot_password_visible(self):
        return self.is_visible(self.FORGOT_PASSWORD_LINK)

    def get_forgot_password_text(self):
        return self.get_text(self.FORGOT_PASSWORD_LINK)

    def get_forgot_password_href(self):
        return self.get_attribute(self.FORGOT_PASSWORD_LINK, "href")

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def is_reset_page_loaded(self):
        """
        Confirms the Reset Password page UI loaded correctly.
        Checks:
        - Header: 'Reset your password'
        - Email field visible
        - Submit button visible
        - Back-to-login button visible
        """

        return (
            self.is_visible(self.RESET_PAGE_HEADER)
            and self.is_visible(self.RESET_EMAIL_INPUT)
            and self.is_visible(self.RESET_SUBMIT_BUTTON)
            and self.is_visible(self.RESET_BACK_TO_LOGIN)
        )

    # def click_google_login(self):
    #     self.click(self.GOOGLE_BTN)

    # def click_linkedin_login(self):
    #     self.click(self.LINKEDIN_BTN)

    # def click_register(self):
    #     self.click(self.REGISTER_LINK)
