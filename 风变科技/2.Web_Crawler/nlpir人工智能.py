# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:06:41 2019

@author: Zac_Fang
"""
import requests,json
#引入requests库
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
#Word2vec功能对应的请求网址。
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#封装请求头
words = input('请输入你想查询的词汇：')
#获取需要分析的文本
data = {'content':words}
#封装数据内容，我们在Headers面板中的底部看过发送的数据内容是一个字典。
res = requests.post(url,data=data,headers=headers)
#发送post请求
print(res.text)
#把返回的结果打印出来

# 引入json模块
a = [1,2,3,4]
# 创建一个列表a。
b = json.dumps(a)
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
print(b)
# 打印b。
print(type(b))
# 打印b的数据类型，为字符串。
c = json.loads(b)
# 使用loads()函数，将json格式的字符串b转为列表，赋值给c。
print(c)
# 打印c。
print(type(c)) 
# 打印c的数据类型，为列表。