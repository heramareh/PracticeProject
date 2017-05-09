#encoding=utf-8

from xml.dom.minidom import parse
import ExcelManage
from openpyxl import Workbook

class DBManage(object):
    def __init__(self, filepath):
        self.DOMTree = parse(filepath)
        self.root_node = self.DOMTree.documentElement

    def get_value_by_tag_names(self, parent_node, tag_name):
        self.db_node = self.root_node.getElementsByTagName(parent_node)[0]
        self.node = self.db_node.getElementsByTagName(tag_name)[0]
        return self.node.childNodes[0].data

    def get_db_info_by_tag_name(self, tag_name):
        return self.get_value_by_tag_names("db", tag_name)

if __name__ == '__main__':
    db = DBManage("e:\\db.xml")
    key_list = ["host", "port", "username", "password", "charset", "dbname"]
    db_info = dict.fromkeys(key_list)
    for key in key_list:
        db_info[key] = db.get_db_info_by_tag_name(key)
    print db_info
    em = ExcelManage.ExcelManage("e:\\db.xlsx")
    em.input_to_excel(db_info, "gloryroad")
