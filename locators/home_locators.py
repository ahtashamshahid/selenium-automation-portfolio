from selenium.webdriver.common.by import By

class HomeLocators:
        
    HOME_PAGE_URL = "https://practice.expandtesting.com/notes/app"

    TITLE_WELCOME = (By.TAG_NAME, "h1")
    TITLE_SUB = (By.TAG_NAME, "h3")
    TXT_MAIN_PARAGRAPH = (By.CSS_SELECTOR, "p.lead")

    BTN_LOGIN = (By.CSS_SELECTOR, "[data-testid='open-login-view'] a.btn-primary")
    BTN_REGISTER = (By.CSS_SELECTOR, "[data-testid='open-register-view']")

    LINK_GOOGLE_LOGIN = (By.CSS_SELECTOR, "[data-testid='use-google-account']")
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "[data-testid='forgot-password-view']")

    IMG_MAIN = (By.CSS_SELECTOR, "img.img-fluid")