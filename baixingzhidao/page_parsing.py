from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017) # 激活
cheshi = client['cheshi']    # 创建一个库
url_list = cheshi['url_list3']  
item_info = cheshi['item_info4']
url_host = 'http://communityaction.org.cn'

# spider 1
# 获取各类里的所有链接
def get_links_from(channel,pages):  # channel 是类的html   pages 是当前类的页数
    # http://communityaction.org.cn/page-9-2.html
    list_view = '{}-{}.html'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    time.sleep(3)   # 延迟时间
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('footer','dwqa-footer-meta'):    # 判断当前页有无信息
        for link in soup.select('a.dwqa-title'):
            url = url_host + link.get('href')
            url_list.insert_one({'url':url})
            print(url)
    else:
        pass
        # Nothing !

# spider 2
# 获取各页里的信息
def get_item_info(url):
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('h1.entry-title')               # 标题
        datas = soup.select('div.dwqa-meta span.dwqa-date')  # 提问时间
        Answer_times = soup.select('header div span.dwqa-date a')        # 未被采用回答时间
        if soup.find('div','acceptAnswer'):                  # 回答是否被采用
            best_times = soup.select('div.acceptAnswer div span:nth-of-type(2)') # 采用回答时间
        else:
            best_times = None
        print(titles,datas,Answer_times,best_times)
        #！ Answer_times 输出时只有一个 未解决 75-78
        #for title,data,Answer_time,best_time in zip(titles,datas,Answer_times,best_times):
        #    text = {
        #        'tiele' :title.get_text(),
        #        'data'  :data.get_text(),
        #        'Answer_time':Answer_time.get_text(),
        #        'best_time' :best_time.get_text()
        #    }
        #    print(text)
#get_links_from('http://communityaction.org.cn/page-100',1)
get_item_info('http://communityaction.org.cn/question/265922.html')
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

        # answer- > header:nth-child(1) > div > span.dwqa-date > a
        # answer- > header:nth-child(3) > div > span.dwqa-date > a
        # answer- > header:nth-child(5) > div > span.dwqa-date > a
        # answer- > header:nth-child(7) > div > span.dwqa-date > a
        #answer- > div.acceptAnswer > div > span.accept
'''
