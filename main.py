# web scrape modules
from bs4 import BeautifulSoup
import requests
# for automatisation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# google docs link
google_docs = "https://docs.google.com/forms/d/e/1FAIpQLSd256mX2TuwqtVCNmEzpTZN5IFj1fXwIvHeteJuSoaIH4G2fQ/viewform?usp=sf_link"

#        ------------------             Request and Bs4 phase   ---------------------   #

# get request to web end point
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
# get web data
soup = BeautifulSoup(response.content, "html.parser")
# get price
all_price = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text[1:6:] for price in all_price]
#get house address
all_addrs = soup.find_all("address")
addr_list = [addr.text.replace("\n","").strip() for addr in all_addrs]
# Get links
all_links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
link_list = [link["href"] for link in all_links]

# house_catalogue = {}

# for house in range(len(all_links)):
#     dict = {f"name {house}" : addr_list[house],f"price {house}" : price_list[house],f"link {house}" : link_list[house]}
#     house_catalogue.update(dict)

# print(house_catalogue)


#    ---------------    lets automatisation <3  -------------------  #

# Chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Step 1  check internet speed
driver = webdriver.Chrome(options=chrome_options)
driver.get(google_docs)

time.sleep(7)

# input importat things
for index in range(len(all_addrs)):
# text address names
    address_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_inp.send_keys(addr_list[index])
# text price
    price_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_inp.send_keys(price_list[index])
# text link
    link_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_inp.send_keys(link_list[index])
# submit everything
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(3)
    retry = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    retry.click()
    time.sleep(2)
