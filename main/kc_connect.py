from kiteconnect import KiteConnect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import global_variables


def set_access_token():
    global_variables.logger.info("Getting Access Token ... ")
    global_variables.kite = KiteConnect(global_variables.key_secret[0])
    service = webdriver.chrome.service.Service('../driver/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options = options.experimental_options
    driver = webdriver.Remote(service.service_url, options)
    driver.get(global_variables.kite.login_url())
    driver.maximize_window()
    time.sleep(5)
    username = driver.find_element(By.XPATH, './/input[@id="userid"]')
    username.send_keys(global_variables.key_secret[2])
    password = driver.find_element(By.XPATH, './/input[@id="password"]')
    password.send_keys(global_variables.key_secret[3])
    login_button = driver.find_element(By.XPATH, ".//button")
    login_button.click()
    time.sleep(5)
    pin = driver.find_element(By.XPATH, './/input[@id="totp"]')
    pin.send_keys(global_variables.token_totp)
    continue_button = driver.find_element(By.XPATH, ".//button")
    continue_button.click()
    time.sleep(5)
    global_variables.request_token = driver.current_url.split('request_token=')[1][:32]
    global_variables.logger.info("Find request token : " + global_variables.request_token)
    driver.quit()
    global_variables.kite = KiteConnect(api_key=global_variables.key_secret[0])
    data = global_variables.kite.generate_session(global_variables.request_token,
                                                  api_secret=global_variables.key_secret[1])
    with open('../datafiles/access_token.txt', 'w') as the_file:
        the_file.write(data["access_token"])


def login_with_access_token():
    global_variables.logger.info("Setting Access Token ... ")
    global_variables.kite = KiteConnect(api_key=global_variables.key_secret[0])
    global_variables.kite.set_access_token(global_variables.access_token)
