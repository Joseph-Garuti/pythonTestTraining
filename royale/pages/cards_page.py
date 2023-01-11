from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.pages.base.pagebase import PageBase


class CardsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver)

    def goto(self):
        self.headernav.goto_cards_page()
        #self.headernav.map.cards_link.click()  #Alternate
        return self

    def get_card_by_name(self, card_name: str) -> WebElement: #REMINDER: card_name: str says that a string should be passed into card_name
        if ' ' in card_name:
            card_name = card_name.replace(' ', '+')
        return self.map.card(card_name)


class CardsPageMap:
    def __init__(self, driver):
        self._driver = driver


    def card(self, card_name) -> WebElement: # -> WebElement tells the IDE that the function should return a WebElement.  This is called an annotation or a type hint
        return self._driver.find_element(By.CSS_SELECTOR, f"[href*='{card_name}']")

