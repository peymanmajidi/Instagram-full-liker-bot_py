import time
from password import my_password
from selenium import webdriver

chrome = webdriver.Chrome("./chromedriver.exe")
chrome.get('https://www.instagram.com/')
time.sleep(2)

username_input = chrome.find_element_by_css_selector("input[name='username']")
password_input = chrome.find_element_by_css_selector("input[name='password']")

username_input.send_keys("peyman_majidi_moein")
password_input.send_keys(my_password)

login_button = chrome.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(2)

doooooooost = "jadijadinet"
chrome.get(f'https://www.instagram.com/{doooooooost}/')

time.sleep(2)

links = chrome.find_elements_by_xpath("//div/a")
valid_links = []
for i in range(0,len(links)):
    href = links[i].get_attribute('href')
    if href.startswith('https://www.instagram.com/p/'):
        valid_links.append(href)

for link in valid_links:
    chrome.get(link)
    like = chrome.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]')
    time.sleep(1)
    like.click()
    

chrome.close()
