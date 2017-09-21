#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
url_saves = ''

# 伪造登陆信息
headers = {
    'User-Agent':'',
    'Cookie':''
}
def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('')    # 标题
    imgs = soup.select('')      # 图片
    cates = soup.select('')     # 分类

    for title,img,cate in zip(titles,imgs,cates):
        data = {
            'title' :titles.get_text(),
            'img'   :imgs.get(),
            'cate'  :list(cate.stripped_strings)
        }
        print(data0


def get_favs(url,data=None):
            wb_data = requests.get(url,headers=headers)
            soup    = BeautifulSoup(wb_data.text,'lxml')
            titles  = soup.select('')
            imgs    = soup.select('')
            metas   = soup.select('')

            if data == None:
                for title,img,meta in zip(titles,imgs,metas):
                        data = {
                            'title':title.get_text(),
                            'img':img.get()
                            'meta':list(meta.stripped_strings)
                        }
                        print(data)
