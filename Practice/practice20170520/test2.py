#encoding=utf-8
from selenium import webdriver
import time
with open("d:\\data.txt") as fp:
    data=fp.readlines()
import ExcelManage, MyTime, ExcelManage3

em = ExcelManage.ExcelManage("d:\\data.xlsx")
datas = em.get_data_dict_arr()
em3 = ExcelManage3.ExcelManage3('d:\\data.xlsx')
file_name = "d:\\data_result.xlsx"
driver=webdriver.Ie(executable_path="d:\\IEDriverServer")
# result_fp = open("d:\\data_result.txt", 'w')
for i in range(len(datas)):
    driver.get("http://www.baidu.com")
    print datas[i][u'搜索词']
    driver.find_element_by_id("kw").send_keys(datas[i][u'搜索词'])
    driver.find_element_by_id("su").click()
    time.sleep(3)
    if datas[i][u'断言关键词'] in driver.page_source:
        em3.insert_data_by_cell(i+2,5, '成功')
    else:
        em3.insert_data_by_cell(i + 2, 5, '失败')
    em3.insert_data_by_cell(i + 2, 4, MyTime.get_datetime())
em3.save(file_name)
# result_fp.close()
driver.quit()