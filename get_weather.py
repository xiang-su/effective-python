"""
This is a python-demo to get country's weather in five days
"""
import requests
from bs4 import BeautifulSoup

URL = 'http://www.weather.com.cn/weather/101190101.shtml'
r = requests.get(URL)
r.encoding = 'utf-8'
bs = BeautifulSoup(r.text, 'lxml')
weather_list = bs.findAll("li", {'class': {'sky skyid lv3 on',
                                          'sky skyid lv3', 'sky skyid lv2', 'sky skyid lv1'}})
print('NanJing weather:\n')
for i in weather_list:
    print(i.get_text().replace('\n', ' '))
weather_list = bs.findAll()
