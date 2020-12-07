import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def Search(string):
	service = Service('C:\Program Files\chromedriver.exe')
	service.start()
	driver = webdriver.Remote(service.service_url)
	driver.get(string)
	time.sleep(5)