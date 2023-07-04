# coding=utf8
# --- TYUT Campus Network -----------------------------------------------------
#
#   name: 学号2021520***
#   password: ********
#   user_ip：根据get请求获取
#   Author:chaojie L
#   cron:  */2 * * * * python3 /root/net.py >> /root/log 2>&1
# -----------------------------------------------------------------------------
import os
import datetime
import requests
import platform

name = ''
password = ''
user_ip = ''

# function1：测试是什么平台
def test_platform():
    if platform.system().lower() == 'windows':
        return 0
    elif platform.system().lower() == 'linux':
        return 1
print(test_platform())

# function2：测试网络是否连通
def is_net_ok():
    if test_platform() == 0:
        exit_code = os.system('ping www.baidu.com -n 1')
        # print(exit_code)
        return exit_code
    if test_platform() == 1:
        exit_code = os.system('ping www.baidu.com -c 1')
        # print(exit_code)
        return exit_code
LOGIN_PAGE_URL = "http://219.226.127.250:801/eportal/portal/login?"

# function3：登录网络过程
def login_request(name, password):
    try:
        data1 = {"callback": "dr1003",
                 "login_method": 1,
                 "user_account": name,
                 "user_password": password,
                 "wlan_user_ip": user_ip,
                 "jsVersion": '4.1.3',
                 "lang": 'zh-cn',
                 "v": '1680',
                 "lang": 'zh'}
        result = requests.get(LOGIN_PAGE_URL, data1)
        print(result.text)
        print("[01] {} login success  ".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
        print("[00] {} requsest error ，openwrt is not connected to WIFI ".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def main():
    if  is_net_ok():
        # 没有网络连接，进行连接
        login_request(name, password)
    else:
        print("[02] {} openwrt is online  ".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('[ERROR]:'),
        print(e)
