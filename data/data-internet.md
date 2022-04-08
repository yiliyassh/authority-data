## 中国互联网络发展状况统计报告 :+1::+1::+1:
- http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index.htm
- [第49次《中国互联网络发展状况统计报告》（2022年2月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/202202/P020220311493378715650.pdf)
- [第48次《中国互联网络发展状况统计报告》（2021年8月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/202109/P020210915523670981527.pdf)
- [第47次《中国互联网络发展状况统计报告》（2021年2月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/202102/P020210203334633480104.pdf)
- [第46次《中国互联网络发展状况统计报告》（2020年9月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/202009/P020210205509651950014.pdf)
- [第45次《中国互联网络发展状况统计报告》（2020年4月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/202004/P020210205505603631479.pdf)
- [第44次《中国互联网络发展状况统计报告》（2019年8月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201908/P020190830356787490958.pdf)
- [第43次《中国互联网络发展状况统计报告》（2019年2月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201902/P020190318523029756345.pdf)
- [第42次《中国互联网络发展状况统计报告》（2018年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201808/P020180820630889299840.pdf)
- [第41次《中国互联网络发展状况统计报告》（2018年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201803/P020180305409870339136.pdf)
- [第40次《中国互联网络发展状况统计报告》（2017年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201708/P020170807351923262153.pdf)
- [第39次《中国互联网络发展状况统计报告》（2017年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201701/P020170123364672657408.pdf)
- [第38次中国互联网络发展状况统计报告    （2016年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201608/P020160803367337470363.pdf)
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
- [第37次中国互联网络发展状况统计报告（2016年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201601/P020160122469130059846.pdf)
- [第36次中国互联网络发展状况统计报告（2015年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201507/P020150723549500667087.pdf)
- [第35次中国互联网络发展状况统计报告（2015年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201502/P020150203551802054676.pdf)
- [第34次中国互联网络发展状况统计报告（2014年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201407/P020140721507223212132.pdf)
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
- [第33次中国互联网络发展状况统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/hlwtjbg/201403/P020140305346585959798.pdf)
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
- [第29次中国互联网络发展状况统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201201/P020120709345264469680.pdf)
- [第28次中国互联网络发展状况统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201107/P020120709345279403991.pdf)
- [第27次中国互联网络发展状况统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201101/P020120709345289031187.pdf)
- [第26次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201007/P020120709345290787849.pdf)
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
- [第25次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/201001/P020120709345300487558.pdf)
- [第24次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200907/P020120709345315706062.pdf)
- [第23次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345332767465.rar)
- [第22次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345337342613.doc)
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
- [第21次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345342042236.rar)
- [第20次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345348973165.doc)
- [第19次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345349881234.doc)
- [第18次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345356258945.doc)
- [第17次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345358064145.pdf)
- [第16次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345358978614.pdf)
- [第15次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345359935070.pdf)
- [第14次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345360848110.pdf)
- [第13次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345361747555.pdf)
- [第12次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345365230387.pdf)
- [第11次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345366251949.pdf)
- [第10次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345367150805.pdf)
- [第9次中国互联网络发展状况调查统计报告](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345368128648.pdf)
- [第8次中国互联网络发展状况调查统计报告（2001年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345368965113.pdf)
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
- [第7次中国互联网络发展状况调查统计报告（2001年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200906/P020120709345369819758.pdf)
- [第6次中国互联网络发展状况调查统计报告（2000年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345370656662.pdf)
- [第5次中国互联网络发展状况调查统计报告（2000年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345371437524.pdf)
- [第4次中国互联网络发展状况调查统计报告（1999年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345372226100.pdf)
- [第3次中国互联网络发展状况调查统计报告（1999年1月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345373005822.pdf)
- [第2次中国互联网络发展状况调查统计报告（1998年7月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345373784718.pdf)
- [第1次中国互联网络发展状况调查统计报告（1997年10月）](http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/200905/P020120709345374625930.pdf)
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
```
wget http://www.cnnic.net.cn/hlwfzyj/hlwxzbg/index_6.htm|cat index_6.htm |grep "次"|grep pdf)|awk -F "</a>" '{print $1}'|awk -F "=" '{print " http://www.cnnic.net.cn/hlwfzyj/hlwxzbg "$3}'|sed 's/target//g'|sed 's/"_blank">//g'|awk -F "'" '{print $1$2}'|sed 's/ //g'|sed 's/hlwxzbg./hlwxzbg/g'|xargs wget -c  
```