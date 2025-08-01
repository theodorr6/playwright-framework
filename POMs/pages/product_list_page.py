import re

from POMs.pages.base_page import BasePage
from enums import CategoriesEnum, SortByEnum
from tests.utils import are_prices_sorted_high_low


class ComponentsPage(BasePage):
    """Components category page modal object"""

    def __init__(self, page):
        super().__init__(page)

    TITLE = "//h1[text()='{}']"
    SORT_BY_DROPDOWN = "//select[@id='input-sort-212403']"
    SHOW_PER_PAGE_DROPDOWN = "//div[@id='entry_212402']//select"
    TOTAL_NUMBER_OF_ITEMS = "//div[@id='entry_212412']//div[contains(text(),'{}')]"
    PRICE_ALL_PRODUCTS_ON_PAGE = "//div[@id='entry_212408']//div[@class='price']//span"

    def get_page_title(self):
        """Get title of product page"""
        return self.get_text(self.TITLE.format(CategoriesEnum.COMPONENTS.value))

    def open_sort_by_dropdown(self, ):
        """Open Sort By dropdown menu"""
        self.click_element(self.SORT_BY_DROPDOWN)

    def open_show_per_page_dropdown(self):
        """Open the show per page dropdown menu"""
        self.click_element(self.SHOW_PER_PAGE_DROPDOWN)

    def select_items_per_page(self, no_of_items):
        """Select the number of items to show per page"""
        if no_of_items not in [15, 25, 50, 75, 100]:
            self.logger.info("Number of items per page can only be 15, 25, 50, 75 or 100!")
        self.page.select_option(self.SHOW_PER_PAGE_DROPDOWN, label=no_of_items)

    def select_high_to_low(self):
        """Sort products by High to Low prices"""
        locator = self.SORT_BY_DROPDOWN.format(SortByEnum.PRICE_HIGH_LOW.value)
        self.page.select_option(locator, label=SortByEnum.PRICE_HIGH_LOW.value)
        self.page.keyboard.press("Escape")

    def get_total_items(self, category):
        """Get total number of items in category"""
        locator_text = self.get_text(self.TOTAL_NUMBER_OF_ITEMS.format(category))
        total_items = re.findall(r'\d+', locator_text)
        return total_items[0]

    def get_all_products_prices(self):
        """Get prices for all products on page"""
        price_elements = self.page.locator(self.PRICE_ALL_PRODUCTS_ON_PAGE).all()
        prices = []

        for element in price_elements:
            price_text = element.text_content()
            cleaned_text = price_text.replace(',', '').replace('$', '')
            price = re.findall(r'\d+\.?\d*', cleaned_text)
            if price:
                prices.append(float(price[0]))

        return prices

    def are_prices_sorted_high_low(self):
        """Check if current page prices are sorted high to low"""
        prices = self.get_all_products_prices()
        return are_prices_sorted_high_low(prices)
