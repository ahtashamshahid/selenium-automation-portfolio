import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # headless for CI; remove locally if you want to see browser
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Add a pytest hook to save screenshots on failure. Create conftest.py or add below to it:
# Store screenshots in screenshots/ and upload them as workflow artifacts.

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(path)

