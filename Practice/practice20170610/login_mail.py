#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def sleep(second=0.5):
    time.sleep(second)

def set_fly(bool=True):
    fly_element = driver.find_element_by_xpath(xpath + "//b[contains(@id,'fly')]")
    class_str = fly_element.get_attribute("class")
    if bool:
        if 'checked' not in class_str:
            fly_element.click()
    else:
        if 'checked' in class_str:
            fly_element.click()

# 创建Chrome浏览器的实例
driver = webdriver.Chrome(executable_path="d:\\chromedriver")
# 设置隐式等待时间为10秒
driver.implicitly_wait(10)
# 最大化浏览器窗口
driver.maximize_window()

# 访问126邮箱登录页面
driver.get("http://mail.126.com")
# 暂停5秒,以便邮箱登录页面加载完成
time.sleep(5)
# 切换进frame控件
driver.switch_to.frame("x-URS-iframe")
# 获取用户名输入框
userName = driver.find_element_by_xpath('//input[@name="email"]')
# 输入用户名
userName.send_keys("sjjm0001")
# 获取密码输入框
pwd = driver.find_element_by_xpath("//input[@name='password']")
# 输入密码
pwd.send_keys("11111q")
# 发送一个回车键
pwd.send_keys(Keys.RETURN)
driver.find_element_by_xpath("//a[text()='继续登录']").click()
driver.switch_to.default_content()
# 等待10秒,以便登录成功后的页面加载完成
time.sleep(10)
# 新建联系人
driver.find_element_by_xpath("//div[text()='通讯录']").click()
sleep(1)
driver.find_element_by_xpath("//header//span[text()='新建联系人']").click()
sleep(1)
# 录入联系人信息
xpath = "//div[@id='contact_edit_main']"
# 姓名
driver.find_element_by_id("input_N").send_keys(u"光荣之路")
sleep()
# 选择邮箱类型
driver.find_element_by_xpath(xpath + "//div[@id='iaddress_MAIL_wrap']//span[@class='nui-select-arr']").click()
mail_type = "家庭邮箱"
driver.find_element_by_xpath(xpath + "//a[text()='" + mail_type + "']").click()
# 邮箱
driver.find_element_by_xpath(xpath + "//div[@id='iaddress_MAIL_wrap']//input").send_keys("gloryroad@126.com")
sleep()
# 设为星标联系人
set_fly()
sleep()
# 选择电话类型
driver.find_element_by_xpath(xpath + "//div[@id='iaddress_TEL_wrap']//span[@class='nui-select-arr']").click()
tel_type = "办公电话"
driver.find_element_by_xpath(xpath + "//a[text()='" + tel_type + "']").click()
# 电话
driver.find_element_by_xpath(xpath + "//div[@id='iaddress_TEL_wrap']//input").send_keys("18888888888")
sleep()
# 备注
driver.find_element_by_id("input_DETAIL").send_keys(u"秋天铁血战车")
sleep()
# 选择分组
driver.find_element_by_xpath(xpath + "//dd[@id='contact_edit_group']//span[text()='请选择']").click()
sleep(1)
# 勾选分组
group_name = "秋天铁血战车学习群"
driver.find_element_by_xpath("//div[@id='contact_edit_details']//span[text()='" + group_name + "']").click()
sleep()
# 保存
driver.find_element_by_xpath("//div[@class='nui-msgbox-ft']//span[text()='保 存']").click()
sleep(1)
# 确定
driver.find_element_by_xpath("//span[text()='确 定']").click()
sleep(1)
assert u'光荣之路' in driver.page_source
driver.quit()