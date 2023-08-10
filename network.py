# coding=utf8
# --- TYUT Campus Network -----------------------------------------------------
#
#   name: 学号2021520***
#   password: ********
#   user_ip：根据get请求获取
#   Author: lllyyyuuu
#   cron:  */2 * * * * python3 /root/net.py >> /root/log 2>&1
# -----------------------------------------------------------------------------
import os
import datetime
import requests
import platform
import re
import json
from msg import msg
from sendNotify import send
# ---------------------
# 输入用户名密码
name = 'XXXXXXXXX'
password = 'XXXXXXXX'
#----------------------

# ---------------------------------
# 以下为代码
user_ip = '101.7.166.XXX'

# -------------------------------------------------------------------------------------
#通知服务
msg().main()

# -------------------------------------------------------------------------------------
url = 'http://219.226.127.250/a79.htm'
current_file_path = os.path.abspath(os.path.dirname(__file__))
# function1：测试是什么平台
def test_platform():
    if platform.system().lower() == 'windows':
        return 0
    elif platform.system().lower() == 'linux':
        return 1


# function2：测试网络是否连通
def is_net_ok():
    if test_platform() == 0:
        exit_code = os.system('ping www.baidu.com -n 1')
        return exit_code
    if test_platform() == 1:
        exit_code = os.system('ping www.baidu.com -c 1')
        # print('exit_code: ',exit_code)
        return exit_code
LOGIN_PAGE_URL = "http://219.226.127.250:801/eportal/portal/login?"

# function3：登录网络过程
def login_request(name, password):
    #user_ip = get_ip()
    data1 = {"callback": "dr1003",
                    "login_method": 1,
                    "user_account": name,
                    "user_password": password,
                    "wlan_user_ip": user_ip,
                    "jsVersion": '4.1.3',
                    "lang": 'zh-cn',
                    "v": '1680',
                    "lang": 'zh'}
    try:
        
        response = requests.get(LOGIN_PAGE_URL, data1)
        
        if response.status_code == 200:
            print('respon:',response.text)
            #旧ip被使用，则使用新的ip
            if int(parse_jsonp_response(response))==0:
                new_ip = get_ip()
                data1['wlan_user_ip'] = new_ip
                print('获取新ip:',data1["wlan_user_ip"])

                modify_user_ip_in_file(new_ip)

                response = requests.get(LOGIN_PAGE_URL, data1)
                print("[01] {} login success  ".format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),'new ip:',new_ip)
            else:
                print("[01] {} login success  ".format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),'old ip:',user_ip)
        else:
            print("Request failed with status code:", response.status_code)

    except:
        print("[00] {} requsest error ，openwrt is not connected to Internet ".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

def parse_jsonp_response(response):
    json_str_match = re.search(r'\((.*?)\)', response.text)
    if json_str_match:
        json_str = json_str_match.group(1)
        response_dict = json.loads(json_str)
        result_value = response_dict.get("result")
        #print("Response as Dictionary:", result_value)
        return result_value
    else:
        print("No valid JSON found in response.")


def get_ip():
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 获取返回的内容（文本形式）
        content = response.text
        pattern = r'v46ip=\'(.*?)\''
        match = re.search(pattern, content)
        if match:
            v46ip_value = match.group(1)
            return v46ip_value
        else:
            return 0
    else:
        print("请求失败，状态码：", response.status_code)

def modify_user_ip_in_file(new_ip_value):
    file_name = current_file_path + '/network.py'
    old_ip = user_ip
    # 读取文件内容
    with open(file_name, "r",encoding='utf-8') as f:
        lines = f.readlines()

    # 找到第一个包含 user_ip 的行，并进行替换
    new_lines = []
    found_user_ip = False

    for line in lines:
        if "user_ip" in line and not found_user_ip:
            parts = line.split("'")
            print(parts)
            if len(parts) >= 3:
                new_line = parts[0] + "'" + new_ip_value + "'" + parts[2] + "\n"
                new_lines.append(new_line)
                found_user_ip = True
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    # 将修改后的内容写回文件
    with open(file_name, "w", encoding='utf-8') as f:
        f.writelines(new_lines)
    print('修改文件：user_ip = ',old_ip,'->user_ip = ',new_ip_value)
    # 将修改后的内容写回文件
    msg(" Hello ! ")
    msg('旧ip：'+ old_ip +'->新获取的ip： ' + new_ip_value)
    message = msg().message()
    send("ip变更通知", message)


def main():
    if  is_net_ok()!=0:
        # 没有网络连接，进行连接
        login_request(name, password)
    else:
        print("[02] {} openwrt is online  ".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        msg(" Hello ! ")
        msg('当前ip：'+ user_ip)
        message = msg().message()
        send("ip变更通知", message)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('[ERROR]:'),
        print(e)

