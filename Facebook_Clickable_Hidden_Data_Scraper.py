# Facebook Clickable Hidden Data Scraper
# Importing the libraries
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import datetime

# Need to install the Chrome driver before going ahead with the below code (https://sites.google.com/a/chromium.org/chromedriver/getting-started)
driver = webdriver.Chrome(executable_path=r"E:\Software\Data Science Software\Chrome Driver\chromedriver_win32\chromedriver.exe") # "E:\Software\Data Science Software\Chrome Driver\chromedriver_win32\chromedriver.exe" is the path of chromedriver.exe file

driver.get('https://www.facebook.com/events/325278428447630/')
driver.find_element_by_xpath('//*[@id="u_0_n_Pz"]').click() #Note: xpath sometimes get change. If so, please change the xpath address or manually click on "Accept All"
driver.find_element_by_xpath('//*[@id="sibling_time_series"]/div[2]/div/a/div/div').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

raw_data = soup.find('div', class_='uiScrollableAreaContent').text
print(raw_data)

driver.close()

###############################################
# Note: Raw data format we are getting is as below:
# raw_data = '''FRI57:30 PM - 9:30 PM EST1,063 people interestedGet Tickets9:45 PM - 11:45 PM EST163 people interestedGet TicketsSAT67:00 PM - 9:00 PM EST282 people interestedGet Tickets9:30 PM - 11:30 PM EST59 people interestedGet TicketsSUN77:00 PM - 9:00 PM EST64 people interestedGet Tickets'''

# Note: Clean data format as like below:
# clean_data = '''FRI, 5, 7:30 PM - 9:30 PM EST (1,063 people interested); 9:45 PM - 11:45 PM EST (163 people interested); SAT, 6, 7:00 PM - 9:00 PM EST (282 people interested); 9:30 PM - 11:30 PM EST (59 people interested); SUN, 7, 7:00 PM - 9:00 PM EST (64 people interested)'''

###############################################