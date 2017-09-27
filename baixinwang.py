from bs4 import BeautifulSoup
import requests
import time

#url = 'http://jimo.baixing.com/ershouqiche/a1184041036.html'

# 获取一页的网页信息
def get_links_from():
    urls = []
    list_view = 'http://qingdao.baixing.com/ershouqiche/'
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    htmls = soup.select('li > div > div.media-body-title > a.ad-title')
    for link in htmls:
        urls.append(link.get('href').split('?')[0])
    print (soup)

def get_item_info():

    urls = get_links_from()
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data = {
            'title':soup.title.text,
            # 'data':soup.select('li.time')[0].get_text(),    # 时间
            'price':soup.select('span.price')[0].get_text(),    # 价格
            #'quality':soup.select('ul > li:nth-of-type(2) > div.su_con > span')[0].get_text()   # 品质
        }
        print(data)
        time.sleep(2) # 延迟时间

get_item_info()
#get_links_from()
