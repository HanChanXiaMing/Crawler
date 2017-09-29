from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
cheshi = client['ceshi']    # 创建一个库
url_list = cheshi['url_list3']  # 创建一个表
url_host = 'http://communityaction.org.cn'

# spider 1
# 获取各类里的所有链接
def get_links_from(channel,pages):  # channel 是类的html   pages 是当前类的页数
    # http://communityaction.org.cn/page-9-2.html
    list_view = '{}-{}.html'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    time.sleep(3)   # 延迟时间
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('a.dwqa-title'):
        url = url_host + link.get('href')
        url_list.insert_one({'url':url})
        print(url)

get_links_from('http://communityaction.org.cn/page-100',1)

'''
http://communityaction.org.cn/question/265604.html
http://communityaction.org.cn/question/265573.html
http://communityaction.org.cn/question/265183.html
http://communityaction.org.cn/question/264842.html
http://communityaction.org.cn/question/264832.html
http://communityaction.org.cn/question/264452.html
http://communityaction.org.cn/question/264483.html
http://communityaction.org.cn/question/264476.html
http://communityaction.org.cn/question/264845.html
http://communityaction.org.cn/question/264847.html
http://communityaction.org.cn/question/264126.html
http://communityaction.org.cn/question/264444.html
http://communityaction.org.cn/question/263743.html
http://communityaction.org.cn/question/264115.html
http://communityaction.org.cn/question/263769.html
http://communityaction.org.cn/question/264123.html
http://communityaction.org.cn/question/264111.html
http://communityaction.org.cn/question/264121.html
http://communityaction.org.cn/question/263397.html
http://communityaction.org.cn/question/263050.html

'''