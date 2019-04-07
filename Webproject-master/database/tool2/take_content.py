from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

def web_content(link):
    url = (link)
    content = urlopen(url).read()
    pageContent = content.decode("utf8")


    soup_c = BeautifulSoup(pageContent, "html.parser")
    content = soup_c.find("div",{"class":"entry-content"})
    title = soup_c.find("div",{"id":"content"})

    images = []
    for img in content.find_all('img'):
        images.append(img.get('src'))


    def find_post(a,b):
        post =""
        for tag in b.find_all(a):
            if tag.img:
                x = 0
            else:
                post += "\n" + tag.getText()
        return post

    title1 = find_post('a',title)
    post = find_post('p',soup_c)
    result = {
        "title": title1,
        "post": post,
        "img": images,
    }

    return result


