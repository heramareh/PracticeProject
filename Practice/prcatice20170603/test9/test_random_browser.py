#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random

# 节点主机的访问地址
host="http://192.168.0.112:6666/wd/hub"
browsers = ["firefox", "chrome", "internet explorer"]
driver = webdriver.Remote(
  # 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
  command_executor = host,
  desired_capabilities = {
        # 在browsers列表中随机选择一个浏览器
        "browserName": random.choice(browsers),
        "platform": "WINDOWS"
  })

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