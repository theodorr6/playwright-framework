from enum import Enum


class CategoriesEnum(Enum):
    """Enum class for all categories"""
    COMPONENTS = "Components"
    LAPTOPS = "Cameras"
    TABLETS = "Software"
    SOFTWARE = "MP3 Players"
    PHONES = "Laptops & Notebooks"
    CAMERAS = "Desktops and Monitors"
    MP3_PLAYERS = "Desktops and Monitors"
    PRINTERS_SCANNERS = "Printers & Scanners"
    MICE_TRACKBALLS = "Mice and Trackballs"
    FASHION_ACCESSORIES = "Fashion and Accessories"
    BEAUTY_SALOON = "Beauty and Saloon"
    AUTOPARTS_ACCESSORIES = "Autoparts and Accessories"
    WASHING_MACHINE = "Washing machine"
    GAMING_CONSOLES = "Gaming consoles"
    AIR_CONDITIONER = "Air conditioner"
    WEB_CAMERAS = "Web Cameras"


class SortByEnum(Enum):
    DEFAULT = "Default"
    BEST_SELLERS = "Best Sellers"
    POPULAR = "Popular"
    NEWEST = "Newest"
    NAME_A_Z = "Name (A - Z)"
    NAME_Z_A = "Name (Z - A)"
    PRICE_LOW_HIGH = "Price (Low > High)"
    PRICE_HIGH_LOW = "Price (High > Low)"
    RATING_HIGHEST = "Rating (Highest)"
    RATING_LOWEST = "Rating (Lowest)"
    MODEL_A_Z = "Model (A - Z)"
    MODEL_Z_A = "Model (Z - A)"
