from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

def take_link(link):
    url = (link)
    content = urlopen(url).read()
    pageContent = content.decode("utf8")

    soup = BeautifulSoup(pageContent, "html.parser")
    paging = soup.find("div",{"class":"archive-postlist"})


    list_link = []
    for ai in paging:
        a = ai.a
        b = a["href"]
        list_link.append(b)

    return list_link