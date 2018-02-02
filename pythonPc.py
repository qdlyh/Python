#coding=utf-8
import urllib
import urllib.request
import re

def download_page(url):
    request = urllib.request.Request(url)   #构建请求
    reponse = urllib.request.urlopen(url)   #获取服务器响应
    data = reponse.read()
    return data

def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern,repr(html))
    num = 0
    for img in get_img:
        image = download_page(img)          #获取图片
        with open('img/%s.jpg'%num,'wb')as fp:  #存放到Img文件夹
            fp.write(image)
            num += 1
            print('正在下载第%s张图片'%num)
    print('获取图片成功')
    return

# url = 'http://pic.yesky.com/c/6_243.shtml'
url = 'http://www.qiumeimei.com/'
html = download_page(url)                   #获取网页
get_image(html)