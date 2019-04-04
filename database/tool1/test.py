from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

n = str(3)
url = ("https://baodulich.com/viet-nam/page/2/")
content = urlopen(url).read()
pageContent = content.decode("utf8")
    # conn = urlopen(req)

soup = BeautifulSoup(pageContent, "html.parser")
paging = soup.find_all("h2", {"class": "post-box-title"})
# ul = paging.find("ul")
# li_list = ul.find_all('li')


new_list = []
for link in paging:
    a = link.a
    link = a["href"]
    title = a.string
    news = {
    "link":link,
    "title":title
    }
    new_list.append(news)
print(new_list)
# # print(soup)
# print(paging)