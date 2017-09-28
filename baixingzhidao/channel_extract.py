from bs4 import BeautifulSoup
import requests

start_url = 'http://communityaction.org.cn/'
url_host = 'http://communityaction.org.cn'

def get_channel_urls(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.sub-menu > li > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

#get_channel_urls(start_url)

channel_list = '''
    http://communityaction.org.cn/cat85.html
    http://communityaction.org.cn/cat86.html
    http://communityaction.org.cn/cat87.html
    http://communityaction.org.cn/cat88.html
    http://communityaction.org.cn/cat89.html
    http://communityaction.org.cn/cat90.html
    http://communityaction.org.cn/cat91.html
    http://communityaction.org.cn/cat92.html
    http://communityaction.org.cn/cat93.html
    http://communityaction.org.cn/cat94.html
    http://communityaction.org.cn/cat95.html
    http://communityaction.org.cn/cat96.html
    http://communityaction.org.cn/cat97.html
    http://communityaction.org.cn/cat98.html
    http://communityaction.org.cn/cat99.html
    http://communityaction.org.cn/cat23.html
    http://communityaction.org.cn/cat24.html
    http://communityaction.org.cn/cat25.html
    http://communityaction.org.cn/cat26.html
    http://communityaction.org.cn/cat27.html
    http://communityaction.org.cn/cat28.html
    http://communityaction.org.cn/cat29.html
    http://communityaction.org.cn/cat30.html
    http://communityaction.org.cn/cat31.html
    http://communityaction.org.cn/cat32.html
    http://communityaction.org.cn/cat33.html
    http://communityaction.org.cn/cat34.html
    http://communityaction.org.cn/cat35.html
    http://communityaction.org.cn/cat36.html
    http://communityaction.org.cn/cat37.html
    http://communityaction.org.cn/cat100.html
    http://communityaction.org.cn/cat101.html
    http://communityaction.org.cn/cat102.html
    http://communityaction.org.cn/cat103.html
    http://communityaction.org.cn/cat104.html
    http://communityaction.org.cn/cat105.html
    http://communityaction.org.cn/cat106.html
    http://communityaction.org.cn/cat107.html
    http://communityaction.org.cn/cat108.html
    http://communityaction.org.cn/cat109.html
    http://communityaction.org.cn/cat110.html
    http://communityaction.org.cn/cat111.html
    http://communityaction.org.cn/cat112.html
    http://communityaction.org.cn/cat55.html
    http://communityaction.org.cn/cat56.html
    http://communityaction.org.cn/cat57.html
    http://communityaction.org.cn/cat58.html
    http://communityaction.org.cn/cat59.html
    http://communityaction.org.cn/cat60.html
    http://communityaction.org.cn/cat61.html
    http://communityaction.org.cn/cat62.html
    http://communityaction.org.cn/cat63.html
    http://communityaction.org.cn/cat64.html
    http://communityaction.org.cn/cat65.html
    http://communityaction.org.cn/cat66.html
    http://communityaction.org.cn/cat67.html
    http://communityaction.org.cn/cat68.html
    http://communityaction.org.cn/cat69.html
    http://communityaction.org.cn/cat40.html
    http://communityaction.org.cn/cat41.html
    http://communityaction.org.cn/cat42.html
    http://communityaction.org.cn/cat43.html
    http://communityaction.org.cn/cat44.html
    http://communityaction.org.cn/cat45.html
    http://communityaction.org.cn/cat46.html
    http://communityaction.org.cn/cat47.html
    http://communityaction.org.cn/cat48.html
    http://communityaction.org.cn/cat49.html
    http://communityaction.org.cn/cat50.html
    http://communityaction.org.cn/cat51.html
    http://communityaction.org.cn/cat52.html
    http://communityaction.org.cn/cat53.html
    http://communityaction.org.cn/cat54.html
    http://communityaction.org.cn/cat120.html
    http://communityaction.org.cn/cat121.html
    http://communityaction.org.cn/cat122.html
    http://communityaction.org.cn/cat123.html
    http://communityaction.org.cn/cat124.html
    http://communityaction.org.cn/cat125.html
    http://communityaction.org.cn/cat126.html
    http://communityaction.org.cn/cat127.html
    http://communityaction.org.cn/cat128.html
    http://communityaction.org.cn/cat129.html
    http://communityaction.org.cn/cat130.html
    http://communityaction.org.cn/cat131.html
    http://communityaction.org.cn/cat132.html
    http://communityaction.org.cn/cat133.html
    http://communityaction.org.cn/cat134.html
    http://communityaction.org.cn/cat135.html
    http://communityaction.org.cn/cat136.html
    http://communityaction.org.cn/cat137.html
    http://communityaction.org.cn/cat138.html
    http://communityaction.org.cn/cat70.html
    http://communityaction.org.cn/cat71.html
    http://communityaction.org.cn/cat72.html
    http://communityaction.org.cn/cat73.html
    http://communityaction.org.cn/cat74.html
    http://communityaction.org.cn/cat75.html
    http://communityaction.org.cn/cat76.html
    http://communityaction.org.cn/cat77.html
    http://communityaction.org.cn/cat78.html
    http://communityaction.org.cn/cat79.html
    http://communityaction.org.cn/cat80.html
    http://communityaction.org.cn/cat81.html
    http://communityaction.org.cn/cat82.html
    http://communityaction.org.cn/cat83.html
    http://communityaction.org.cn/cat84.html
    http://communityaction.org.cn/cat38.html
    http://communityaction.org.cn/cat39.html
    http://communityaction.org.cn/cat13.html
    http://communityaction.org.cn/cat14.html
    http://communityaction.org.cn/cat15.html
    http://communityaction.org.cn/cat16.html
    http://communityaction.org.cn/cat17.html
    http://communityaction.org.cn/cat18.html
    http://communityaction.org.cn/cat19.html
    http://communityaction.org.cn/cat20.html
    http://communityaction.org.cn/cat21.html
    http://communityaction.org.cn/cat22.html
    http://communityaction.org.cn/cat113.html
    http://communityaction.org.cn/cat114.html
    http://communityaction.org.cn/cat115.html
    http://communityaction.org.cn/cat116.html
    http://communityaction.org.cn/cat117.html
    http://communityaction.org.cn/cat118.html
    http://communityaction.org.cn/cat119.html
'''
