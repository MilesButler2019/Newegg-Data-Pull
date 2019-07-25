from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
#Spoofs the User-Agent in order to get around the 403 error
def SpoofandSoup(Link):
    myUrl = Link
    req = Request(myUrl,data=None, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})
    uClient = uReq(req)
    raw_html = uClient.read()
    page_soup = soup(raw_html,"html.parser")
    return(page_soup)

def Get_Top_Artists(soupage):
    Artists_List = []
    Artists_container = (soupage.findAll("div",{"class","chart-list-item__artist"}))
    for artist in Artists_container:
        Artists_List.append(artist.text.strip())
    return(Artists_List)

def Get_Top_Songs(soupage):
    Songs_List = []
    Songs_container = (soupage.findAll("div",{"class","chart-list-item__title"}))
    for song in Songs_container:
        Songs_List.append(song.text.strip())
    return(Songs_List)       

    
#print(Get_Top_Artists(SpoofandSoup("https://www.billboard.com/charts/hot-100")))
print(Get_Top_Songs(SpoofandSoup("https://www.billboard.com/charts/hot-100")))
