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
    # 根据实际地址修改字符集
    content=response.read().decode('utf-8')
    return content

# 2.处理数据（设置匹配条件）
def get_url(content):
    # 根据地址不同，判断设置不同的匹配条件
    pattern = re.compile('<a href="(.*?)".*?><span.*?><img.*?><font.*?>(.*?)</font><font.*?>(.*?)</font></span></a>',re.S)
    items = re.findall(pattern,content)
    return items

# 3.显示数据
def show_result(items):
    # 根据地址不同，判断设置不同的匹配条件
    for item in items:
        curl = item[0]
        cname = item[1]
        # 生成完整的链接地址
        #http://www.stats.gov.cn/sj/zxfb/201602/t20160229_1323991.html
        if str(cname).find('年')>-1:
            cyear = str(cname).replace('年','')
            iyear = int(cyear)
        if iyear>2012:
            curl = 'http://www.stats.gov.cn'+str(curl)
        if iyear>=1978 and iyear<=2012:
            curl=str(curl).replace('./','/')
            curl = 'http://www.stats.gov.cn/sj/tjgb/ndtjgb'+str(curl)
        strs = '|['+cname+']('+curl+')'
        # 显示链接信息
        print(strs)
        # 下载数据
        get_file(curl)

# 4.下载数据（写入文件）
def get_file(url):
    file_name = url.split('/')[-1]
    # 修改路径
    file_names='E:/download/'+file_name
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
    print ("Sucessful to download" + " " + file_name)

# 下载（2013~2021）
# 2022-2021年

url = 'http://www.stats.gov.cn/sj/tjgb/ndtjgb/qgndtjgb/index.html'
# 1983-2001年
#url = 'http://www.stats.gov.cn/sj/tjgb/ndtjgb/index_1.html'
#
#url = 'http://www.stats.gov.cn/sj/tjgb/ndtjgb/index_2.html'

# 获取信息
html = get_html(url)
# 获取下载地址
items = get_url(html)
# 下载显示数据
show_result(items)

