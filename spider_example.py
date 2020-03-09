import requests
import re

# sid 学号


def get_session_id(code: str) -> str:
    url = "http://ecardwx.ccnu.edu.cn/data_chart/chart_verify_count.php?code=" + \
        code + "&state=1"

    payload = {}
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/WIFI Language/zh_CN',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.headers['Set-Cookie'].split(';')[0]


def get_ecard(sid: str) -> str:
    url = "http://ecardwx.ccnu.edu.cn/data_chart/ecard_deal/month_deal_list.php?m_xxh=" + sid

    year = '2020'
    month = '1'
    payload = 'year=' + year + '&month=' + month

    headers = {
        'Cookie': get_session_id(),
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN',
        'Host': 'ecardwx.ccnu.edu.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '17',
        'Cache-Control': 'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'http://ecardwx.ccnu.edu.cn/data_chart/ecard_deal/month_deal_main.php?m_xxh='+sid,
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-cn'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

# 下面是用正则把数据给提取出来。


def regular_expressions(string: str) -> str:
    # 食堂
    # 最后面两个空格把店家名字后面的空格去掉。
    result = re.findall(
        "<span>消费：(.*?)元，</span><span>地点：后勤集团/饮食中心/(.*?)/(.*?)/(.*?)  </span>", string)

    # 超市
    #result = re.findall("<span>消费：(.*?)元，</span><span>地点：后勤集团/商贸中心/(.*?)/(.*?)/(.*?)</span>", string)
    return result


if __name__ == '__main__':
    sid = input('Enter sid: ')
    print(regular_expressions(get_ecard(sid)))
