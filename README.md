# tyut_net(太原理工大学自动连接校园网)
## 前置条件：
已经物理连接到校园网的无线或者有线
## 1.本地使用方法
1. 安装git和python3
2. 克隆仓库
   ```
   git clone ttps://github.com/LH428/tyut_net.git && cd tyut_net
   ```
3. 安装依赖
```
   pip3 install pip -U
   pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   pip3 install -r requirements.txt
```
4. 配置config.json以及network.py
- config.json配置
  ```
  "send":[
           {
               ## 下方填写app提供的设备码，例如：https://api.day.app/123 那么此处的设备码就是123
               "BARK": "", # bark服务,自行搜索; secrets可填;
                                
               "SCKEY": "", # Server酱的SCKEY; secrets可填
               # 下方填写自己申请@BotFather的Token，如10xxx4:AAFcqxxxxgER5uw             
               "TG_BOT_TOKEN": "", # tg机器人的TG_BOT_TOKEN; secrets可填1407203283:AAG9rt-6RDaaX0HBLZQq0laNOh898iFYaRQ
               ## 下方填写 @getuseridbot 中获取到的纯数字ID740688801     
               "TG_USER_ID": "",  # tg机器人的TG_USER_ID; secrets可填 1434078534
               ## 下方填写代理IP地址，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "127.0.0.1"      
               "TG_API_HOST":"", # tg 代理api           
               "TG_PROXY_IP": "", # tg机器人的TG_PROXY_IP; secrets可填          
               "TG_PROXY_PORT": "", # tg机器人的TG_PROXY_PORT; secrets可填        
               "DD_BOT_ACCESS_TOKEN": "",# 钉钉机器人的DD_BOT_ACCESS_TOKEN; secrets可填  
               "DD_BOT_SECRET": "", # 钉钉机器人的DD_BOT_SECRET; secrets可填
               "QQ_SKEY": "", # qq机器人的QQ_SKEY; secrets可填              
               "QQ_MODE": "", # qq机器人的QQ_MODE; secrets可填
                ## 参考文档：http://note.youdao.com/s/HMiudGkb
                ## 下方填写素材库图片id（corpid,corpsecret,touser,agentid），素材库图片填0为图文消息, 填1为纯文本消息              
               "QYWX_AM": "", # 企业微信
                #官方网站：http://www.pushplus.plus         
               "PUSH_PLUS_TOKEN": ""# 微信推送Plus+        
           } 
       ]
  ```
- network.py配置
  ```
  name = "学号"
  password = "密码"
  #可随便填写一个user_ip
  例如：user_ip = "101.7.171.142"
  ```
5. 添加定时任务

   ```
   5 12,13 * * * cd /scriptPath/ && python3 network.py
   ```
