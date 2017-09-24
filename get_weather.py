"""
This is a python-demo to get contry's weather in five days
"""
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = 'http://www.weather.com.cn/weather/101190101.shtml'
BS = BeautifulSoup(urlopen(URL), 'lxml')
WEATHERLIST = BS.findAll("li", {'class': {'sky skyid lv3 on',
                                          'sky skyid lv3', 'sky skyid lv2', 'sky skyid lv1'}})
print('NanJing weather:\n')
for i in WEATHERLIST:
    print(i.get_text().replace('\n', ' '))
WEATHERLIST = BS.findAll()
