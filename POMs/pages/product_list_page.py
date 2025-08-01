from POMs.pages.base_page import BasePage
from enums import CategoriesEnum


class ComponentsPage(BasePage):
    """Components category page modal object"""

    def __init__(self, page):
        super().__init__(page)


    TITLE = "//h1[text()='{}']"
    SORT_BY_DROPDOWN = "//div[@id='entry_212397']"

    def get_page_title(self):
        """Get title of product page"""
        return self.get_text(self.TITLE.format(CategoriesEnum.COMPONENTS))

    def open_sort_by_dropdown(self):
        """Open Sort By dropdown menu"""
        self.click_element(self.SORT_BY_DROPDOWN)