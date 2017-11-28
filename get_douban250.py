# -*- coding:utf-8 -*-
import re
import sys
import time

import requests
from bs4 import BeautifulSoup


def get_html_text(url, start_arg):
    try:
        if start_arg == 0:
            kw = {}
        else:
            kw = {'start': start_arg, 'filter': ''}
        r = requests.get(url, params=kw, headers={'User-Agent': 'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed!")


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # 找到第一个class属性值为grid_view的ol标签
    movie_list = soup.find('ol', attrs={'class': 'grid_view'})
    for movieLi in movie_list.find_all('li'):  # 找到所有li标签
        data = []
        # 得到电影名字
        # 找到第一个class属性值为hd的div标签
        movie_hd = movieLi.find('div', attrs={'class': 'hd'})
        # 找到第一个class属性值为title的span标签
        movie_name = movie_hd.find('span', attrs={'class': 'title'}).getText()
        # 也可使用.string方法
        data.append(movie_name)

        # 得到电影的评分
        movie_score = movieLi.find(
            'span', attrs={'class': 'rating_num'}).getText()
        data.append(movie_score)

        # 得到电影的评价人数
        movie_eval = movieLi.find('div', attrs={'class': 'star'})
        movie_eval_num = re.findall(r'\d+', str(movie_eval))[-1]
        data.append(movie_eval_num)

        # 得到电影的短评
        movie_quote = movieLi.find('span', attrs={'class': 'inq'})
        if movie_quote:
            data.append(movie_quote.getText())
        else:
            data.append("无")

        print(outputMode.format(data[0], data[1],
                                data[2], data[3], chr(12288)))


# 将输出重定向到txt文件
output = sys.stdout
outputFile = open("moviedata.txt", 'w', encoding='utf-8')
sys.stdout = outputFile

outputMode = "{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"
print(outputMode.format('电影名称', '评分', '评论人数', '短评', chr(12288)))
basicUrl = 'https://movie.douban.com/top250'
k = 0
while k <= 225:
    html = get_html_text(basicUrl, k)
    time.sleep(2)
    k += 25
    get_data(html)

outputFile.close()
sys.stdout = output
