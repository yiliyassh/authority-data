-  [**返回**](../README.md)  | [**下载**](../data/data.md)  
> **shell命令一句话爬虫**  

- 下载第39~49次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index.htm|
cat index.htm |
grep "次"|
grep pdf|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|
sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|
sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第34~37次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_1.htm|
cat index_1.htm |
grep "次"|
grep pdf|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|
sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|
sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第33次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_2.htm|
cat index_2.htm |
grep "次"|
grep pdf|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第26~29次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_3.htm|
cat index_3.htm |
grep "次"|
grep pdf|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|
sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|
sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第22~25次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_4.htm|
cat index_4.htm |
grep "次"|
grep -E "pdf|rar|doc"|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|
sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|
sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第8~21次《中国互联网络发展状况统计报告》
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_5.htm|
cat index_5.htm |
cat index_5.htm |
grep "次"|
grep -E "pdf|rar|doc"|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|
sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|
sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```
- 下载第1~7次《中国互联网络发展状况统计报告》
  - 多行
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_6.htm|
cat index_6.htm |
grep "次"|
grep pdf|
awk -F "</a>" '{print $1}'|
awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|
sed 's/target//g'|sed 's/"_blank">//g'|
awk -F "'" '{print $1$2}'|sed 's/ //g'|
sed 's/hlwxzbg./hlwxzbg/g'|
xargs wget -c
```  
- 单行
>wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_6.htm|cat index_6.htm |grep "次"|grep pdf)|awk -F "</a>" '{print $1}'|awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|sed 's/target//g'|sed 's/"_blank">//g'|awk -F "'" '{print $1$2}'|sed 's/ //g'|sed 's/hlwxzbg./hlwxzbg/g'|xargs wget -c
