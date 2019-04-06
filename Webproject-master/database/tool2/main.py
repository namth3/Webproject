from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
from take_content import web_content
from main_link import take_link
from db import db_connect_DiaDiem,client
from DiaDiem import *
from pymongo import MongoClient


for place in TinhThanh:
    for place_detail in place:
        if place_detail == "MienBac":
            db = client.MienBac
        elif place_detail == "MienTrung":
            db = client.MienTrung
        elif place_detail == "MienNam":
            db = client.MienNam
        else:
            n = place_detail
            main_n = n.replace(" ","+")
            db_connect = n.replace(" ","")
            postcollection = db[db_connect]
            for i in range(1,3):
                s = str(i)
                uri_link_main = "https://www.ivivu.com/blog/page/"+s+"/?s="+n
                link_taken = take_link(uri_link_main)
                for link in link_taken:
                    result = web_content(link)
                    postcollection.insert_one(result)

            
            
