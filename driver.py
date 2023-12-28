import time
import import_ipynb
import random
from selenium import webdriver 
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_pass import UserPass
from XPATH import  Xpath
from Comments import Comments
from URLS import Url

#web_driver options
options= webdriver.FirefoxOptions()
options.headless= True
service= Service( executable_path= './geckodriver.exe')
driver= webdriver.Firefox( service= service)


#instagram url site
driver.get(Url.instagram())

#time for load page
Pause_Time= 3
time.sleep(Pause_Time+ 5)

#allow cooki
# if driver.find_element('xpath', Xpath.cooki())== True:
#     driver.find_element('xpath', Xpath.cooki()).click()
#     time.sleep(Pause_Time+ 5)

#for login site
#ensert username

username= driver.find_element('xpath', Xpath.username())
username.send_keys(UserPass.user_name())

#ensert password
password= driver.find_element('xpath', Xpath.password())
password.send_keys(UserPass.password())

#enter login button
login= driver.find_element('xpath', Xpath.login_button()).click()
time.sleep(Pause_Time+ 8)

#Skip the first page
saveinfo= driver.find_element('xpath', Xpath.saveinfo_button()).click()
time.sleep(Pause_Time+ 2)

#offing notification
notifications= driver.find_element('xpath', Xpath.notif()).click()
time.sleep(Pause_Time+ 2)

#reload Home page and reload posts
driver.find_element('xpath', Xpath.home()).click()
time.sleep(Pause_Time+ 2)


#Scroll down to bottom and like 50 post per day
counter= 0

while counter<= 50:
    time.sleep(Pause_Time)
    driver.find_element('xpath', Xpath.posts()).click()
    driver.find_element ('xpath', Xpath.home()).click()
    time.sleep(Pause_Time+ 5)
    driver.find_element ('xpath', Xpath.home()).click()
    time.sleep(Pause_Time+ 5)
    counter+= 1
    
#chek the notifications in page
driver.find_element('xpath', Xpath.notif_page()).click()
time.sleep(Pause_Time+5)
driver.find_element('xpath', Xpath.notif_page()).click()
        


#chek and like reels 
driver.find_element('xpath', Xpath.reels()).click()
time.sleep(Pause_Time+5)

for like in range(10):
    driver.find_element('xpath', Xpath.posts()).click()
    time.sleep(Pause_Time+ 10)


   

#Comment for some posts
driver.find_element ('xpath', Xpath.home()).click()
time.sleep(Pause_Time+ 4)

driver.find_element ('xpath', Xpath.home()).click()
time.sleep(Pause_Time+ 4)

for like in range(8):
    comment = driver.find_element('xpath', Xpath.comments())
    comment.send_keys(Comments.comments())
    time.sleep(Pause_Time+ 2)
    driver.find_element('xpath', Xpath.send_comment()).click()
    time.sleep(Pause_Time+ 5)
    driver.find_element ('xpath', Xpath.home()).click()
    time.sleep(Pause_Time+ 4)
    driver.find_element ('xpath', Xpath.home()).click()
    time.sleep(Pause_Time+ 4)


# Comment_counter= 0
# while Comment_counter<= 10:
#     driver.find_element ('xpath', Xpath.Home()).click()
#     time.sleep(Pause_Time)
#     driver.find_element ('xpath', Xpath.Home()).click()
#     time.sleep(Pause_Time)
#     driver.find_element('xpath', "//*[local-name()='svg' and @aria-label='Comment']").click()
    
