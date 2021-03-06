import requests
import json
from urllib.request import urlopen
from selenium import webdriver
import time
import sys

#global
gecko = 'C:[insert path]'
cdrive = '[insert path]'

def menu():
    print('*'*5,'Automated Weekly Testing','*'*5,
          '\n*',' '*32,'*',
          '\n*',' '*5,'1. Test Firefox',' '*10,'*',
          '\n*',' '*5,'2. Test Chrome ',' '*10,'*',
          '\n*',' '*5,'3. Test Explorer',' '*9,'*', #unavailable
          '\n*',' '*5,'    0. Exit',' '*14,'*',
          '\n*',' '*32,'*',
          '\n*','*'*32, '*')
    choice = int(input('Pick Choice: '))
    pick(choice)

def firefox():
    driver1 = webdriver.Firefox(executable_path= gecko)
    driver1.get('http://google.com')
    driver1.maximize_window()
    print('Worked')
    #driver1.quit()

def chrome():
    url = '[insert url]'
    #Open Chrome
    driver2 = webdriver.Chrome(cdrive)
    driver2.get(url)
    driver2.maximize_window()
    time.sleep(10)

    #Home Page -  First CheckPoint
    check = driver2.find_element_by_xpath('//h1[contains(text(), "[text]")]')
    check2 = driver2.find_element_by_xpath('//h5[contains(text(), "[text]")]')
    check3 = driver2.find_element_by_xpath('//h5[contains(text(), "[text]")]')
    check4 = driver2.find_element_by_xpath('//h5[contains(text(), "[text]")]')
    if check and check2 and check3 and check4:
        print('CheckPoint #1: Passed!')
    else:
        print('CheckPoint #1: Error!')
    ###########################################
    time.sleep(10)
    signin = driver2.find_element_by_xpath('//div[@class="header-item lonely"]//a[@class="menu-link"]').click()
    time.sleep(3)
    user = driver2.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input"]').send_keys('[username]')
    time.sleep(3)
    psw = driver2.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input disabledAutoFillPassword"]').send_keys('[password]')
    enter = driver2.find_element_by_xpath('//div[@class="form__box"]//button[@type="submit"]').click()
    time.sleep(10)
    #driver2.quit()

def explorer():
    print('Unavailable')


def pick(choice):
    if choice == 1:
        firefox()
    elif choice == 2:
        chrome()
    elif choice == 3:
        explorer()
    elif choice == 0:
        sys.exit()
    else:
        print('Invalid Choice')
        menu()
menu()
