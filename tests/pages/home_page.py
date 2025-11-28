from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    # ---------- INIT ----------
    def __init__(self, driver):
        super().__init__(driver)
    
    # ---------- LOCATORS ----------
    HOME_PAGE_URL = "https://practice.expandtesting.com/notes/app"
    WELCOME_TITLE = (By.XPATH, "//h1[contains(text(),'Welcome to Notes App')]")
    SUB_TITLE = (By.XPATH, "//h3[contains(text(),'A Better Way To Track Your Tasks')]")

    BTN_LOGIN = (By.CSS_SELECTOR, "[data-testid='open-login-view'] a.btn-primary")
    BTN_REGISTER = (By.CSS_SELECTOR, "[data-testid='open-register-view']")
    LINK_GOOGLE = (By.CSS_SELECTOR, "[data-testid='use-google-account']")
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "[data-testid='forgot-password-view']")

    IMAGE = (By.CSS_SELECTOR, "img[alt='Practice ']")

    # ---------- UI Validation ----------
    def is_welcome_title_visible(self):
        return self.is_visible(self.WELCOME_TITLE)
    
    def get_welcome_title_text(self):
        return self.get_text(self.WELCOME_TITLE)

    def is_sub_title_visible(self):
        return self.is_visible(self.SUB_TITLE)
    
    def get_sub_title_text(self):
        return self.get_text(self.SUB_TITLE)

    def is_main_image_visible(self):
        return self.is_visible(self.IMAGE)

    # ---------- Functional Validation ----------
    def load(self):
        self.go_to(self.HOME_PAGE_URL)
    
    def click_login(self):
        self.click(self.BTN_LOGIN)

    def click_register(self):
        self.click(self.BTN_REGISTER)

    def click_google_login(self):
        self.click(self.LINK_GOOGLE)

    def click_forgot_password(self):
        self.click(self.LINK_FORGOT_PASSWORD)

