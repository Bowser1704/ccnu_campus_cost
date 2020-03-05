# 项目名称：ccnu消费记录分析

## 项目信息

作用：根据学校的接口(已知)，

1. 通过学号获取某人的校园卡消费记录==>爬虫，

2. 通过可视化包，做一点分析==>数据分析/简单分析，

3. 可视化一下==>可视化。


请求如下，是校园卡中心微信上抓包过来的。

```http
POST /data_chart/ecard_deal/month_deal_list.php?m_xxh=2018212576 HTTP/1.1
Host: ecardwx.ccnu.edu.cn
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
Content-Type: application/x-www-form-urlencoded
Origin: http://ecardwx.ccnu.edu.cn
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Referer: http://ecardwx.ccnu.edu.cn/data_chart/ecard_deal/month_deal_main.php?m_xxh=2018212576
Content-Length: 17
Cookie: PHPSESSID=f4f587d4708bdf1a9e962537fbe81a73  #可能会过期、
```

## 开发规范

1. 使用pipenv,对虚拟环境和依赖管理。
2. 命名规范：待定
3. 注释规范：待定