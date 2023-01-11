from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage


def test_ice_spirit_is_displayed():

    driver = webdriver.Chrome(
        'C:/Users/ssjga/PycharmProjects/pythonTestTraining/venv/Lib/site-packages/selenium/webdriver/chromedriver.exe')

    driver.maximize_window()

    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    # Using map path way
    cards_page = CardsPage(driver)
    assert cards_page.goto().get_card_by_name('Ice Spirit').is_displayed()
    '''assert cards_page.goto().map.ice_spirit_card.is_displayed'''

    '''# Old way
    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    # 3. assert Ice Spirit is displayed
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert ice_spirit_card.is_displayed()'''

def test_ice_spirit_details_displayed():
    driver = webdriver.Chrome(
        'C:/Users/ssjga/PycharmProjects/pythonTestTraining/venv/Lib/site-packages/selenium/webdriver/chromedriver.exe')
    driver.maximize_window()

    driver.get('https://statsroyale.com')

    #Replaced by using Page Map pattern (pm)
    '''#2. go to Cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()'''

    #3. go to Ice Spirit's Details page
    CardsPage(driver).goto().get_card_by_name('Ice Spirit').click()
    #driver.find_element(By.CSS_SELECTOR, "[href*='/Ice+Spirit']").click()  #(pm)


    #4. get the card name, type, arena, and rarity
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    split = details_page.map.card_type.text.split(', ')
    card_type = split[0]
    card_arena = split[1]
    card_rarity = details_page.map.card_rarity.text.split('\n')[1]


    #(mp)
    '''card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text

    split = driver.find_element(By.CSS_SELECTOR, "[class='card__rarity'").text.split(', ')
    card_type = split[0]
    card_arena = split[1]

    #All three of these seem to work
    #card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='common']").text
    #card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='card__count']").text
    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split('\n')[1]'''

    #5. assert they are correct
    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop '
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
