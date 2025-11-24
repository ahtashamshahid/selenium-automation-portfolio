from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RegisterPage(BasePage):
    
    # Locators
    EMAIL =  (By.CSS_SELECTOR, "[data-testid='register-email']")
    NAME =  (By.CSS_SELECTOR, "[data-testid='register-name']")
    PASSWORD =  (By.CSS_SELECTOR, "[data-testid='register-password']")
    CONFIRM_PASSWORD =  (By.CSS_SELECTOR, "[data-testid='register-confirm-password']")
    REGISTER_BTN = (By.CSS_SELECTOR, "[data-testid='register-submit']")

    # Error Messages
    EMAIL_ERROR = (By.CSS_SELECTOR, '#email + .invalid-feedback')
    PASSWORD_ERROR = (By.CSS_SELECTOR, '#password + .invalid-feedback')
    NAME_ERROR = (By.CSS_SELECTOR, '#name + .invalid-feedback')
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, '#confirmPassword + .invalid-feedback')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Fill form fields
    def enter_email(self, email):
        self.type(self.EMAIL, email)
    
    def enter_name(self, name):
        self.type(self.NAME, name)
    
    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def enter_confirm_password(self, confirm_password):
        self.type(self.CONFIRM_PASSWORD, confirm_password)

    # Click Register
    def click_register(self):
        self.click(self.REGISTER_BTN)

    # Get errors messages
    def get_error_message(self):
    
        error_locators = {
           "email": self.EMAIL_ERROR,
           "name": self.NAME_ERROR,
           "password": self.PASSWORD_ERROR,
           "confirm_password": self.CONFIRM_PASSWORD_ERROR
        }

        errors = {}

        for field, locator in error_locators.items():
            if self.is_visible(locator):
                errors[field] = self.get_text(locator)
        
        return errors if errors else None
  
    # Check element visible


    