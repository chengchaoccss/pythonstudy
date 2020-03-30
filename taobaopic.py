from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.aixdzs.com/')
print(browser.title)