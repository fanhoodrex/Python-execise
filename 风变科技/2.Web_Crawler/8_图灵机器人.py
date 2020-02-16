# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:01:00 2019

@author: Zac_Fang
"""
import requests
import json

userid = str(1)
# 1 可以替换成任何长度小于32的字符串哦 
apikey = str(‘A')
# 这里的A，记得替换成你自己的apikey哦～

# 创建post函数
def robot(content):
    # 图灵api
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # 创建post提交的数据
    data = {
        "perception": {
            "inputText": {
                "text": content
                         }
                      },
        "userInfo": {
                    "apiKey": apikey,
                    "userId": userid,
                    }
    }
    # 转化为json格式
    jsondata = json.dumps(data)
    # 发起post请求
    response = requests.post(api, data = jsondata)
    # 将返回的json数据解码
    robot_res = json.loads(response.content)
    # 提取对话数据
    print(robot_res["results"][0]['values']['text'])

for x in range(10):
    content = input("talk:")
    # 输入对话内容 
    robot(content)
    if x == 10:
        break 
        # 十次之后就结束对话，数字可以改哦，你想几次就几次
