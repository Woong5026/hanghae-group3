from bs4 import BeautifulSoup
import requests

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.PetHotel

hotel_1_url='https://www.goodchoice.kr/product/detail?ano=66997'

raw=requests.get(hotel_1_url)

soup=BeautifulSoup(raw.text,'html.parser')

box= soup.find('section',{'class':'default_info'})

contents=box.find_all({'section','h3','li'})
# print(contents)

for content in contents:
    if content.text !='사장님 한마디':
        info=content.text

        doc={
            'hotelinfo': info
        }

        db.info.insert_one(doc)

        print(info)

