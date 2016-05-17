# -*- coding: utf-8 -*-
import sys  
import os
import time
from selenium import webdriver
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
chromedriver = "/Users/cylee/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://wootalk.today/key/%E6%88%90%E4%BA%BA%E6%A8%A1%E5%BC%8F")
#driver.get("https://wootalk.today")
driver.find_element_by_class_name('buttons').click()
time.sleep(23) ##time for human verification. =D
driver.refresh() 
def chatbot():##chatbot starts to do its job =)##
	driver.find_element_by_class_name('buttons').click()
	time.sleep(3)
	textBox = driver.find_element_by_id('messageInput')
	time.sleep(2)
	strangerText = None
	timeoff = 0
	while strangerText is None:
		try:
			timeoff += 1
			#print timeoff
			strangerText = driver.find_element_by_css_selector(".stranger.text")
		except:
			pass
	##dealing with dead ends(people who are AFK)###
	if timeoff > 5000:
		driver.find_element_by_id('changeButton').click()
		time.sleep(0.5)
		try:
			driver.find_element_by_id('popup-yes').click()
		except:
			pass
		return
	print strangerText.text.strip('陌生人：')
	censoredWords = ['男', '女嗎', '色', '約', '18', '17', '壯', '性', '找', '女?', '愛', '尋']
	for i in censoredWords:
		if i in strangerText.text and 'hi' not in strangerText.text and 'Hi' not in strangerText.text and '嗨' not in strangerText.text and '好' not in strangerText.text:
			textBox.send_keys("Please by polite. Say hi first!")
			driver.find_element_by_id('sendButton').click()
			break
	time.sleep(2.5)
	textBox.send_keys("This is a chatbot developed by z.lee. Have a nice day!")
	driver.find_element_by_id('sendButton').click()
	time.sleep(5)
	driver.find_element_by_id('changeButton').click()
	time.sleep(0.5)
	##if the user left, the popup message won't be displayer###
	try:
		driver.find_element_by_id('popup-yes').click()
	except:
		pass
while True:
	time.sleep(2)
	chatbot()