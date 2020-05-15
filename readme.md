# 项目名称：ccnu消费记录分析

## 项目信息

作用：根据学校的接口(已知)，

1. 通过学号获取某人的校园卡消费记录==>爬虫，将数据储存下来。
   
   >已有信息为2019一年数据，其中学号范围为  201(6/7/8/9)210000——201(6/7/8/9)216000

2. 通过可视化包，做一点分析==>数据分析/简单分析，

3. 可视化一下==>可视化。

sessionid 获取, 问题是code会过期，所以就不能在线获取用户的数据，但是我们可以爬下来之后，对每个用户进行处理。

```http
GET /data_chart/chart_verify_count.php?code=&{code}&state=1 HTTP/1.1
Host: ecardwx.ccnu.edu.cn
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
Connection: keep-alive
```


请求如下，是校园卡中心微信上抓包过来的。

```http
POST /data_chart/ecard_deal/month_deal_list.php?m_xxh=${sid} HTTP/1.1
Host: ecardwx.ccnu.edu.cn
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
Content-Type: application/x-www-form-urlencoded
Origin: http://ecardwx.ccnu.edu.cn
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Referer: http://ecardwx.ccnu.edu.cn/data_chart/ecard_deal/month_deal_main.php?m_xxh=${sid}
Content-Length: 17
Cookie:   #会过期、
```

## 开发规范

1. 使用pipenv,对虚拟环境和依赖管理。
2. 命名规范：待定
3. 注释规范：待定

## 项目目录结构

```
/
   __init__.py
   routes/
   models/
   templates/
      index.html
   static/
      style.css
   util/
      wordcloud/
      graph/
```