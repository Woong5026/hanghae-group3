import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.PetHotel

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.goodchoice.kr/product/recommend/153',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 호텔 정보
# 이름 : #poduct_list_area > li:nth-child(2) > a > div > div.name > strong
# 평점 : #poduct_list_area > li:nth-child(2) > a > div > div.name > p.score > em
# 가격 : #poduct_list_area > li:nth-child(23) > a > div > div.price > p > b
# 위치 : #poduct_list_area > li:nth-child(23) > a > div > div.name > p:nth-child(4)
# 이미지 url : #poduct_list_area > li:nth-child(23) > a > p > img
#poduct_list_area > li:nth-child(2) > a > div > div.name > strong
#poduct_list_area > ul > li:nth-child(1) > a > div > div.name > p:nth-child(3)
#poduct_list_area > ul > li:nth-child(1) > a > div > div.name > strong
#poduct_list_area > ul > li:nth-child(1) > a > div > div.name
lis = soup.select('#poduct_list_area > ul > li')
i = 0
for li in lis:
        hotel_name = li.select_one('a > div > div.name > strong').text
        hotel_price = li.select_one('a > div > div.price > p > b').text
        hotel_location = li.select_one('a > div > div.name > p:nth-child(3)').text.strip()
        hotel_imageUrl = li.select_one('a > p > img')['data-original']


        doc = {
            'checkId': i,
            'name': hotel_name,
            'location': hotel_location,
            'price': hotel_price,
            'imageUrl': hotel_imageUrl,
        }
        db.list.insert_one(doc)
        print(hotel_name, hotel_location, hotel_price, hotel_imageUrl,i)
        i=i+1
        if i==10 :
            break;
