import requests, random, bs4,time,openpyxl

#create excel file for storing data
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "豆瓣TOP250"

worksheet['A1'] = '序号ID'
worksheet['B1'] = '电影名'
worksheet['C1'] = '评分' 
worksheet['D1'] = '推荐语' #可能不存在
worksheet['E1'] = '链接'

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url).text
    bs = bs4.BeautifulSoup(res, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']
        if titles.find('span',class_="inq") != None: 
            tes = titles.find('span',class_="inq").text
            print(num + '.' + title + ' 评分:' + comment + '\n' + '推荐语：' + tes +'\n' + "链接:" + url_movie + "\n")
            worksheet.append([num,title,comment,tes,url_movie])
            time.sleep(0.1)
        else:
            print(num + '.' + title + ' 评分:' + comment + '\n' + "链接:"+ url_movie + "\n")
            worksheet.append([num,title,comment,'NUll',url_movie])           
            time.sleep(0.1)
workbook.save("豆瓣爬虫.xlsx")