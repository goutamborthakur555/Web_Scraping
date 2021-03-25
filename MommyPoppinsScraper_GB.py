# Mommy Poppins Scraper
# Setting up the directory
import os
os.getcwd() # present directory
os.chdir("....\\Web Scraping\\Mommy Poppins") # changing the directory

# Importing Libraries
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Links from where data need to be extracted/scrapped
master_link = 'https://mommypoppins.com/events/115/los-angeles/all/tag/all/age/03-01-2021/03-31-2021/deals/0/near/0/0' #Enter the website link

# Opening the chrome browser using webdriver
driver = webdriver.Chrome(executable_path=r"chromedriver_win32\chromedriver.exe")
driver.get(master_link)
soup = BeautifulSoup(driver.page_source, 'html.parser')
mains = soup.find_all("a", {"angularticsaction": "expanded-detail"})

attributes = [{el.text: el.get('href')} for el in mains]

#Empty list for attributes list items
name = []
mp_link = []

for main in attributes:
    for key,value in main.items():
        try:
            name.append(key)
        except:
            name.append("")
        try:
            mp_link.append("https://mommypoppins.com" + value)
        except:
            mp_link.append("")

driver.quit() #To close all the tab
#driver.close() #To close the current tab

#Empty list for remaining items
date = []
evnt_time = []
age = []
price = []
description = []
phone = []
email = []
website = []
ind_attributes_lst = []

# Opening the chrome browser using webdriver
driver = webdriver.Chrome(executable_path=r"chromedriver_win32\chromedriver.exe")

for ind_lnk in mp_link:  
    driver.get(ind_lnk)
    
    # To expand the date details
    #see_all_dates = driver.find_elements_by_xpath('//*[@id="node-state"]/div[1]/div/app-eventinfo/div/div[1]/span/a')
    #see_all_dates[0].click()
    
    #date.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event.ng-star-inserted > div > app-eventinfo > div > div.date-repeats.ng-star-inserted").text)
    
    try:
        date.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event > div > app-eventinfo > div > div.date-repeats > strong").text)
    except:
        date.append("")
    try:
        evnt_time.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event.ng-star-inserted > div > app-eventinfo > div > div:nth-child(2) > strong").text)
    except:
        evnt_time.append("")
    try:
        age.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event.ng-star-inserted > div > app-eventinfo > div > div:nth-child(3) > span").text)
    except:
        age.append("")
    try:
        price.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event.ng-star-inserted > div > app-eventinfo > div > div:nth-child(4) > span").text)
    except:
        price.append("")
    try:
        description.append(driver.find_element_by_css_selector("#node-state > div.content-head-wrapper.content-wrapper.event.ng-star-inserted > div > app-bodyparsed").text)
    except:
        description.append("")
    
    # To extract the list for Website links
    ind_soup = BeautifulSoup(driver.page_source, 'html.parser')
    ind_mains = ind_soup.find_all("a", {"angularticsaction": "contentClick"})
    ind_attributes = [{el.text: el.get('href')} for el in ind_mains]
    ind_attributes_lst.append(ind_attributes)

driver.quit() #To close all the tab
#driver.close() #To close the current tab

# Filtering out the phone number
for ph_attr in ind_attributes_lst:
    ph_check = []
    for ph_dct in ph_attr:
        ph_check += [val for val in ph_dct.values() if re.match(r'tel:\(?(\d{3})\)?[^\d]*(\d{3})[^\d]*(\d{4})', val)]
    phone.append(', '.join(ph_check)[4:].replace('.', ' ') if ph_check else '')

# Filtering out the email id
for em_attr in ind_attributes_lst:
    em_check = []
    for em_dct in em_attr:
        em_check += [val for val in em_dct.values() if re.match(r'mailto:([\w\.]+@\w+\.\w+).*', val)]
    email.append(', '.join(em_check)[7:].split('?')[0] if em_check else '')

# Filtering up the website links
for web_attr in ind_attributes_lst:
    vl_check = []
    for dct in web_attr:
        vl_check += [val for val in dct.values() if re.match(r'https?[/\w\.]*', val)]
    website.append(', '.join(vl_check) if vl_check else '')

# Save work in excel file
data = {}
data = {'Name': name, 'MommyPoppins_Link': mp_link, 'Date': date, 'Time': evnt_time, 'Age': age, 'Price' : price, 'Phone' : phone, 'Email' : email,'Website' : website, 'Description' : description}

# Converting to dataframe
result = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in data.items()])) #As all arrays are of not same lenght 
header = ['Name', 'MommyPoppins_Link', 'Date', 'Time', 'Age', 'Price', 'Phone', 'Email', 'Website', 'Description']

# Exporting to .xlsx file
result.to_excel("MommyPoppins_50_sample_records.xlsx", columns = header, index = False)

########################################################################

