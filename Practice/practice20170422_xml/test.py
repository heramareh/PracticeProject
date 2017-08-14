#encoding=utf-8

#从xml.dom.minidom模块引入解析器parse
from xml.dom.minidom import parse
import xml.dom.minidom

def test():
    #minidom解析器打开xml文档并将其解析为内存中的一棵树
    DOMTree = parse(r"E:\booklist.xml")
    print type(DOMTree)
    #获取xml文档对象，就是拿到树的根
    booklist = DOMTree.documentElement
    print booklist
    # 获取xml内容
    print booklist.toxml()
    # 判断是否包含属性
    print booklist.hasAttribute("book")
    print booklist.getAttribute("book")
    print booklist.lastChild
    print booklist.firstChild
    # 获取所有book节点的list集合
    print booklist.getElementsByTagName("book")
    # 返回节点下所有子节点组成的list
    print booklist.getElementsByTagName("book")[0].childNodes
    # 获取节点文本值
    print booklist.getElementsByTagName("title")[0].childNodes[0].data
    for title in booklist.getElementsByTagName("title"):
        print title.toxml()
        print title.nodeName
        print title.childNodes[0].data
    # 判断是否有子节点
    print booklist.hasChildNodes()

if __name__ == '__main__':
    # 在内存中创建一个空文档
    doc = xml.dom.minidom.Document()
    print doc
    # 创建一个根节点Managers对象
    root = doc.createElement("Managers")
    print u"添加的xml标签为：", root.tagName
    # 给根节点root添加属性
    root.setAttribute('company', 'xx科技')
    value = root.getAttribute('company')
    print u"root元素的'company'属性值为：", value
    # 给根节点添加一个叶子节点
    ceo = doc.createElement('CEO')
    #给叶子节点name设置一个文本节点，用于显示文本内容
    ceo.appendChild(doc.createTextNode('吴总'))
    print ceo.tagName
    print u"给叶子节点添加文本节点成功"
    print ceo.toxml()
