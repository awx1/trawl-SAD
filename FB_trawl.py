from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime, date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

# Insert your username and password here
user= 
pwd= 

driver.get('https://www.facebook.com')

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(2)

#Insert the link for the facebook group that you want to pull the links for different posts from
driver.get('https://www.facebook.com/groups/725870897781323/?sorting_setting=CHRONOLOGICAL')

def scrapePost(drive):
	url = drive.find_elements(By.CLASS_NAME, "_5pcq")
	print("Length of urls list: " + str(len(url)))

	new_url = []
	for webElem in url:
		try:
			print("Try: ")
			new_url.append(webElem.get_attribute("href"))
		except TimeoutException:
			print("Except: ")
			pass

	return new_url

start = datetime.now()
print("Start Loop: " + str(start))

count = 0

var = True
while var:
	try:
		while var:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			print(str(count) + ': ' + str(datetime.now()))
			time.sleep(5)
			count += 1
			if count > 100:
				var = False
		break
	except TimeoutException:
		time.sleep(60)
		print("Sleeping, please do not wake up")
		if count > 100:
			var = False

# try:
# 	for i in range(5000):
# 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		print(str(count) + ': ' + str(datetime.now()))
# 		time.sleep(0.1)
# 		count += 1
# except TimeoutException:
# 	time.sleep(10)
# 	print("Sleeping, please do not wake up")
# 	try:
# 		for i in range(5000):
# 			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 			print(str(count) + ': ' + str(datetime.now()))
# 			time.sleep(0.1)
# 			count += 1
# 	except TimeoutException:
# 		pass
# 	pass

# while True:
#     try:
#         for i in range(5000):
# 			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 			print(str(count) + ': ' + str(datetime.now()))
# 			time.sleep(0.1)
# 			count += 1
#         break
#     except TimeoutException: 
#         pass

# lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

# match=False

# while(match==False):
# 	lastCount = lenOfPage
# 	print(str(count) + ': ' + str(datetime.now()))
# 	time.sleep(20)
# 	lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# 	count += 1
# 	if lastCount==lenOfPage:
# 		match=True

# Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# SCROLL_PAUSE_TIME = 3

# elem = driver.find_element_by_tag_name("body")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait to load page

#     if count >= 200:
#     	SCROLL_PAUSE_TIME = 15

#     time.sleep(SCROLL_PAUSE_TIME)

#     print(str(count) + ': ' + str(datetime.now()))

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     count += 1

end = datetime.now()
print("End Loop: " + str(end))

#overall = datetime.combine(date.today(), end) - datetime.combine(date.today(), start)
#print("Total Loop: " + str(overall))

urls = scrapePost(driver)

total_links = 0
with open('links.txt', 'w') as f:
	for item in urls:
		total_links += 1
		f.write("%s\n" % item)
		print(total_links)

print("Total links: " + str(total_links))

print("Finish writing in file: " + str(datetime.now()))