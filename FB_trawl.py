from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.set_preference("dom.webnotifications.enabled", False)
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_options=options, executable_path = '/Users/alexanderxiong/Documents/Projects/geckodriver')

user= 'whoami.2008@mail.com'  
pwd= 'welive1life'

driver.get('https://www.facebook.com')

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(5)
driver.get('https://www.facebook.com/groups')

sad = driver.find_element_by_link_text("subtle asian dating")
sad.click()

time.sleep(5)

while True:
	htmlElem = driver.find_element_by_tag_name('html')
	htmlElem.send_keys(Keys.END)

	time.sleep(5)