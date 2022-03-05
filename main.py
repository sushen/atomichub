import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib

import winsound

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
driver = webdriver.Chrome(r"./chromedriver.exe", chrome_options=chrome_options)

# paths variables
# login_link = "https://opensea.io/login?referrer=%2Faccount"
# NFT_link = "https://wax.atomichub.io/"
NFT_link = "https://wax.atomichub.io/market/sale/64194421"

driver.get(NFT_link)