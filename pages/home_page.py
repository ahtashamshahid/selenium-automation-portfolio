from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):

    # ---------- INIT ----------
    def __init__(self, driver):
        super().__init__(driver)

    # ---------- UI Validation ----------
    def is_welcome_title_visible(self):
        return self.is_visible(HomeLocators.TITLE_WELCOME)

    def is_sub_title_visible(self):
        return self.is_visible(HomeLocators.TITLE_SUB)
    
    def get_welcome_title_text(self):
        return self.get_text(HomeLocators.TITLE_WELCOME)

    def get_subtitle_text(self):
        return self.get_text(HomeLocators.TITLE_SUB)
    
    def get_paragraph_text(self):
        return self.get_text(HomeLocators.TXT_MAIN_PARAGRAPH)

    def is_main_image_visible(self):
        return self.is_visible(HomeLocators.IMG_MAIN)
    
    def get_login_button_text(self):
        return self.get_text(HomeLocators.BTN_LOGIN)
    
    def get_register_button_text(self):
        return self.get_text(HomeLocators.BTN_REGISTER)
    
    def get_forgot_password_text(self):
        return self.get_text(HomeLocators.LINK_FORGOT_PASSWORD)

    # ---------- Functional Validation ----------
    def load(self):
        self.go_to(HomeLocators.HOME_PAGE_URL)
    
    def click_login(self):
        self.click(HomeLocators.BTN_LOGIN)

    def click_register(self):
        self.click(HomeLocators.BTN_REGISTER)

    def click_google_login(self):
        self.click(HomeLocators.LINK_GOOGLE_LOGIN)

    def click_forgot_password(self):
        self.click(HomeLocators.LINK_FORGOT_PASSWORD)

    # -------------------------
    # STYLE METHODS
    # -------------------------
    def get_element_class(self, locator):
        return self.find(locator).get_attribute("class")

    def get_css(self, locator, property_name):
        return self.find(locator).value_of_css_property(property_name)

