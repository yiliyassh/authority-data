## 全国年度统计公报 :+1::+1::+1:
http://www.stats.gov.cn/tjsj/tjgb/ndtjgb/
- [2021年国民经济和社会发展统计公报](http://www.stats.gov.cn/tjsj/zxfb/202202/t20220227_1827960.html)

### 下载统计公报 :+1::+1::+1:
#### 2013~2021年
```
wget http://www.stats.gov.cn/tjsj/tjgb/ndtjgb/index.html|
xargs cat index.html |
grep -E "t202|t201[4-9]"|
grep "cont_tit"|
awk -F '"' '{print "http://www.stats.gov.cn/"$2}'|
xargs wget
```
#### 2001~2012年
```
wget http://www.stats.gov.cn/tjsj/tjgb/ndtjgb/index.html|
xargs cat index.html |
grep -E "t201[0-3]|t200[0-9]"|
grep "cont_tit"|
awk -F '"' '{print "http://www.stats.gov.cn/tjsj/tjgb/ndtjgb"$2}'|
xargs wget
```
#### 1982~2000年
```
wget http://www.stats.gov.cn/tjsj/tjgb/ndtjgb./index_1.html|
xargs cat index_1.html |
grep "t2002"|
grep "cont_tit"|
awk -F '"' '{print "http://www.stats.gov.cn/tjsj/tjgb/ndtjgb"$2}'|
xargs wget
```
#### 1978~1981年
```
wget http://www.stats.gov.cn/tjsj/tjgb/ndtjgb./index_2.html|
xargs cat index_2.html|
grep "t2002"| 
grep "cont_tit"|
awk -F '"' '{print "http://www.stats.gov.cn/tjsj/tjgb/ndtjgb"$2}'|
xargs wget
```