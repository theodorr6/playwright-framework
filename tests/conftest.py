import pytest

from POMs.modals.categories import CategoriesModal
from POMs.pages.product_list_page import ComponentsPage



@pytest.fixture()
def components_page(browser_page):
    """ComponentsPage fixture"""
    return ComponentsPage(browser_page)

@pytest.fixture()
def categories_modal(browser_page):
    """HomePage fixture"""
    return CategoriesModal(browser_page)

@pytest.fixture()
def select_number_items_per_page(components_page):
    """Select the number of items to be shown per page"""
    def _select_items_per_page(category):
        max_items = components_page.get_total_items(category)
        components_page.open_show_per_page_dropdown()
        components_page.select_items_per_page(max_items)
        return components_page
    return _select_items_per_page

@pytest.fixture()
def _sort_products_descendant_price(components_page):
    """Sort products by highest to lowest price and return the page"""
    components_page.open_sort_by_dropdown()
    components_page.select_high_to_low()

@pytest.fixture()
def go_to_category(categories_modal):
    """Go to specified product category"""
    def _select_product_category(category):
        categories_modal.click_category(category)
    return _select_product_category