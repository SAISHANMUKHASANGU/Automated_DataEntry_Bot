import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

URL="https://appbrewery.github.io/Zillow-Clone/"

response=requests.get(url=URL)
html_code=response.text
prices_unformated=[]
prices_formated=[]
addresses_formated=[]
links=[]

soup=BeautifulSoup(html_code,"html.parser")
prices_extract=soup.find_all(name='span',class_="PropertyCardWrapper__StyledPriceLine")
for price in prices_extract:
    a=price.getText()
    prices_unformated.append(a)
for price in prices_unformated:
    if "+" in price:
        a=price.split("+")
        prices_formated.append(a[0])
    else:
        a=price.split("/")
        prices_formated.append(a[0])

addresses_extract=soup.find_all(name='address')
addresses_formated = [address.get_text().replace(" | ", " ").strip() for address in addresses_extract]

link_extract=soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor")
for link in link_extract:
    a=link["href"]
    links.append(a)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome()

for i in range(0,len(prices_formated)):
    driver.get("https://forms.gle/w8etTEWvxCSttgLR8")
    time.sleep(3)
    address_input=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses_formated[i])
    price_input=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices_formated[i])
    link_input=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[i])
    submit=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

driver.quit()



