from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.pages.base.pagebase import PageBase


class CardDetailsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardDetailsPageMap(driver)


class CardDetailsPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    @property
    #web page devs messed-up,so this gives both category and arena.  We'll fix this in the page object
    def card_type(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class='card__rarity'")

    @property
    #Also need to alter this in page object probably
    def card_rarity(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']")

