from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import pytest
import os

@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=GpuProcessSupport")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--start-maximized")

    service = Service(
        ChromeDriverManager().install(),
        log_path="NUL"     # Stop Chrome writing logs to console
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    request.cls.driver = driver
    yield driver
    driver.quit()


# ---------- Fixture for Home Page ----------

@pytest.fixture(scope="class")
def home_page_ui(request):
    driver = request.cls.driver      # <-- driver now exists because we use "driver" fixture on class
    page = HomePage(driver)
    page.load()
    request.cls.home_page = page     # attach page to class
    return page

@pytest.fixture()
def home_page_functional(driver):
    page = HomePage(driver)
    page.load() 
    return page

# ---------- Fixture for Login Page ----------
@pytest.fixture(scope="class")
def login_page(driver):
    page = LoginPage(driver)
    return page

# ---------- Fixture for Register Page ----------
@pytest.fixture(scope="class")
def register_page(driver):
    page = RegisterPage(driver)
    return page

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

