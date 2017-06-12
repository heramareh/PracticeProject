#encoding=utf-8
from lettuce import world, steps

def add(number1, number2):
  return number1 + number2

@steps
class FactorialSteps(object):
    """Methods in exclude or starting with _ will not be considered as step"""

    exclude = ['set_number', 'get_number']

    def __init__(self, environs):
        # 初始全局变量
        self.environs = environs

    def set_numbers(self, value1, value2):
        # 设置全局变量中的number1,number2变量的值
        self.environs.number1 = int(value1)
        self.environs.number2 = int(value2)

    def get_numbers(self):
        # 从全局变量中取出number1,number2的值
        return self.environs.number1,self.environs.number2

    def _assert_number_is(self, expected, msg="Got %d"):
        number = self.environs.number
        # 断言
        assert number == expected, msg % number

    def have_the_number(self, step, number1, number2):
        '''I have the numbers (-?\d+),(-?\d+)'''
        # 上面的三引号引起的代码必须写，并且必须是三引号引起
        # 表示从场景步骤中获取需要的数据
        # 并将获得数据存到环境变量number中
        self.set_numbers(number1, number2)

    def i_compute_its_factorial(self, step):
        """When I compute its add"""
        number1, number2 = self.get_numbers()
        # 调用factorial方法进行阶乘结算，
        # 并将结算结果存于全局变量中的number1,number2中
        self.environs.number = add(number1, number2)

    def check_number(self, step, expected):
        '''I see the number (-?\d+)'''
        # 上面的三引号引起的代码必须写，并且必须是三引号引起
        # 表示从场景步骤中获取需要的数据以便断言测试结果
        self._assert_number_is(int(expected))

FactorialSteps(world)
