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
        content=response.read().decode('utf-8')
        return content
    except:
        content='test2022!'
        pass


# 2.处理数据（设置匹配条件）
def get_url(content):
    # 根据地址不同，判断设置不同的匹配条件（第一层，文件标题）
    pattern = re.compile('<td.*?><span.*?>.*?<a href="(.*?)".*?>(.*?)</a>.*?</td>.*?<td.*?><span.*?>(.*?)</span></td>',re.S)
    # 处理异常，忽略错误，继续执行
    try:
        items = re.findall(pattern,content)
        return items
    except:
        pass


def get_url2(content):
    # 根据地址不同，判断设置不同的匹配条件（第2层，文件下载地址）
    pattern = re.compile('<b>【全文下载】</b>.*?<a href="(.*?)".*?class=kxyj_text>(.*?)</a>',re.S)
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
    # 获取待下载文件的第一层地址：文件标题
    # 处理异常，忽略错误，继续执行
    try:
        for item in items:
            url = item[0]
            cname = item[1]
            cdate = item[2]
            url2 = 'http://www.caict.ac.cn/kxyj/qwfb/ztbg' + str(url).replace('./', '/')
            strs1 = '|[' + cname + '](' + url2 + ')' + '|' + cdate
            tsum = tsum + 1
            # print(strs1)
            # 获取待下载文件的第二层地址：文件下载地址
            html2 = get_html(url2)
            items2 = get_url2(html2)
            # 处理异常，忽略错误，继续执行
            try:
                for item2 in items2:
                    url3 = item2[0]
                    url3 = str(url3)
                    ss = url3[4:10]
                    url3 = 'http://www.caict.ac.cn/kxyj/qwfb/ztbg/' + ss + str(url3).replace('./', '/')
                    uname = item[1]
                    # markdown格式文本
                    strs2 = strs1 + '|[' + uname + '](' + url3 + ')'
                    print(strs2)
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
url = 'http://www.caict.ac.cn/kxyj/qwfb/ztbg/index.htm'
html = get_html(url)
items = get_url(html)
show_result(items)


# 下载历史数据
tsum = 0    #计数器
tsums = 0   #累加计数器
# 获得总页数（手动调整）
for i in range(1,12):
    url = 'http://www.caict.ac.cn/kxyj/qwfb/ztbg/index_'+str(i)+'.htm'
    # 获取信息
    html = get_html(url)
    # 获取下载地址
    items = get_url(html)
    # 下载显示数据
    show_result(items)
    # 计数器累加
    tsums = tsum + tsums
    psums = str(tsum)+'/'+str(tsums)
    print(psums)


# 统计总数
tsums = '总计： '+str(tsums)+' 个文件'
print(tsums)

