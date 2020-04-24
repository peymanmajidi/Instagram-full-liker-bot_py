import time
from selenium import webdriver

chrome = webdriver.Chrome("D:\Peyman\Desktop\chromedriver.exe")

chrome.get('https://www.instagram.com/')

time.sleep(2)

username_input = chrome.find_element_by_css_selector("input[name='username']")
password_input = chrome.find_element_by_css_selector("input[name='password']")

username_input.send_keys("_i_am_matin__")
password_input.send_keys("0047967")

login_button = chrome.find_element_by_xpath("//button[@type='submit']")
login_button.click()




def first_picture(): 
    
    # finds the first picture  
    pic = chrome.find_element_by_class_name("_9AhH0")    
    pic.click()   # clicks on the first picture 

def like_pic(): 
    time.sleep(4) 
    like = chrome.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]')
    time.sleep(2) 
    like.click()   # clicking the like button 


def next_picture(): 
    time.sleep(2) 
  
    # finds the button which gives the next picture 
    nex = chrome.find_element_by_class_name("HBoOv")   
    time.sleep(1) 
    return nex 

def continue_liking(): 
    while(True): 
        next_el = next_picture() 
  
        # if next button is there then 
        if next_el != False:   
  
            # click the next button 
            next_el.click()    
            time.sleep(2) 
  
            # like the picture 
            like_pic()     
            time.sleep(2)             
        else: 
            print("not found")  
            break


time.sleep(5)


chrome.get('https://www.instagram.com/peyman_majidi_moein/')

time.sleep(2)

links = chrome.find_elements_by_xpath("//div/a")
valid_links = []
for i in range(0,len(links)):
    href = links[i].get_attribute('href')
    if href.startswith('https://www.instagram.com/p/'):
        valid_links.append(href)

for link in valid_links:
    chrome.get(link)
    chrome.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]').click()




chrome.close()
