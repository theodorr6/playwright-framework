import pytest
from enums import CategoriesEnum


pytestmark = [pytest.mark.product_sorting]


@pytest.fixture()
def high_to_low_test_setup(page, base_url, components_page, select_number_items_per_page, go_to_category, _sort_products_descendant_price):
    category = CategoriesEnum.COMPONENTS.value

    components_page.navigate_to(base_url)
    go_to_category(category)
    select_number_items_per_page(category)
    _sort_products_descendant_price()

    return components_page


def test_high_to_low(high_to_low_test_setup):
    """Verify that products are sorted by highest to lowest price"""
    components_page = high_to_low_test_setup
    prices = components_page.get_all_products_prices()
    are_sorted = components_page.are_prices_sorted_high_low()

    assert are_sorted, f"Prices not sorted correctly. First 10 prices: {prices[:10]}"
