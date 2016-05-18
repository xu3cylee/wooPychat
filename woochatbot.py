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
def sendMessage(text):
	textBox = driver.find_element_by_id('messageInput')
	textBox.send_keys(str(text).decode('utf-8'))
	driver.find_element_by_id('sendButton').click()
	return
def keepChat():
	if 'hi' in strangerText.text or 'Hi' in strangerText.text or '嗨' in strangerText.text or '好' in strangerText.text or '安' in strangerText.text:
		sendMessage("嗨！")
		#keepChat()
	else:
		sendMessage("到公海了嗎？")

def leave():
	driver.find_element_by_id('changeButton').click()
	time.sleep(0.5)
	##if the user left, the popup message won't be displayed###
	try:
		driver.find_element_by_id('popup-yes').click()
	except:
		pass
def chatbot():##chatbot starts to do its job =)##
	driver.find_element_by_class_name('buttons').click()
	time.sleep(3)
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
		leave()
	print strangerText.text[4:]
	censoredWords = ['男', '女嗎', '色', '約', '18', '17', '壯', '性', '找', '女?', '愛', '尋']
	for i in censoredWords:
		if i in strangerText.text:
			sendMessage("第一句話不會問好喔？幹喔！")
			break
		else:
			keepChat()
			break
	time.sleep(5)
	"""
	sendMessage("掰掰！")
	"""
	time.sleep(0.5)
	leave()
if __name__ == '__main__':
	while True:
		try:
			checkLeave = driver.find_element_by_css_selector(".system.text")
			if "對方離開" in checkLeave:
				leave()
				checkbot()
		except:
			time.sleep(2)
			chatbot()
