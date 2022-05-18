#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yiliyas
# Date: 2022.5.18

import re
from urllib import request

# 1.获取数据
def get_html(url):
    # https 模拟浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    req = request.Request(url,headers=headers)
    response=request.urlopen(req)
    content=response.read().decode('gb2312')
    return content

# 2.处理数据（设置匹配条件）
def get_url(content):
    # 根据地址不同，判断设置不同的匹配条件
    pattern = re.compile('<li><a href=\'(.*?)\'>(.*?)</a></li>',re.S)
    items = re.findall(pattern,content)
    return items

# 3.显示数据
def show_result(items):
    # 根据地址不同，判断设置不同的匹配条件
    for item in items:
        curl = item[0]
        cname = item[1]
        # 生成完整的链接地址
        curl = 'http://www.stats.gov.cn/tjsj/ndsj/'+str(iyear)+'/'+str(curl)
        strs = '|['+cname+']('+curl+')'
        # 显示链接信息
        print(strs)
        # 下载数据
        get_file(curl)

# 4.下载数据（写入文件）
def get_file(url):
    file_name = url.split('/')[-1]
    # 修改路径（文件名加入年份，避免重复）
    file_names='E:/download/'+str(iyear)+file_name
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

# 下载（2005~2021）
# 定义全局变量：iyear 历年
global iyear
#url = 'http://www.stats.gov.cn/tjsj/ndsj/2021/left.htm'
for iyear in range(2005,2021):
    url = 'http://www.stats.gov.cn/tjsj/ndsj/'+str(iyear)+'/left.htm'
    # 获取信息
    html = get_html(url)
    # 获取下载地址
    items = get_url(html)
    # 下载显示数据
    show_result(items)


