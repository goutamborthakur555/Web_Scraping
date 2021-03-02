# YouTube Scraper
# Setting up the directory
import os
os.getcwd() # present directory
os.chdir("....\\Web Scraping\\YouTube") # changing the directory

# Importing the libraries
import pandas as pd
from selenium import webdriver

# Enter the search keywords
search_keyword = input('Enter your search keyword: ') # kids events in California

# YouTube main link
master_link = 'https://www.youtube.com/'

# Final search link after concating with the search keyword
search_link = master_link + 'search?q=' + search_keyword

# Opening the chrome browser using webdriver
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get(search_link)

cl_data = driver.find_elements_by_css_selector("#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
cl_links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),cl_data)))

# Empty lists
channel_name = []
channel_link = []
channel_subscriber = []
location = []
channel_joined_date = []
channel_views = []
channel_description = []
channel_all_links = []

for link in cl_links:
    driver.get(f"{link}/about")
    # Channel Name
    try:
        cn_name = driver.find_element_by_css_selector("#text.style-scope.ytd-channel-name").text
        channel_name.append(cn_name)
    except:
        channel_name.append("")
    
    # Channel Link
    try:
        channel_link.append(link)
    except:
        channel_link.append("")
    
    # Channel Subscriber
    try:
        cn_subscr = driver.find_element_by_xpath("//*[@id='subscriber-count']").text
        channel_subscriber.append(cn_subscr)
    except:
        channel_subscriber.append("")
    
    # Location
    try:
        cn_loc = driver.find_element_by_xpath("//*[@id='details-container']/table/tbody/tr[2]/td[2]").text
        location.append(cn_loc)
    except:
        location.append("")
    
    # Channel Joined Date
    try:
        cn_jn_dt = driver.find_element_by_xpath("//*[@id='right-column']/yt-formatted-string[2]/span[2]").text
        channel_joined_date.append(cn_jn_dt)
    except:
        channel_joined_date.append("")
    
    # Channel Views
    try:
        cn_vws = driver.find_element_by_xpath("//*[@id='right-column']/yt-formatted-string[3]").text
        channel_views.append(cn_vws)
    except:
        channel_views.append("")
    
    # Channel Description
    try:
        cn_description = driver.find_element_by_css_selector("#description-container > yt-formatted-string:nth-child(2)").text
        channel_description.append(cn_description)
    except:
        channel_description.append("")
    
    # Additional Links available in Channel
    try:
        ot_links = driver.find_elements_by_css_selector("#link-list-container.style-scope.ytd-channel-about-metadata-renderer a.yt-simple-endpoint.style-scope.ytd-channel-about-metadata-renderer")
        cn_all_links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),ot_links)))
        channel_all_links.append(cn_all_links)
    except:
        channel_all_links.append("")

driver.close()

# Empty list
linkedin = []
twitter = []
facebook = []
instagram = []
pinterest = []
website = []
blog = []
other_links = []

# Filter out the particular links
for lnk in channel_all_links:        
    if "Linkedin" or "LinkedIn" in lnk:
        try:
            linkedin.append(lnk)
        except:
            linkedin.append("")
    elif "Twitter" in lnk:
        try:
            twitter.append(lnk)
        except:
            twitter.append("")
    elif "Facebook" in lnk:
        try:
            facebook.append(lnk)
        except:
            facebook.append("")
    elif "Instagram" in lnk:
        try:
            instagram.append(lnk)
        except:
            instagram.append("")
    elif "Pinterest" in lnk:
        try:
            pinterest.append(lnk)
        except:
            pinterest.append("")
    elif "Website" in lnk:
        try:
            website.append(lnk)
        except:
            website.append("")
    elif "Blog" or "Blogger" in lnk:
        try:
            blog.append(lnk)
        except:
            blog.append("")
    else:
        try:
            other_links.append(lnk)
        except:
            other_links.append("")
# Empty list
phone = []
email = []
website1 = []

# Pattern to filter out the particular details
phone_pattern = r"""(\+\d\s*\d(?:-?\d)+)"""
email_pattern = r"""([a-z]+@[\w.-]+(?:\.[\w.-]+)*\.[a-z]{2,6})"""
website1_pattern = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

for dt in channel_description:
    import re
    phn = re.findall(phone_pattern, dt)
    eml = re.findall(email_pattern, dt)
    web = re.findall(website1_pattern, dt)
    
    if (phn==True):
        try:
            phone.append(phn)
        except:
            phone.append("")
    
    elif (eml==True):
        try:
            email.append(eml)
        except:
            email.append("")
    
    elif (web==True):
        try:
            website1.append(web)
        except:
            website1.append("")

# Save work in excel file
data = {}
data = {'Channel_Name': channel_name, 'Channel_Link': channel_link, 'Channel_Subscriber': channel_subscriber, 'Location': location, 'Channel_Joined_Date': channel_joined_date, 'Channel_Views': channel_views, 'LinkedIn' : linkedin, 'Twitter' : twitter, 'Facebook' : facebook, 'Instagram' : instagram, 'Pinterest' : pinterest, 'Website' : website, 'Website1' : website1, 'Blog' : blog, 'Other_Links' : other_links, 'Phone' : phone, 'Email' : email, 'Channel_Description': channel_description}

# Converting to dataframe
result = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in data.items()])) #As all arrays are of not same lenght 
header = ['Channel_Name', 'Channel_Link', 'Channel_Subscriber', 'Location', 'Channel_Joined_Date', 'Channel_Views', 'LinkedIn', 'Twitter', 'Facebook', 'Instagram', 'Pinterest', 'Website', 'Website1', 'Blog', 'Other_Links', 'Phone', 'Email', 'Channel_Description']

# Exporting to .xlsx file
result.to_excel("Raw_YouTube_Channel_Details.xlsx", columns = header, index = False)

###############################################################################