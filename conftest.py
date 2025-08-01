import pytest
from playwright.sync_api import sync_playwright, Browser
from config import BrowserConfig


@pytest.fixture(scope="session")
def browser_setup():
    """Setup browser instance for the entire test session"""
    with sync_playwright() as playwright:
        if BrowserConfig.BROWSER.lower() == "firefox":
            browser = playwright.firefox.launch(headless=BrowserConfig.HEADLESS, slow_mo=BrowserConfig.SLOW_MO)
        else:
            browser = playwright.chromium.launch(headless=BrowserConfig.HEADLESS, slow_mo=BrowserConfig.SLOW_MO)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_setup: Browser):
    """Create a new page for each test"""
    context = browser_setup.new_context(
        viewport={'width': BrowserConfig.VIEWPORT_WIDTH,
                  'height': BrowserConfig.VIEWPORT_HEIGHT}
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return "https://ecommerce-playground.lambdatest.io/"
