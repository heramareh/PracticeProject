#encoding=utf-8

from openpyxl import Workbook, load_workbook
import random, os
from common import ConfigManage
from public_code.excel.ExcelManage import ExcelManage
from public_code.excel.ExcelManage3 import ExcelManage3


class ExcelManage2(object):
    def __init__(self, sheet_name = None):
        self.wb = Workbook()
        self.sheet_name = sheet_name
        if self.sheet_name == None:
            self.ws = self.wb.active
        else:
            self.ws = self.wb.get_sheet_by_name(self.sheet_name)

    def create_datas_goods(self, nick_list, outer_id, lens, file_path):
        size = ['SS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
        # 设置第一行标题
        self.ws.append(['nick', 'num_iid', 'skus-sku-outer_id', 'skus-sku-sku_id'])
        # 生成随机数
        for i in xrange(lens):
            self.ws.append([random.choice(nick_list), str(random.randint(int('1'+'0'*11), int('9'*12))), outer_id+str(random.randint(100, 200))+random.choice(size), str(random.randint(int('1'+'0'*12), int('9'*13)))])
        self.wb.save(file_path)

    def create_datas_orders(self, goods_file_path, file_path, lens=None):
        order_status = []
        # 设置第一行标题
        self.ws.append(['buyer_nick', 'orders-order-num_iid', 'orders-order-oid', 'orders-order-sku_id', 'seller_nick', 'status', 'tid'])
        # 获取商品信息
        datas = ExcelManage(goods_file_path).get_data_dict_arr()
        index = 1
        for data in datas[:lens]:
            self.ws.append([u'小明'+str(index), data['num_iid'], str(random.randint(int('1'+'0'*14), int('9'*15))), data['skus-sku-sku_id'], data['nick'], "WAIT_SELLER_SEND_GOODS", str(random.randint(int('1'+'0'*14), int('9'*15)))])
            index += 1
        self.wb.save(file_path)

    def insert_data_by_col(self,start_row, col, data, old_file_name, new_file_name):
        u"""在指定列，插入相同数据"""
        datas = ExcelManage3(old_file_name).get_datas()
        for i in range(start_row, len(datas)):
            datas[i][col] = data
        for i in datas:
            self.ws.append(i)
        self.wb.save(new_file_name)

if __name__ == '__main__':
    # em = ExcelManage2()
    # nick_list = [u'淘宝店铺001_100071', u'123321_100071', u'999999_100071', u'22222_100071', u'淘宝店铺002_100071']
    # goods_file_path = os.path.join(ConfigManage.get_input_path(), "test01_Basic_Files", u"test01_004_002_input.xlsx")
    # file_path = os.path.join(ConfigManage.get_input_path(), "test02_Order_Manage", u"test02_001_002_input.xlsx")
    # # em.create_datas_goods(nick_list, 'D-C301_T146-',10,file_path)
    # em.create_datas_orders(goods_file_path, file_path)
    em = ExcelManage2()
    em.insert_data_by_col(1, 6, u'商品分类', os.path.join(ConfigManage.get_export_path(), 'export_goods_005.xlsx'), os.path.join(ConfigManage.get_export_path(), 'export_goods_005_new.xlsx'))
