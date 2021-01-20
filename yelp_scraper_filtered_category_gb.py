# Web Scraping of Yelp
import os
os.getcwd() # present directory
os.chdir("...\\Machine Learning\\Project") # changing the directory

# Importing Libraries
import bs4 as bs
import urllib.request as url
import requests
import re
from ast import literal_eval

source = url.urlopen('https://www.yelp.com/search?find_desc=Botanical%20Gardens&find_loc=NYC') # Enter the link to be scraped
category_filter = "Botanical Gardens" # Enter the Category

page_soup = bs.BeautifulSoup(source, 'html.parser')

# For Main Attributes
mains = page_soup.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__1gZC1 arrange-unit-fill__09f24__O6JFU border-color--default__09f24__R1nRO"})
main = mains[0] #First item of mains

#Empty list for main list items
business_name = []
business_url_old = []
business_rating = []
business_reviews = []
business_category = []

#Get Main attributes (business_name, business_rating, business_reviews)
for main in mains:
    try:
        business_name.append(main.find("a").text)
    except:
        business_name.append("")
    try:
        business_url_old.append(main.find("a").get('href'))
    except:
        business_url_old.append("")
    try:
        business_rating.append(main.find("span", {"class": "display--inline__09f24__3iACj border-color--default__09f24__R1nRO"}).div.get('aria-label'))
    except:
        business_rating.append("")
    try:
        business_reviews.append(main.find("span", {"class": "text__09f24__2tZKC reviewCount__09f24__EUXPN text-color--black-extra-light__09f24__38DtK text-align--left__09f24__3Drs0"}).text)
    except:
        business_reviews.append("")
    try:
        business_category.append(main.find("div", {"class": "priceCategory__09f24__2IbAM display--inline-block__09f24__FsgS4 border-color--default__09f24__R1nRO"}).text)
    except:
        business_category.append("")

# Loop to concat "https://www.yelp.com"
business_url = []
for i in business_url_old:
    p = 'https://www.yelp.com' + i
    business_url.append(p)

# For Secondary Attributes
secondarys = page_soup.find_all("div", {"class": "secondaryAttributes__09f24__3db5x arrange-unit__09f24__1gZC1 border-color--default__09f24__R1nRO"})
sec = secondarys[0]

#Empty list for secondary list items
phone = []

#Get Secondary attributes (phone)
for sec in secondarys:
    try:
        phone.append(sec.div.div.text)
    except:
        phone.append("")

#Replace any non-phone numbers with "" (if no values, keeping empty)
business_phone = [x if (bool(re.search(r'[(]\d\d\d[)].\d{3}.\d{4}|[(]\d\d[)].\d{4}.\d{3}|\d{4}.\d{3}.\d{3}', x)) == True) else "" for x in phone]

#####################################################################
biz_ad = []
for i in business_url:
    r = requests.get(i)
    try:
        match = literal_eval(re.search(r'addressLines.+?(\[.+?])', r.text).group(1))
        biz_ad.append(match)
    except:
        biz_ad.append("")

business_address = []
for i in biz_ad:
    business_address.append(','.join(i))

##################################################################
#Save work in excel file
import pandas as pd

data = {}
data = {'business_name': business_name, 'business_rating': business_rating, 'business_url': business_url, 'business_reviews': business_reviews, 'business_address': business_address, 'business_phone': business_phone, 'business_category': business_category}
result = pd.DataFrame(data)
header = ["business_name", "business_url", "business_phone", "business_category", "business_address", "business_rating", "business_reviews"]

filtered_result = result[result.business_category.str.contains(category_filter)]
filtered_result.to_excel("Yelp_File.xlsx", columns = header, index = False)

##############################################################################