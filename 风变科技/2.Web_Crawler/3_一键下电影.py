#Method 1
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

movie = input('你想看什么电影呀？')
gbkmovie = movie.encode('utf-8')
#将汉字，用gbk格式编码，赋值给gbkmovie
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
#将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
res = requests.get(url)
#下载××电影的搜索页面
res.encoding ='utf-8'
#定义res的编码类型为gbk
soup_movie = BeautifulSoup(res.text,'html.parser')
#解析网页
urlpart = soup_movie.find(class_="co_content8").find_all('table')
# print(urlpart)
if urlpart:#
    urlpart = urlpart[0].find('a')['href']
    urlmovie = 'https://www.ygdy8.com/' + urlpart
    res1 = requests.get(urlmovie)
    res1.encoding = 'utf-8'
    soup_movie1 = BeautifulSoup(res1.text,'html.parser')
    urldownload = soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href']
    print(urldownload)
else:
    print('未找到<' + movie + ">这部电影")
    # 有些电影是查询不到没下载链接的，因此加了个判断


"""
#Method 2 
import requests
# 引用requests模块
for i in range(5):
    res_comments = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(i)+'&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010')
    # 调用get方法，下载评论列表
    json_comments = res_comments.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_comments = json_comments['comment']['commentlist']
    # 一层一层地取字典，获取评论列表
    for comment in list_comments:
    # list_comments是一个列表，comment是它里面的元素
        print(comment['rootcommentcontent'])
        # 输出评论
        print('-----------------------------------')
        # 将不同的评论分隔开来
"""