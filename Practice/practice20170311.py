#encoding=utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time

driver=webdriver.Ie(executable_path='c:\\IEDriverServer')
#设置浏览器加载最长等待时长
#一般用于加载文字，不需要等待其他图片等内容加载完毕，起到提速的效果
#如果超时会抛出异常，需要捕获异常，然后继续操作
driver.set_page_load_timeout(5)
try:
    driver.get("https://www.sogou.com")
except TimeoutException, e:
    print u"页面没有完全加载完"
#获取当前driver对应的handle
print driver.window_handles
#获取浏览器名字
print driver.name
#获取浏览器port
print driver.port
#获取当前窗口的url
print driver.current_url
#截屏
driver.get_screenshot_as_file("d:\\test\\baidu.png")

#执行js脚本
#弹出alert窗口
driver.execute_script("alert('hello');")
#修改页面
driver.execute_script("document.write('<h1>gloryroad<h1>');")
#向百度搜索框输入内容
driver.execute_script("document.getElementById('kw').value='hello';")
#向sogou搜索框输入内容
driver.execute_script("document.getElementById('query').value='hello';")
#获取搜索框内容
print driver.execute_script("return document.getElementById('query').value;")

#点击搜索
driver.execute_script("document.getElementById('stb').click();")

#获取浏览器窗口标题
print driver.title
#获取浏览器属性设置
print driver.desired_capabilities
#获取窗口大小
'''>>> driver.get_window_size()
{u'width': 800, u'height': 600}'''
driver.get_window_size()
#设置窗口大小
driver.set_window_size(800,800)
#获取当前窗口位置左上角坐标
'''>>> driver.get_window_position()
{u'y': -150, u'x': -100}'''
driver.get_window_position()
#设置窗口位置
driver.set_window_position(10,10)
#最大化浏览器窗口
driver.maximize_window()
time.sleep(2)
#可以自定义获取元素的方式，可以用于数据与代码分离，将参数集以特定的格式存放到一个文件中，循环去读取
driver.find_element('id','kw')
driver.find_element('xpath', "//input[@id='kw']")
#获取当前页的源码driver.page_source，返回Unicode编码
source = driver.page_source.encode('utf-8')
with open("d:\\test\\baidu_source.html",'w') as fp:
    fp.write(source)
#断言，判断源码里是否包含某个字符串
assert u'百度一下，你就知道' in source

#从文件中读取参数，获取元素
def find_object(config_file,element_name):
    with open(config_file) as fp:
        content=fp.readlines()
    for eachLine in content:
        eachLine = eachLine.strip()
        key_value = eachLine.split('=')[1].split(",")
        key = key_value[0]
        value = key_value[1]
        if element_name in eachLine:
            return driver.find_element(key,value)
    return None

#对象库，从文件中读取参数，获取元素
class object_map(object):
    def __init__(self, config_file):
        self.config_file = config_file
    def find_object(self,element_name):
        with open(self.config_file) as fp:
            content=fp.readlines()
        for eachLine in content:
            by_value = eachLine.strip().split('=')[1].split(",")
            by = by_value[0]
            value = by_value[1]
            if element_name in eachLine:
                return driver.find_element(by,value)
        return None

om = object_map("d:\\test\\config.txt")
om.find_object("searchbox").send_keys(u"光荣之路自动化测试")
om.find_object("submitbutton").click()
time.sleep(5)
assert u"吴老" in driver.page_source

#通过链接定位元素(精确匹配)
driver.find_element_by_link_text(u'图片').click()
time.sleep(2)
#查看找到元素的个数,elements：查找多个元素
print len(driver.find_elements_by_partial_link_text(u'美女'))
print len(driver.find_elements('xpath','//input'))
print len(driver.find_elements_by_path('//a'))
#通过链接定位元素（模糊匹配）
driver.find_element_by_partial_link_text(u'美女').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
#定位输入框输入内容
#通过id查找
search_box=driver.find_element_by_id('query')
#通过xpath查找
search_box=driver.find_element_by_xpath("//*[@id='query']")
#通过css查找，传说比xpath要快
search_box=driver.find_element_by_css_selector("#query")
#通过标签来查找
driver.find_element_by_tag_name('input')
search_box.send_keys(u'光荣之路')
time.sleep(2)
#点击搜索
submit_button=driver.find_element_by_id('stb')
submit_button.click()
#点击input输入框
search_input=driver.find_element_by_name('q')
search_input.click()
time.sleep(5)
#浏览器后退
driver.back()
time.sleep(3)
#浏览器前进
driver.forward()
time.sleep(3)
#退出浏览器
driver.quit()
