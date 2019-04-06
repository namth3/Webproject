from get_post_detail import get_post
from db_BaiViet import main_web
from connect import add_post
from db import post_collection



for i in range(1,2):
        n = str(i)
        link = "https://baodulich.com/viet-nam/page/"+n+"/"
        new_list = main_web(link)

        detail_link = []
        for link in new_list:
                
                url_c = link["link"]
                a = get_post(url_c)


                title = link["title"]
                img = a["image"]
                p = a["post"]
                # content = a["post"]
                add_post(title,img,p)
                
        