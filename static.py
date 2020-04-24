from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("D:\Peyman\Desktop\chromedriver.exe")

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")

        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def like_photo(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            time.sleep(random.randint(2, 4))
            like_button = driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]')
            like_button.click()

        except:
            print("not found")
            time.sleep(2)


if __name__ == "__main__":

    username = "_i_am_matin__"
    password = "0047967"

    ig = InstagramBot(username, password)
    ig.driver.get("file:///D:/Peyman/Desktop/peyman.html")
    
    ig.like_photo()
