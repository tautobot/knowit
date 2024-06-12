import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import headless

filepath = os.path.dirname(__file__)
IMPLICITLY_WAIT = 5


def options():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    if headless == 'yes':
        chrome_options.add_argument("--headless")
    else:
        pass

    return chrome_options


def webdriver_local():
    chrome_options = options()
    chrome_options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.maximize_window()
    return driver


def webdriver_docker():
    options().add_argument(webdriver.ChromeOptions)
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options()
    )
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.maximize_window()
    return driver
