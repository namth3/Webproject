

def get_post(link):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    import json
    url = (link)
    content = urlopen(url).read()
    pageContent = content.decode("utf8")


    soup_c = BeautifulSoup(pageContent, "html.parser")
    paging_c = soup_c.find("div",{"class":"entry"})

    #LẤY LINK HÌNH ẢNH
    images = []
    for img in paging_c.find_all('img'):
        images.append(img.get('src'))

    #LẤY TEXT CỦA WEBSITE
    post = ""
    for tag in soup_c.find_all('p'):
        if tag.img:
           x = 0
        else:
            post += "\n" + tag.getText()

    dic = {'post': post,
    'image':images
    }


    return dic