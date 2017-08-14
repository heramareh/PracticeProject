#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
  # 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
  command_executor = 'http://192.168.0.112:6666/wd/hub',
  desired_capabilities = {
        # 指定远程计算机执行使用的浏览器为ie
        "browserName": "chrome",
        "video": "True",
        # 远程计算机的平台
        "platform": "WINDOWS"
  })
print ("Video: " + "http://www.baidu.com" + driver.session_id)

try:
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://www.sogou.com")
    assert u"搜狗" in driver.title
    elem = driver.find_element_by_id("query")
    elem.send_keys(u"webdriver实战宝典")
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    assert u"吴晓华" in driver.page_source
    print 'done!'
finally:
    driver.quit()