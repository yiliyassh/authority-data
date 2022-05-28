#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yiliyas
# Date: 2022.5.26


import re
from urllib import request


# 1.获取数据
def get_html(url):
    # https 模拟浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    req = request.Request(url,headers=headers)
    response=request.urlopen(req)
    # 根据实际地址修改字符集
    content=response.read().decode('utf-8')
    return content

# 2.处理数据（设置匹配条件）
def get_url(content):
    # 根据地址不同，判断设置不同的匹配条件
    pattern = re.compile('<li><a.*?data-area="(.*?)">(.*?)</a></li>.*?<li><a href="(.*?)".*?>(.*?)</a></li>',re.S)
    items = re.findall(pattern,content)
    return items


# 3.显示数据
def show_result(items):
    # 根据地址不同，判断设置不同的匹配条件
    n=0
    for item in items:
        curl = item[0]
        cname = item[1]
        curl2 = item[2]
        cname2 = item[3]
        # 生成完整的链接地址
        if str(cname).find('pdf')>-1:
            n=n+1
            curl = 'http://www.mofcom.gov.cn/dl/gbdqzn/upload/'+str(curl)+'.pdf'
            # markdown格式
            cname=str(cname).replace('pdf','')
            #strs = '|'+str(n)+'.|['+cname+']('+curl+')|['+cname2+']('+curl2+')'
            strs = '|['+cname+']('+curl+')|['+cname2+']('+curl2+')'
            # 显示链接信息
            print(strs)
            # 下载数据
            get_file(curl)


# 4.下载数据（写入文件）
def get_file(url):
    file_name = url.split('/')[-1]
    # 设置下载路径（根据实际情况修改）
    file_names='E:/download/'+file_name
    print(file_names)
    req = request.Request(url)
    u = request.urlopen(req)
    f = open(file_names, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_names)


# 下载最新页
url = 'http://fec.mofcom.gov.cn/article/gbdqzn/'
html = get_html(url)
items = get_url(html)
show_result(items)

