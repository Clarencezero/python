#coding:utf-8
import json
from bs4 import BeautifulSoup
import requests
import csv
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers = headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_ = "mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

# with open('qiye.json', 'wb') as fp:
#     # json.dump(content, fp = fp, indent=4)
#     fp.write((json.dumps(content).encode('utf-8')))
#     fp.close()
header = ['ID','USERNAME','PASSWORD']
wors = [(1,'zhangwenfeng','520'), (2, 'zhangwenfeng', '520')]
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(wors)