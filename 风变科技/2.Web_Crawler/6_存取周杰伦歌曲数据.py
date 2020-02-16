# 直接运行代码就好
import requests,time,openpyxl
# 引用requests,time,openpyxl模块

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
item = 1 #歌曲ID序号

workbook = openpyxl.Workbook()
working_sheet = workbook.active
working_sheet.title = "周杰伦歌单"

head_row = ['序号ID','歌曲名','所属专辑','播放时长','播放链接']
working_sheet.append(head_row)
"""
working_sheet['A1'] ='序号ID'     #加表头，给A1单元格赋值
working_sheet['B1'] ='歌曲名'     #加表头，给A1单元格赋值
working_sheet['C1'] ='所属专辑'   #加表头，给B1单元格赋值
working_sheet['D1'] ='播放时长'   #加表头，给C1单元格赋值
working_sheet['E1'] ='播放链接'   #加表头，给D1单元格赋值
"""

for x in range(5):
    headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
    # 伪装请求头

    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        song_name = music['name']
        album = music['album']['name']
        interval = music['interval']
        link = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n'
        # 定义变量初始化
        print(str(item) +". " +music['name'])
        # 以name为键，查找歌曲名
        print( '所属专辑：'+music['album']['name'])
        # 查找专辑名
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
        # 查找播放链接
        working_sheet.append([item,song_name,album,interval,link])
        item += 1
        time.sleep(0.1)
        #程序停顿一秒从而提升输出效果
    workbook.save('Jay.xlsx')
    #最后保存并命名这个Excel文件