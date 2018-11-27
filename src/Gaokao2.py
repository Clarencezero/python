import re
import urllib.request
import urllib.error
import urllib.parse
import sys
import io
import json
from bs4 import BeautifulSoup


# 通过根URL获取下一页
def getNextPageSrc(url):
    response = urllib.request.urlopen(url)
    htmlText = response.read().decode('gb2312')
    soupParse = BeautifulSoup(htmlText, 'html.parser')
    for divContent in soupParse.find_all('div', {'class', 'pages'}):
        aContent = divContent.find_all('a')
        nextPageSrc = aContent.pop().get('href')
        print(nextPageSrc)
        # for index, nextPage in enumerate(aContent):
        #     if index == len(aContent) - 1:
        #         if ()
        #         return nextPage.get('href')


nextPageSrc = getNextPageSrc('http://www.gaokao.com/e/20180428/5ae4096535b73_5.shtml')
print(nextPageSrc)
