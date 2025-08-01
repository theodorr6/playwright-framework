import pytest

from POMs.pages.home_page import HomePage
from POMs.pages.product_list_page import ComponentsPage


@pytest.fixture()
def components_page(page):
    """ComponentsPage fixture"""
    return ComponentsPage(page)

@pytest.fixture()
def home_page(page):
    """HomePage fixture"""
    return HomePage(page)


@pytest.fixture()
def select_number_items_per_page(components_page):
    """Select the number of items to be shown per page"""
    def _select_items_per_page(category):
        max_items = components_page.get_total_items(category)
        components_page.open_show_per_page_dropdown()
        components_page.select_items_per_page(max_items)
    return _select_items_per_page

@pytest.fixture()
def _sort_products_descendant_price(components_page):
    """Sort products by highest to lowest price and return the page"""
    def do_sorting():
        components_page.open_sort_by_dropdown()
        components_page.select_high_to_low()
    return do_sorting

@pytest.fixture()
def go_to_category(home_page):
    """Go to specified product category"""
    def _select_product_category(category):
        modal = home_page.open_category_modal()
        modal.click_category(category)
    return _select_product_category