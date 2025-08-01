import pytest
from enums import CategoriesEnum


pytestmark = [pytest.mark.product_sorting]

@pytest.fixture()
def high_to_low_test_setup(page, base_url, components_page, categories_modal, select_number_items_per_page, go_to_category, _sort_products_descendant_price):
    category = CategoriesEnum.COMPONENTS.value

    page.goto(base_url)
    go_to_category(category)
    select_number_items_per_page(category)

    return components_page

def test_high_to_low(high_to_low_test_setup):
    """Verify that products are sorted by highest to lowest price"""
    components_page = high_to_low_test_setup
    assert components_page.are_prices_sorted_high_low()
