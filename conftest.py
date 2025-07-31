import pytest
from playwright.sync_api import sync_playwright, Browser, Page

@pytest.fixture(scope="session")
def browser_setup():
    """Setup browser instance for the entire test session"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=500
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser_setup: Browser):
    """Create a new page for each test"""
    context = browser_setup.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return "https://ecommerce-playground.lambdatest.io/"
