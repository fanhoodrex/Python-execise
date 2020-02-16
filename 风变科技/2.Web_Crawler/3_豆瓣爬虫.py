import requests, random,bs4,time

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    res_content = res.text
    bs = bs4.BeautifulSoup(res_content, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']
        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        time.sleep(0.2)


import requests,time
# 引用requests模块
from bs4 import BeautifulSoup
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    tag_num = bs.find_all('div', class_="item")
    # 查找包含序号，电影名，链接的<div>标签
    tag_comment = bs.find_all('div', class_='star')
    # 查找包含评分的<div>标签
    tag_word = bs.find_all('span', class_='inq')
    # 查找推荐语
    list_all = []
    for x in range(len(tag_num)):
        if tag_num[x].text[2:5] == '' or tag_num[x].text[2:5] =='':
        # 此处引号内，填写没有推荐语的电影序号
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_num[x].find('a')['href'] ]
        else:
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_word[x].text, tag_num[x].find('a')['href']]
        list_all.append(list_movie)
for i in list_all:
    print(i,end="\n")
    time.sleep(0.1)