#encoding=utf-8

import json, re

def test_json_dumps(str):
    try:
        return json.dumps(str)
    except:
        return None

def test_json_loads(str):
    try:
        return json.loads(str)
    except:
        return None

def re_search(str):
    try:
        return re.search(r'{"code":\d+,"userid":\d{1,10}}', str).group()
    except:
        return None

class Employee(object):
    def __init__(self, name, age, sex, tel):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel

    # 将序列化函数定义到类里面
    def obj_json(self, obj_instance):
        return {
            'name': obj_instance.name,
            'age': obj_instance.age,
            'sex': obj_instance.sex,
            'tel': obj_instance.tel}

if __name__ == '__main__':
    # print re_search('{"code":1,"userid":10000}')
    # print re_search('{"code":15,"userid":1001233410}')
    # print re_search('{"code":1,"userid":10012334100}')
    a = [{1: 12, 'a': 12.3}, [1, 2, 3], (1, 2), 'asd', u'ad', 12, 13L, 3.3, True, False, None]
    print u"Python类型:    ", a
    print u"编码后的json串:", json.dumps(a)

    data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
    # sort_keys：排序，默认为False
    print json.dumps(data)
    print json.dumps(data, sort_keys=True)

    # indent：缩进
    print json.dumps(data, sort_keys=True, indent=3)

    # separators：去掉编码后的json串中  ,和:后面的空格
    print len(json.dumps(data))
    print len(json.dumps(data, separators=(',', ':')))

    # skipkeys可以跳过那些非string对象的key的处理
    data= [ { 'a':'A', 'b':(2, 4), 'c':3.0, (1,2):'D tuple' } ]
    print u"不设置skipkeys 参数"
    try :
      res1 = json.dumps(data) #skipkeys参数默认为False时
    except Exception, e:
      print e

    print u"设置skipkeys 参数"
    print json.dumps(data, skipkeys=True)# skipkeys=True时

    a = [{1: 12, 'a': 12.3}, [1, 2, 3], (1, 2), 'asd', u'ad', 12, 13L, 3.3, True, False, None]
    print u"编码后\n", json.dumps(a)
    print u"解码后\n", json.loads(json.dumps(a))

    # 将类对象编码成json串
    emp = Employee('Lily', 24, 'female', '18223423423')
    print u"将类对象编码成json串"
    print json.dumps(emp, default=emp.obj_json)
    print json.dumps(emp.obj_json(emp))

    # 使用__dict__方法获取类或类实例中有效的属性
    emp = Employee('Lily', 24, 'female', '18223423423')
    print emp.__dict__
    print(json.dumps(emp, default=lambda Employee: Employee.__dict__))
    print(json.dumps(emp, default=lambda emp: emp.__dict__))

    # json反序列化为类对象
    emp = Employee('Lily', 24, 'female', '18223423423')
    def jsonToClass(emp):
        return Employee(emp['name'], emp['age'], emp['sex'], emp['tel'])

    json_str = '{"name": "Lucy", "age": 21, "sex": "female", "tel": "15834560985"}'
    e = json.loads(json_str, object_hook=jsonToClass)
    f = jsonToClass(json.loads(json_str))
    print e
    print e.name
    print f
    print f.name
