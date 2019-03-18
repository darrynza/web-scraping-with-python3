
from selenium import webdriver


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/firefox"
driver = webdriver.Firefox(firefox_options=options)
driver.get('https://python.org')