from POMs.modals.categories import CategoriesModal
from base_page import BasePage

class HomePage(BasePage):
    """Home page object model"""

    def __init__(self, page, base_url):
        super().__init__(page, base_url)


    SELECT_CATEGORY_BUTTON = "//div[contains(@class,'shop-by-category')]"

    def open_category_modal(self):
        """Open Select by category modal"""
        self.click_element(self.SELECT_CATEGORY_BUTTON)
        return CategoriesModal