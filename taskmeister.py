from selenium import webdriver

print('Input your taskmeister email address')
userEmail = input()
print('Input your taskmeister password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('http://taskmeister.com')

loginElem = browser.find_element_by_id('login-header')
loginElem.click()

emailElem = browser.find_element_by_id('edit-mail')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('edit-pass')
passwordElem.send_keys(userPassword)
passwordElem.submit()
