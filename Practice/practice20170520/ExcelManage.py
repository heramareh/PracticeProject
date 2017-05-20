#encoding=utf-8

import xlrd, os, shutil
from xlwt import easyxf
from xlutils.copy import copy
from datetime import datetime

# from common import LogManage, ConfigManage

class ExcelManage(object):
    def __init__(self, file_path, sheet_name=None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = xlrd.open_workbook(self.file_path)
        if self.sheet_name is None:
            self.sheet = self.workbook.sheet_by_index(0)
        else:
            self.sheet = self.workbook.sheet_by_name(self.sheet_name)

    def get_rows(self):
        u"""获取文件总行数"""
        return self.sheet.nrows

    def get_cols(self):
        u"""获取文件总列数"""
        return self.sheet.ncols

    def get_excel_data(self):
        u"""读取excel数据，存放在一个列表中返回"""
        try:
            data = []
            for row in xrange(self.get_rows()):
                each_data = {}
                for value in self.sheet.row_values(row):
                    each_data = eval(value)
                data.append(each_data)
            return data
        except Exception, e:
            # LogManage.error(u"读取excel失败：" + str(e))
            return None

    def get_excel_datas(self):
        u"""读取excel数据，存放在一个二维列表中返回"""
        try:
            data = []
            for row in xrange(self.get_rows()):
                each_row = []
                for value in self.sheet.row_values(row):
                    each_row.append(value)
                data.append(each_row)
            return data
        except Exception, e:
            # LogManage.error(u"读取excel失败：" + str(e))
            return None

    def get_excel_data_by_row(self, row):
        u"""读取一行excel数据，存放在一个列表中返回"""
        try:
            data = []
            for value in self.sheet.row_values(row):
                data.append(value)
            return data
        except Exception, e:
            # LogManage.error(u"读取excel失败：" + str(e))
            return None

    def get_excel_data_by_col(self, col):
        u"""读取一列excel数据，存放在一个列表中返回"""
        try:
            data = []
            for value in self.sheet.col_values(col):
                data.append(value)
            return data
        except Exception, e:
            # LogManage.error(u"读取excel失败：" + str(e))
            return None

    def get_excel_data_by_cell(self, cell):
        u"""读取指定单元格数据，并返回"""
        try:
            return self.sheet.cell_value(cell[0], cell[1])
        except Exception, e:
            # LogManage.error(u"读取excel失败：" + str(e))
            return None

    def get_data_dict_arr(self):
        u"""文件第一行为key，从第二行往后为value"""
        datas = []
        for row in xrange(1, self.get_rows()):
            data = {}
            for col in xrange(self.get_cols()):
                data[self.sheet.cell_value(0, col)] = self.sheet.cell_value(row, col)
            datas.append(data)
        return datas

    def get_data_dict_arr2(self):
        u"""文件第一行为key，从第二行往后为value，对日期格式单元格做了特殊处理"""
        datas = []
        for row in xrange(1, self.get_rows()):
            data = {}
            for col in xrange(self.get_cols()):
                if self.sheet.cell(row, col).ctype == 3:
                    date_value = xlrd.xldate_as_tuple(self.sheet.cell_value(row, col), 0)
                    value = datetime(*date_value[:6]).strftime("%Y-%m-%d %H:%M:%S")
                    print value
                    data[self.sheet.cell_value(0, col)] = value
                else:
                    data[self.sheet.cell_value(0, col)] = self.sheet.cell_value(row, col)
            datas.append(data)
        return datas

    def get_title(self):
        u"""获取第一行标题"""
        data = []
        for row in xrange(1):
            for col in xrange(self.get_cols()):
                data.append(self.sheet.cell_value(row, col))
        return data

    def get_data_dict(self):
        datas = []
        parent_col = 0
        parent_key = ''
        for col in xrange(self.get_cols()):
            if self.sheet.cell_value(1, col):
                parent_key = self.sheet.cell_value(0, col)
                break
            parent_col += 1
            continue
        data = {}
        data[parent_key] = []
        for row in xrange(2,self.get_rows()):
            if not self.sheet.cell_value(row, 0):
                child_data = {}
                for col in xrange(parent_col, self.get_cols()):
                    child_data[self.sheet.cell_value(1, col)] = self.sheet.cell_value(row, col)
                data[parent_key].append(child_data)
            else:
                if data and data[parent_key]:
                    datas.append(data)
                    data = {}
                    data[parent_key] = []
                child_data = {}
                for col in xrange(0, self.get_cols()):
                    if col >= parent_col:
                        child_data[self.sheet.cell_value(1, col)] = self.sheet.cell_value(row, col)
                    else:
                        data[self.sheet.cell_value(0, col)] = self.sheet.cell_value(row, col)
                data[parent_key].append(child_data)
        if data and data[parent_key]:
            datas.append(data)
        return datas

    def insert_data_by_col(self, start_row, col, data, file_name):
        u"""在指定列，插入相同数据"""
        wb = copy(self.workbook)
        ws = wb.get_sheet(0)
        for row in range(start_row, self.get_rows()):
            # self.sheet.cell_value(row=row, column=col).value = data
            ws.write(row, col, data)
        wb.save(file_name)

# 重命名文件，并将文件复制到指定路径下
def rename_file(file_name, new_file_name):
    u"""重命名文件"""
    os.rename(file_name, new_file_name)

def copy_file(file_name, new_file_name):
    u"""复制文件到指定目录下"""
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    shutil.copy(file_name, new_file_name)

def empty_dir(dir_name):
    u"""清空文件夹内容"""
    for root, dirs, files in os.walk(dir_name):
        if files:
            for file in files:
                os.remove(os.path.join(root, file))

# def copy_tmp_to_export(new_file_path):
#     # 复制临时目录下的文件到export文件下并重命名，同时清空tmp目录
#     try:
#         # tmp = ConfigManage.get_tmp_path()
#         old_file_path = ''
#         for root, dirs, files in os.walk(tmp):
#             if files:
#                 for file in files:
#                     old_file_path = os.path.join(tmp, file)
#                     break
#         copy_file(old_file_path, new_file_path)
#     except ExcelManage, e:
#         # LogManage.error(u"拷贝失败" + str(e))
#     finally:
#         # empty_dir(ConfigManage.get_tmp_path())

if __name__ == '__main__':
    # em = ExcelManage(r"E:\PythonProject\AutoTest_EGENIE\data\input\test01_Basic_Files\test01_001_warehouse_info.xlsx", "test_005")
    # print em.get_rows()
    # for i in em.get_excel_data():
    #     for k, v in i.items():
    #         print k, v
    # copy_tmp_to_export(os.path.join(ConfigManage.get_export_path(), "test01_002_010_export.xlsx"))
    # expect_file_dir = os.path.join(ConfigManage.get_expect_path(), "test01_Basic_Files")
    # export_file_dir = os.path.join(ConfigManage.get_export_path(), "test01_Basic_Files")
    # expect_file = os.path.join(expect_file_dir, "test01_002_010_expect.xlsx")
    # export_file = os.path.join(export_file_dir, "test01_002_010_export.xlsx")
    #     self.wareHouseLocation.import_warehouse_location(input_file, export_file)
    #     ExcelManage.copy_tmp_to_export(export_file)
    # assert ExcelManage(expect_file).get_excel_datas() == ExcelManage(export_file).get_excel_datas()
    # file_path = os.path.join(ConfigManage.get_input_path(), "test01_Basic_Files", u"test01_004_002_input.xlsx")
    # datas = ExcelManage(file_path).get_data_dict()
    # for data in datas:
    #     print data
        # for k,v in data.items():
        #     print k,v
    # file_path = os.path.join(ConfigManage.get_input_path(), "test02_Order_Manage", u"test02_001_002_input.xlsx")
    # datas = ExcelManage(file_path).get_data_dict()
    # for data in datas:
    #     print data
    # em = ExcelManage(os.path.join(ConfigManage.get_export_path(), 'export_goods_003.xlsx'))
    # em.insert_data_by_col(1, 6, u'商品分类', os.path.join(ConfigManage.get_export_path(), 'export_goods_003_new.xlsx'))
    pass