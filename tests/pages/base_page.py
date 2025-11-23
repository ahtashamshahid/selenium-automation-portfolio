from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    # -------------------------
    # Basic Element Operations
    # -------------------------
    def click(self, locator):
        try:
            element = self.wait.wait_until_clickable(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except:
            # fallback to JS click
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text, clear_first=True):
        element = self.wait_until_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_attribute(self, locator, attribute_name):
        element = self.wait_until_visible(locator)
        return element.get_attribute(attribute_name)

    # -------------------------
    # Wait Helpers
    # -------------------------
    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # -------------------------
    # Element existence checks
    # -------------------------
    def is_visible(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_present(self, locator):
        try:
            self.wait_until_present(locator)
            return True
        except TimeoutException:
            return False

    # -------------------------
    # JavaScript Helpers
    # -------------------------
    def js_click(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_type(self, locator, value):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    # -------------------------
    # Page Navigation
    # -------------------------
    def go_to(self, url):
        self.driver.get(url)

    # -------------------------
    # Action Chains (Hover, etc)
    # -------------------------
    def hover(self, locator):
        element = self.wait_until_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # -------------------------
    # Alerts
    # -------------------------
    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    # -------------------------
    # Multiple Elements
    # -------------------------
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def count_elements(self, locator):
        return len(self.get_elements(locator))

    # -------------------------
    # Screenshot Support
    # -------------------------
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
