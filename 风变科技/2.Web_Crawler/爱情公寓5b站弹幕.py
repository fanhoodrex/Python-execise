import pandas as pd
import requests,time,jieba
from bs4 import BeautifulSoup
from collections import Counter
from pyecharts import WordCloud

url = 'http://comment.bilibili.com/123519261.xml'
html = requests.get(url)
html.encoding='utf8'
soup = BeautifulSoup(html.text, 'lxml') 
results = soup.find_all('d') 
comments = [comment.text for comment in results] #list comprehension on the list of results
num = 1
for i in comments:
    print(str(num)+": " + i +'\n')
    num = num + 1   
comments_dict = {'comments': comments} # form dictionany consisting of the conmment key and comment as value

df = pd.DataFrame(comments_dict)
df.to_csv('bili_弹幕.csv', encoding='utf-8-sig')
#学生阶段在弹幕中的提及数
a = {'小学':'小学|一年级|二年级|三年级|四年级|五年级|六年级', 
     '初中':'初中|初一|初二|初三', 
     '高一':'高一', 
     '高二':'高二',
     '高三':'高三', 
     '大一':'大一', 
     '大二':'大二', 
     '大三':'大三', 
     '大四':'大四',}
     
for key, value in a.items():
    data[key] = data['comments'].str.contains(value)
staff_count = pd.Series({key: data.loc[data[key], 'comments'].count() for key in a.keys()}).sort_values()
print(staff_count)

stop_words = [x.strip() for x in open ('stopwords.txt',encoding="utf-8") ]
text = ''.join(data['comments'])
words = list(jieba.cut(text))
ex_sw_words = []
for word in words:
    if len(word)>1 and (word not in stop_words):
        ex_sw_words.append(word)
c = Counter()
c = Counter(ex_sw_words)
wc_data = pd.DataFrame({'word':list(c.keys()), 'counts':list(c.values())}).sort_values(by='counts', ascending=False).head(100)
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", wc_data['word'], wc_data['counts'], word_size_range=[15, 80])