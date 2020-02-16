import requests,smtplib,schedule,time
from bs4 import BeautifulSoup 
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def weather_crawler():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = []
    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,URL,ingredients])
    return list_all

def send_email(list_all):
    global account,password,receiver
    mailhost='smtp.qq.com'
    #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()


def job():
    print('开始')
    list_all = weather_crawler()
    send_email(list_all)
    print('任务完成')

schedule.every().day.at("07:30").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)

