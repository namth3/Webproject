def main_web(link):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    import json

    url = (link)
    content = urlopen(url).read()
    pageContent = content.decode("utf8")
    # conn = urlopen(req)

    soup = BeautifulSoup(pageContent, "html.parser")
    paging = soup.find_all("h2", {"class": "post-box-title"})
    # ul = paging.find("ul")
    # li_list = ul.find_all('li')


    new_list = []
    for link_p in paging:
        a = link_p.a
        link = a["href"]
        title = a.string
        news = {
            "link":link,
            "title":title
        }
        new_list.append(news)
    
    return new_list








# new_list = []
# for i in paging:    
#     h2 = paging.h2
#     a = h2.a

#     link = url + a["href"]
#     new_list.append(link)

# print(new_list)
# print(paging)
# print(content)

    #looping through paging
# for i in range(1,last_page):
#     print (req+str(i))

# url_news = news.find('a',{'class':'article__link'}).get('href')


# raw_data=conn.read()
# page_content=raw_data.decode("utf8")


# soup=BeautifulSoup(page_content,"html.parser")
# div = soup.find("div","post-listing archive-box masonry-grid isotope")
# # post = div.find("div","post-listing archive-box masonry-grid isotope")
# p = div.find_all('article')


# new_list = []
# for art in p:
#     h2 = p.h2
#     a = h2.a
#     link = req + a["href"]
#     # title = a.string
#     news = {
#         "link":link,
#         # "title":title
#     }
#     new_list.append(news)
#     print(new_list)
# # y = json.loads(page_content)



