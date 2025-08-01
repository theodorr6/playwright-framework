from POMs.pages.base_page import BasePage

class CategoriesModal(BasePage):
    """Categories modal object"""

    def __init__(self, page):
        super().__init__(page)

    CATEGORY = "//div[contains(@class,'drawer')]//span[normalize-space(text())='{}']"

    def click_category(self, category):
        """Click on specific category"""
        self.click_element(self.CATEGORY.format(category))
