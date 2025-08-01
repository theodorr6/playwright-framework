import logging

from playwright.sync_api import Page, expect

class BasePage:
    """Base page class containing common functionality"""

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url
        self.logger = logging.getLogger()

    def navigate_to(self, url):
        """Navigate to specified URL or base URL"""
        target_url = url if url else self.base_url
        self.page.goto(target_url)
        self.page.wait_for_load_state("networkidle")

    def wait_for_visibility_of_element(self, selector: str, timeout= 5000):
        """Wait for element to be visible"""
        return self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def click_element(self, selector: str, timeout= 5000):
        """Click element for actionability"""
        self.page.locator(selector).click(timeout= timeout)

    def fill_text(self, selector: str, text: str, timeout= 5000):
        """Type text in input fields"""
        self.page.locator(selector).fill(text, timeout= timeout)

    def get_text(self, selector: str, timeout= 5000):
        """Get text for from element"""
        return self.page.locator(selector).text_content(timeout= timeout)
