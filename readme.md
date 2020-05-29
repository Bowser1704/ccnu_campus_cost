# 项目名称：ccnu消费记录分析

## 项目信息

作用：根据学校的接口(已知)，

1. 通过学号获取某人的校园卡消费记录==>爬虫，将数据储存下来。
   
   >已有信息为2019一年数据，其中学号范围为  201(6/7/8/9)210000——201(6/7/8/9)216000，均为本科生
                                         > 201X11XXXX 为研究生学号

2. 通过可视化包，做一点分析==>数据分析/简单分析，

3. 可视化一下==>可视化。


## 开发规范

1. 使用pipenv,对虚拟环境和依赖管理。
2. 数据库使用环境变量
   ```bash
   export CAMPUS_DATABASE_URI="mysql+pymysql://username:password@host/dbname"
   ```

## 项目目录结构

```
/
   __init__.py
   routes/
      templates/
         index.html
      static/
         style.css
   models/
   util/
      wordcloud/
      graph/
```

## TODO

1. 添加异常处理，如果没有收录这个人的学号，返回一些信息。

2. mysql to clickhouse。
