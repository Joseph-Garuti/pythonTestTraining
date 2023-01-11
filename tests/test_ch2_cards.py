#TODO:
# Close the window if the test fails

# Challenges:
#   1: Assert Lava Golem is displayed
#       1b. Streamline so less code is copied between searches
#
#   2: Rarity search (Done in new file)
#       2a. Uncheck the Common Filter at the top# name='common-cards'
#       2b. Assert that Ice Spirit is not displayed.

from selenium import webdriver
from selenium.webdriver.common.by import By




def test_cards_displayed():
    card_addresses = ["[href*='Ice+Spirit']", "[href*='Lava+Hound']"]
    global driver
    driver = webdriver.Chrome(
        'C:/Users/ssjga/PycharmProjects/pythonTestTraining/venv/Lib/site-packages/selenium/webdriver/chromedriver.exe')

    driver.maximize_window()

    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com')

    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    for card in card_addresses:
        card_name = driver.find_element(By.CSS_SELECTOR, card)
        assert card_name.is_displayed()

    '''common_checkbox = driver.find_element(By.NAME, 'common-cards')
    assert common_checkbox.is_displayed()'''

    '''cards_button = driver.find_element(By.CSS_SELECTOR, "[href='/cards']")
    assert cards_button.is_displayed()'''

    '''test_card_displayed("[href*='Ice+Spirit']")
    test_card_displayed("[href*='Lava+Hound']")'''




'''def test_ice_spirit_is_displayed():
    # 3. assert Ice Spirit is displayed
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    #assert ice_spirit_card.is_displayed()


# Challenge 1. assert Lava Hound is displayed, then streamline code.
def test_lava_hound_is_displayed(driver):
    lava_hound_card = driver.find_element(By.CSS_SELECTOR, "[href*='Lava+Hound']")
    #assert lava_hound_card.is_displayed()'''




# Challenge 2: See test_ch2_cards_challenge_2.py

