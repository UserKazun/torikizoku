"""指定した店舗の待ち人数やweb予約可能かを取得。
可能な場合は予約する
"""

import re
import requests
from bs4 import BeautifulSoup


class Torikizoku(object):
    def __init__(self):
        self.get_toriki_title()
        self.shop_area = input()

    def get_toriki_title(self):
        """とりきのセールス文句みたいなものを出力"""
        self.html = requests.get("https://www.torikizoku.co.jp")
        self.soup = BeautifulSoup(self.html.text, 'html.parser')
        titles = self.soup.find_all('title')
        print(titles[0].text)

    def get_shop_area(self):
        """入力されたエリアを元に店名,住所,TEL,web予約可能かを出力"""
        session = requests.session()
        post = session.post("https://www.torikizoku.co.jp/searches/free", \
                            data={"q": self.shop_area})
        soup = BeautifulSoup(post.text, 'html.parser')
        item_tags = soup.find_all(class_="shoplist")

        for item_tag in item_tags:
            # shop_link = item_tag.a.get('href')
            shop_name = item_tag.get_text()
            # html = requests.get("https://www.torikizoku.co.jp/searches/free"+shop_link)
            shop_names = re.split('[\n]', shop_name)
            shop_names_split = [space for space in shop_names if space]
            print(shop_names_split)

torikizokiu = Torikizoku()

torikizokiu.get_shop_area()