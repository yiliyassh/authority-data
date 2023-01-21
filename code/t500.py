#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yiliyas
# Date: 2022.5.19

import re
from urllib import request


# 1.获取数据
def get_html(url):
    # https 模拟浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    req = request.Request(url,headers=headers)
    # 处理异常，忽略错误，继续执行
    try:
        response=request.urlopen(req)
        # 设置编码
        content=response.read().decode('utf-8-sig')
        return content
    except:
        content='test2022!'
        pass


# 2.处理数据（设置匹配条件）
def get_url(content):
    # 根据地址不同，判断设置不同的匹配条件（第一层，文件标题）
    pattern = re.compile('<div class="swiper-slide">.*?<a href="(.*?)" data-year=".*?">(.*?)</a>.*?</div>',re.S)
    # 处理异常，忽略错误，继续执行
    try:
        items = re.findall(pattern,content)
        return items
    except:
        pass


def get_url2(content,ctype,iyear):
    # 根据地址不同，判断设置不同的匹配条件（第2层，文件下载地址）
    # 不同年度数据格式有差异，匹配规则不同
    #pattern = re.compile('<tr>\n<td>(.*?)</td>\n<td><a.*?>(.*?)</a></td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td.*?><span>.*?</span></td></tr>',re.S)
    cyear = str(iyear)
    # 英文年度榜
    # 5列
    if ctype=='en' and cyear in(2020,2021,2022):
        pattern=re.compile('<tr>\n<td>(.*?)</td>\n<td><a.*?>(.*?)</a></td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td.*?><span>.*?</span></td></tr>',re.S)
    # 6列
    if ctype=='en' and cyear in(2015,2018,2019):
        pattern = re.compile('<tr>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td><a.*?>(.*?)</a>.*?</td>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td>(.*?)</td></tr>',re.S)
    # 6列
    if ctype=='en' and cyear in(2014,2016,2017):
        pattern = re.compile('<tr><td>(.*?)</td><td>(.*?)</td><td><a.*?>(.*?)</a>.*?</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',re.S)
    # 6列
    if ctype=='en' and cyear == 2013:
        pattern = re.compile('<tr>\n.*?<td>(.*?)</td>\n.*?<td>(.*?)</td>\n.*?<td><a.*?>(.*?)</a>.*?</td>\n.*?<td>(.*?)</td>\n.*?<td>(.*?)</td>\n.*?<td>(.*?)</td>\n.*?</tr>',re.S)
    # 6列
    if ctype=='en' and cyear == 2012:
        pattern = re.compile('<tr><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?><a.*?>(.*?)</a>.*?</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td></tr>',re.S)
    # 6列
    if ctype=='en' and cyear==2011:
        pattern = re.compile('<tr>\n<td.*?>(.*?)</td>\n<td.*?>(.*?)</td>\n<td.*?><a.*?>(.*?)</a></td>\n<td.*?>(.*?)</td>\n<td.*?>(.*?)</td>\n<td.*?>(.*?)</td></tr>',re.S)
    # 5列
    if ctype=='en' and cyear==2010:
        pattern = re.compile('<tr>\n<td>(.*?)</td>\n<td>(.*?)</td>\n<td><a.*?>(.*?)</a></td>\n<td>(.*?)</td>\n<td>(.*?)</td></tr>',re.S)
    # 处理异常，忽略错误，继续执行
    try:
        items = re.findall(pattern,content)
        return items
    except:
        pass


# 3.显示数据
def show_result(items):
    # 根据地址不同，判断设置不同的匹配条件
    # 计数器
    global tsum
    tsum = 0
    # 获取待下载数据列表
    # 处理异常，忽略错误，继续执行
    try:
        for item in items:
            url=item[0]
            uname=item[1]
            strs=uname+'|'+url
            print(strs)
            # 获取载数据：文件下载地址（不同年度数据格式有差异，匹配规则不同）
            ctype = 'en'
            iyear = int(uname)
            html2 = get_html(url)
            items2 = get_url2(html2,ctype,iyear)
            # 处理异常，忽略错误，继续执行
            try:
                for item2 in items2:
                    c1=item2[0]
                    c2=item2[1]
                    c3=item2[2]
                    c4=item2[3]
                    c5=item2[4]
                    # markdown 表格格式
                    # if ctype=='cn':
                    cstr='|'+c1+'|'+c2+'|'+c3+'|'+c4+'|'+c5
                    print(cstr)
            except:
                pass
    except:
        pass


# 4.下载数据（写入文件）
def get_file(url):
    file_name = url.split('/')[-1]
    # 设置下载路径（根据实际情况修改）
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
    print ("Sucessful to download" + " " + file_names)


# 下载最新数据
# 《财富》世界500强排行榜
#url = 'https://www.fortunechina.com/fortune500/index.htm'
url = 'https://www.fortunechina.com/fortune500/c/2022-08/03/content_415683.htm'
# 《财富》中国500强排行榜
#url = 'https://www.fortunechina.com/fortune500/node_4302.htm'

html = get_html(url)
items = get_url(html)
show_result(items)

