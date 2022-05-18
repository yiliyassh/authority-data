# -*- coding:utf-8 -*-
# Author: yiliyas
# Date: 2022.5.18

from urllib import request
import re

# 工信数据
url = 'https://www.miit.gov.cn/gxsj/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
req = request.Request(url,headers=headers)
response=request.urlopen(req)
content=response.read().decode('utf-8-sig')

# 获得最新行业数据
pattern = re.compile('<p><a href="(.*?)".*?title="(.*?)">.*?</a><span>(.*?)</span></p>',re.S)
items = re.findall(pattern,content)
for item in items:
    url=item[0]
    uname=item[1]
    utime=item[2]
    url='https://www.miit.gov.cn'+url
    if str(url).find('yclgy')>-1:
        strs='|原材料工业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('zbgy')>-1:
        strs='|装备工业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('xfpgy')>-1:
        strs='|消费品工业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('txy')>-1:
        strs='|通信业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('dzxx')>-1:
        strs='|电子信息制造业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('rjy')>-1:
        strs='|软件业'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('hlw')>-1:
        strs='|互联网'+'|['+uname+']('+url+')|'+utime
        print(strs)
    if str(url).find('wlaq')>-1:
        strs='|网络安全'+'|['+uname+']('+url+')|'+utime
        print(strs)
