from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup as bs

main_url = 'http://v.qq.com/movie/'


def get_url(main_url):
    index = requests.get(main_url).content
    soup = bs(index, 'lxml')
    # print(soup)
    item = soup.find(
        'div', {'class': 'mod_figures mod_figure_v mod_figure_v_175'})
    itemList = item.findAll('li', {'class': 'list_item'})
    urls = [i.strong.a.attrs['href'] for i in itemList]
    return urls


def get_detail(url):
    index = requests.get(url).content
    soup = bs(index, 'lxml')

    name = soup.head.title.string.split('_')[0]
    print('电影名称：', name)
    time = soup.head.find('meta', {'itemprop': 'uploadDate'}).attrs['content']
    print('上映时间：', time)
    clicks = soup.find('em', {'id': 'mod_cover_playnum'}).string
    print('播放量：', clicks)
    try:
        score = soup.find('div', {'class': 'douban_score'}).span.string
    except AttributeError as a:
        score = '无评分'
    print('豆瓣评分：', score)
    director = soup.find('a', {'_stat': 'desc:director'}).string
    print('导演：', director)
    actors = soup.findAll('a', {'_stat': 'desc:actor'})
    actor = [i.string for i in actors]
    print('主演：', ','.join(actor))
    description = soup.head.find(
        'meta', {'name': 'description'}).attrs['content']
    print('电影简介：', description)

    print()


urls = get_url(main_url)

# 多线程
tpool = ThreadPool(15)
url = tpool.map(get_detail, urls)
