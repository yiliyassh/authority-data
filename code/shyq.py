#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yiliyas
# date: 2022.4.24

from urllib import request
import re

# 上海市商业联合会抗疫保供产销对接信息平台生活物资供应名录（json格式数据）类别统计
url = 'https://c.kdcer.com/sh_keep_supply/home/categories'
req = request.Request(url)
response=request.urlopen(req)
content=response.read().decode('utf-8-sig')

# 获得类型id,类别，企业名
pattern = re.compile('"name":"(.*?)",.*?,"count":(.*?)}',re.S)
items = re.findall(pattern,content)
m=0
for item in items:
    m = m+1
    cname=item[0]
    cnum=item[1]
    # 获得全部企业——总数
    if str(cname).find("全部企业")>-1:
        nums = int(cnum)
    # 输入markdown格式
    strs='|'+cname+'|'+str(cnum)
    print(strs)

# 打印markdown表头
title2='\n|序号|类型|点击(详细工商信息)|\n'+'|:----|:----|:----|'
print(title2)
n=0
# 获得总页数（每页20个）
m = int(nums/20)+1
for i in range(1,nums):
    url = 'https://c.kdcer.com/sh_keep_supply/home/enterprises?categoryId=-1&keyword=&page='+str(i)+'&limit=20'
    req = request.Request(url)
    response=request.urlopen(req)
    content=response.read().decode('utf-8-sig')
    # 获得类型id,类别，企业名
    pattern = re.compile('"name":"(.*?)",".*?,"categoryName":"(.*?)"',re.S)
    items = re.findall(pattern,content)
    for item in items:
        n=n+1
        cname=item[0]
        cgname=item[1]
        strs='|'+str(n)+'|'+cgname+'|'+cname
        print(strs)

