#encoding=utf-8

from lettuce import *

# 用于计算整数的加法函数
def add(numbers):
    return reduce(lambda x,y:int(x)+int(y),numbers)

@step('I have the number (-?\d+,-?\d+)')
def have_the_numbers(step, number):
    # 将通过正则表达式匹配的数字存于全局变量world中
    world.numbers = number.split(',')

@step('I compute its add')
def compute_its_factorial(step):
    # 从全局变量world中取出匹配的数字，
    # 计算其阶乘，并将结果再存回world中
    world.number = add(world.numbers)

@step('I see the number (-?\d+)')
def check_number(step, expected):
    # 通过正则匹配到预期数字
    expected = int(expected)
    # 断言计算阶乘结果是否等于预期
    assert world.number == expected, "Got %d" %world.number
