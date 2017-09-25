# -*- coding: UTF-8 -*-


from bs4 import BeautifulSoup
import requests
import time

url = 'http://qd.58.com/bijibendiannao/31238820212804x.shtml'

def get_links_from():
    #urls = []
    list_view = 'http://qd.58.com/bijiben/1/pn1/'
    # list_view = 'http://qd.58.com/bijiben/{}/pn1/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    #for link in soup.select('td.t t_b a.t'):
    #       urls.append(link.get('href').split('?')[0])
    #return urls
    #print(urls)

def get_item_info(url):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    data = {
        'title':soup.title.text,
        'data':soup.select('li.time')[0].get_text(),    # 时间
        'price':soup.select('span.price')[0].get_text(),    # 价格
        'quality':soup.select('ul > li:nth-of-type(2) > div.su_con > span')[0].get_text()   # 品质
    }
    print(data)

#get_item_info(url)
get_links_from()




'''
http://qd.58.com/bijibendiannao/0/
http://qd.58.com/bijiben/0/pn2/
http://qd.58.com/bijiben/1/
http://qd.58.com/bijiben/1/pn2/


'''
