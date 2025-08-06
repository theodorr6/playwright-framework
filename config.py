import os


class BrowserConfig:
    """Browser configuration settings"""
    BROWSER = "chromium"
    IS_CI = os.getenv("CI", "false").lower() == "true"
    HEADLESS = IS_CI
    SLOW_MO = 500

    VIEWPORT_WIDTH = 1920
    VIEWPORT_HEIGHT = 1080
