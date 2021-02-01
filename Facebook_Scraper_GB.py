# Facebook Scraper
# Setting up the directory
import os
os.getcwd() # present directory
os.chdir(".....\\Web Scraping\\Facebook") # changing the directory

# Importing the libraries
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

import_fb_links = pd.read_excel("Desktop/FB_event_links.xlsx") # Reading the Excel file (FB_event_links) consisting of FB Event links from Desktop

event_links = import_fb_links['FB_Links'].tolist() # Converting to list

# Empty list for data to be scrapped
Event_Link = []
Event_Name = []
Event_Date = []
Days_Left = []
People_Responded = []
Address = []
Hosted_By = []
Descriptions = []
Tags = []
Ticket_Purchase_Link = []

# Event_Link
Event_Link = event_links

# Event_Name, Event_Date, Days_Left, People_Responded, Address, Hosted_By, Descriptions, Tags, Ticket_Purchase_Link
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
for i in event_links:
    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        en = soup.find('div', class_=['2ycp', '_5xhk']).text
        Event_Name.append(en)
    except:
        Event_Name.append("")
    try:
        ed = soup.find('div', class_=['_2ycp _5xhk']).text
        Event_Date.append(ed)
    except:
        Event_Date.append("")
    try:
        dl = soup.find('div', class_=['_5xhp fsm fwn fcg']).text
        Days_Left.append(dl)
    except:
        Days_Left.append("")
    try:
        pr = soup.find('span', class_=['_5z74']).text
        People_Responded.append(pr)
    except:
        People_Responded.append("")
    try:
        ad = soup.find('div', class_=['_4930']).text
        Address.append(ad)
    except:
        Address.append("")
    try:
        hb = soup.find('div', class_=['_5gnb']).text
        Hosted_By.append(hb)
    except:
        Hosted_By.append("")
    try:
        ds = soup.find('div', class_=['_63ew']).text
        Descriptions.append(ds)
    except:
        Descriptions.append("")
    try:
        tg = soup.find('ul', class_=['_63er']).text
        Tags.append(tg)
    except:
        Tags.append("")
    try:
        tp = driver.find_element_by_xpath("//*[@id='u_0_z']/table/tbody/tr/td[2]/div/div[1]/div/div[2]/div/div").text
        Ticket_Purchase_Link.append(tp)
    except:
        Ticket_Purchase_Link.append("")

driver.close()

# Save work in excel file
data = {}
data = {'Event_Link': Event_Link, 'Event_Name': Event_Name, 'Event_Date': Event_Date, 'Days_Left': Days_Left, 'People_Responded': People_Responded, 'Address': Address, 'Hosted_By': Hosted_By, 'Descriptions': Descriptions, 'Tags': Tags, 'Ticket_Purchase_Link': Ticket_Purchase_Link}

result = pd.DataFrame(data)
header = ['Event_Name', 'Event_Date', 'Days_Left', 'People_Responded', 'Hosted_By', 'Address', 'Event_Link', 'Descriptions', 'Tags', 'Ticket_Purchase_Link']

result.to_excel("Facebook_Event_Details.xlsx", columns = header, index = False)

###############################################################################
### Thank You!!! ###
###############################################################################