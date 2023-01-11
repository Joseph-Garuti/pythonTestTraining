from selenium import webdriver
from selenium.webdriver.common.by import By

def test_uncheck_Common_Filter():
    driver = webdriver.Chrome(
        'C:/Users/ssjga/PycharmProjects/pythonTestTraining/venv/Lib/site-packages/selenium/webdriver/chromedriver.exe')

    driver.maximize_window()

    # 1. go to statsroyale.com
    driver.get('https://statsroyale.com/cards')

    '''exists = driver.find_element(By.NAME, 'common-cards')
    assert exists.is_displayed()'''

    driver.find_element(By.NAME, 'common-cards').click()

    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert not ice_spirit_card.is_displayed()
