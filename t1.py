from selenium import webdriver
import filecmp
import time
import os

browser = webdriver.Chrome('C:\\Users\\Owner\\Desktop\chromedriver.exe')
browser.get("http://www.gmail.com")

ready = ""
print ("Authenticate to NAMMCal.")
while ready != "Yes":
    ready = input("Heve you authenticated (Y/N)? ")
    if ready == "y" or ready == "Y" or ready == "Yes" or ready == "yes":
        break
    else:
        print ("Please authenticate")
print("Fuck Yeah")

countDown = 30

elem1 = browser.find_element_by_id(':3b')
source_code = elem1.get_attribute("outerHTML")
    
while True:
    '''
    browser.get("http://www.gmail.com")
    elem1 = browser.find_element_by_id(':3b')
    source_code = elem1.get_attribute("outerHTML")

'''
    while countDown > 0:
        print ("Refreshing in: " + str(countDown))
        countDown = countDown - 1
        time.sleep(1)
    print ("Refreshing in: 0 \n")
    
    browser.get("http://www.gmail.com")
    elem = browser.find_element_by_id(':3b')
    source_code1 = elem.get_attribute("outerHTML")

    print (source_code)
    print ('\n')
    print (source_code1)
    print ('\n')

    if source_code == source_code1:
        print("No New Alarm. \n")
        countDown = 30
    else:
        elem1 = elem
        source_code = source_code1
        print("New Alarm! \n")
        os.system('C:\\Users\\Owner\\Desktop\mail.mp3')
        time.sleep(10)
        countDown = 60
        print("Restarting services \n")
