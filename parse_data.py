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
from bs4 import BeautifulSoup
import re
import csv

def pull_time(link):
	return link[58:74]

def convert_string(num):
	if "K" in num:
		return int(float(num.replace('K', '')) * 1000)
	else:
		return int(num)

def format_comments(str):
	comments = str.split()

	return convert_string(comments[0])

### Pulls the number of likes from a single post
def num_likes(driver):
	try:
		num_comments = driver.find_element_by_class_name('_81hb').text
	except Exception:
		return 0

	return convert_string(num_comments)

### Pulls the number of pictures from a single post
def num_pics(driver):
	pictures = driver.find_elements_by_css_selector("a[rel = 'theater']")
	
	pic_links = []
	for pic in pictures:
		pic_links.append(pic.get_attribute("href"))
	pic_links = pic_links[4:]

	try:
		extra_pics = driver.find_element_by_css_selector("div[class = '_52db']").text
		return len(pic_links) + int(extra_pics[1:]) - 1
	except Exception:
		pass
	
	return len(pic_links)

### Pulls the number of comments from a single post
def num_comments(driver):
	try:
		num_comments = driver.find_element_by_css_selector("a[class = '_3hg- _42ft']").text
	except Exception:
		return 0
	
	return format_comments(num_comments)

### Pulls the text data from the post and stores data in a txt file
def pull_text(url, driver):
	body1 = driver.find_elements_by_tag_name("p")
	body2 = driver.find_elements_by_css_selector("div[class = '_2cuy _3dgx _2vxa']")
	extra1 = driver.find_elements_by_css_selector("span[class = '_4yxo']")
	extra2 = driver.find_elements_by_css_selector("li[class = '_2cuy _509q _2vxa']")
	
	body = body1 + body2 + extra1 + extra2
	
	for text in body:
		print(text.text)

	with open('/Users/alexanderxiong/Documents/GitHub/trawl-SAD/' + str(url), "w+") as f:
		for line in body:
			f.write("%s\n" % line.text)
	f.close()

### Overall function for one post
def data_from_post(link, driver):
	try:
		notFound = driver.find_element_by_css_selector("div[class = '_585r _50f4']")
		if notFound.text == "This post has been removed or could not be loaded.":
			return pull_time(link), [0,0,0]
	except:
		pass
	numLikes = num_likes(driver)
	numPics = num_pics(driver)
	numComments = num_comments(driver)

	data = [numLikes, numPics, numComments]

	print(data)

	pull_text(pull_time(link), driver)

	return pull_time(link), data

### Debugging specific lines
# line = 'https://www.facebook.com/groups/725870897781323/permalink/1146498932385182/'
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(options=chrome_options)

# driver.implicitly_wait(30)

# user = 'whoami.2008@mail.com'  
# pwd = 'welive1life'

# driver.get('https://www.facebook.com')

# try:
# 	elem = driver.find_element_by_id("email")
# 	elem.send_keys(user)
# 	elem = driver.find_element_by_id("pass")
# 	elem.send_keys(pwd)
# except Exception:
# 	elem = driver.find_element_by_name("email")
# 	elem.send_keys(user)
# 	elem = driver.find_element_by_name("pass")
# 	elem.send_keys(pwd)

# elem.send_keys(Keys.RETURN)

# time.sleep(2)

# driver.get(line)

# timedate, post_data = data_from_post(line, driver)
# driver.close()

### General Code
data_storage_dict = {}

f_read = open("rewrite_links.txt", "r")
all_lines = f_read.readlines()
for line in all_lines[-2:]:
	print(str(line) + ": " + str(datetime.now()))
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options=chrome_options)
	
	driver.implicitly_wait(30)

	user = 'whoami.2008@mail.com'  
	pwd = 'welive1life'

	driver.get('https://www.facebook.com')

	try:
		elem = driver.find_element_by_id("email")
		elem.send_keys(user)
		elem = driver.find_element_by_id("pass")
		elem.send_keys(pwd)
	except Exception:
		elem = driver.find_element_by_name("email")
		elem.send_keys(user)
		elem = driver.find_element_by_name("pass")
		elem.send_keys(pwd)

	elem.send_keys(Keys.RETURN)

	time.sleep(2)

	driver.get(line)

	timedate, post_data = data_from_post(line, driver)
	data_storage_dict[timedate] = post_data
	driver.close()

f_read.close()

print(len(data_storage_dict))

w = csv.writer(open("output_dict.csv", "w"))
for key, val in data_storage_dict.items():
    w.writerow([key, val[0], val[1], val[2]])





