import re
import urllib.request
import urllib.error
import urllib.parse
import sys
import io
import json
from bs4 import BeautifulSoup

disFileRoot = 'D:\\Gaokao\\2018\\语文\\'
srcFileRoot = "http://www.gaokao.com/e/20180428/5ae4096535b73"
# response = urllib.request.urlopen("http://www.gaokao.com/e/20180428/5ae4096535b73.shtml")
# text = response.read().decode("gb2312")
# soup = BeautifulSoup(text,"html.parser")

# img_src =  soup.find_all('img',{'alt':'2018年四川高考理综真题（图片版）'})
# i = 0
# for img in img_src:
#     try:
#         i+=1
#         print(img.get('src'))
#         distFile = open(disFileRoot + "语文" + str(i) + ".jpg", 'wb')
#         distFile.write((urllib.request.urlopen(img.get('src'))).read())
#         distFile.close()
#     except Exception as e:
#         print('error:' + e)

# 获取当前URL的所有下一页地址
def getNextPageURL(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode("gb2312")
    soup = BeautifulSoup(text, "html.parser")
    src=[]
    for div in soup.find_all('div', {'class': 'pages'}):
        # print(div)
        a = div.find_all('a')
        for tagA in a:
            src.append(tagA.get('href'))
            # print(tagA.get('href'))
    src.pop()
    src.pop()
    return src

def getImgSrc(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode("gb2312")
    soup = BeautifulSoup(text, "html.parser")
    imgSrcList = []
    img_src = soup.find_all('img', {'alt': '2018年四川高考理综真题（图片版）'})
    for src in img_src:
        imgSrc = src.get('src')
        imgSrcList.append(imgSrc)
    return imgSrcList

i = 0
srcList = getNextPageURL('http://www.gaokao.com/e/20180428/5ae4096535b73.shtml')
for src in srcList:
    imgSrc = ''
    if not src is None:
        imgSrc = getImgSrc(src)
    print(imgSrc)
    for img in imgSrc:
        try:
            i+=1
            # print(img.get('src'))
            distFile = open(disFileRoot + "语文" + str(i) + ".jpg", 'wb')
            distFile.write((urllib.request.urlopen(img)).read())
            distFile.close()
        except Exception as e:
            print('error:' + e)
# nextClassText = soup.find_all('div',{'class':'pages'})
# for div in nextClassText:
#     s = BeautifulSoup(value,'html.parser')
#     print(value)
    # print(value['href'])
# print(nextClass)
# nextHref = BeautifulSoup(nextClass,'html.parser')
# print(nextHref)
# value = nextHref.find_all('href')
# for i in value:
#     print(i)

