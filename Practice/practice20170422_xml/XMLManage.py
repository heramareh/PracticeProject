#encoding=utf-8

import xml.dom.minidom

class XMLManage(object):
    def __init__(self):
        # minidom解析器打开xml文档并将其解析为内存中的一棵树
        self.DOMTree = xml.dom.minidom.parse(r"E:\booklist.xml")
        print type(self.DOMTree)
        # 获取xml文档对象，就是拿到树的根
        self.booklist = self.DOMTree.documentElement


