from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as Ureq  
import numpy as np 
#Downloads raw html
#Parses html
def get_soup(Link):
    my_url = Link
    UClient = Ureq(my_url)
    raw_html = UClient.read()
    UClient.close()
    page_soup = soup(raw_html,"html.parser")
    #Downloads raw html
    #Parses html
    return(page_soup)


def Find_Price(soupage):
    price_list= []
    price = (soupage.findAll("li",{"class":"price-current"}))
    counter = 0
    fail_counter = 0 
    for item in price:
        dollars = item.strong
        cents = item.sup 
        try:
            dollars = dollars.get_text()
            cents = cents.get_text()
            Total = dollars + cents
            price_list.append(Total)
            counter += 1        
        except AttributeError:
            fail_counter += 1
            pass

    return(price_list,counter,"Fails",fail_counter)

def Find_Item_Name(soupage):
    title_list = []
    Title_container = soupage.findAll("a",{"class":"item-title"})
    counter = 0
    for item in Title_container:
        title_list.append(item.text)
        counter += 1
    return(title_list,counter)

def Find_Shipping(soupage):
    shipping_list = []
    Shipping_Container = soupage.findAll("li",{"class":"price-ship"})
    for item in Shipping_Container:
        print(item.get_text().strip())


print(Find_Shipping(get_soup("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card")))
print(Find_Item_Name(get_soup("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card")))
print(Find_Price(get_soup("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card")))
