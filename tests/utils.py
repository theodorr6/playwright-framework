def are_prices_sorted_high_low(prices):
    """Check if prices are sorted from high to low"""
    return all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1))
