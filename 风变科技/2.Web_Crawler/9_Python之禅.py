# 下面是只能在爬虫课系统中运行的答案：
from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant') # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub') # 找到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(1)

contents = driver.find_elements_by_class_name('content') # 定位到Python之禅所在的标签
for content in contents:
    title = content.find_element_by_tag_name('h1').text # 提取标题
    chan = content.find_element_by_tag_name('p').text # 提取正文
    print(title + '\n' + chan + '\n') # 打印标题与正文
driver.close()


# 下面是只能在你的本地运行的答案：
from selenium import  webdriver # 从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() # 声明浏览器对象
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant') # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub') # 找到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(1)

contents = driver.find_elements_by_class_name('content') # 定位到Python之禅所在的标签
for content in contents:
    title = content.find_element_by_tag_name('h1').text # 提取标题
    chan = content.find_element_by_tag_name('p').text # 提取正文
    print(title + '\n' + chan + '\n') # 打印标题与正文
driver.close()