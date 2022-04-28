from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = "C:\Program Files (x86)\chromedriver.exe"
username = "username"
password = "pass"
browser = webdriver.Chrome(PATH)

        #opening instagram.com
browser.get('https://www.instagram.com/')

       #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
browser.find_element_by_xpath("//input[@name='password']").send_keys(password)
        #findind login button and clicking it
browser.find_element_by_xpath("//button[@type='submit']").click()
        #-------login process ends

browser.implicitly_wait(5)

     
     
        #Clicking "Not Now" in pop up just after login
sleep(2.5)
not_now_button = browser.find_element_by_xpath("//*[text()='Not now']")
sleep(1)
not_now_button.click()


browser.implicitly_wait(4)

notnow2 = browser.find_element_by_xpath("//*[text()='Not Now']")
sleep(1)
notnow2.click()

for n in range(1000):
 sleep(10)
 commentArea = browser.find_element_by_class_name('Ypffh')
 commentArea.click()
 commentArea = browser.find_element_by_class_name('Ypffh')
 commentArea.send_keys('')
 commentArea.submit()