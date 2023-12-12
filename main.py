import subprocess
import time
import requests
'''
用于电子科技大学实验室安全知识学习的刷时间脚本
使用方法：
1. 安装requests库
2. 替换成你在看的页面“Referer”
2. 替换成你的“Cookie”
3. 运行
'''

def update_my_time():

    url = "https://labsafetest.uestc.edu.cn/exam_xuexi_online.php"
    payload = {
        "Cookie": "wsess=ST-123456-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-aaaa-cas",
        "Origin": "https://labsafetest.uestc.edu.cn",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Referer": "https://labsafetest.uestc.edu.cn/redir.php?catalog_id=121&object_id=2731",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
    }
    data = "cmd=xuexi_online"

    r = requests.post(url,data=data,headers=payload)
    txt = r.text
    print(txt)

if __name__ == "__main__":
    while True:
        update_my_time()
        time.sleep(30)
