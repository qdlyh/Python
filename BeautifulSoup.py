from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
#获取a标签文字
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())

#获取单个a标签连接
a_node = soup.find('a',href='http://example.com/lacie')
print(a_node['href'])

#获取class段落文字
p_node=soup.find('p',class_='title')
print(p_node.get_text())


#获取class为sister段落所有
p_all = soup.find_all('a',class_= 'sister')
for p in p_all:
    print(p.name,p['href'],p.get_text())

#正则表达式
p_ill = soup.find('a',href=re.compile(r'ill'))
print(p_ill.get_text())