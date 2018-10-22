#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        # 抛出异常
        raise TypeError("bad operand type")
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-99))


# print(my_abs('A'))


# 返回多个值,Python的函数返回多值其实就是返回一个元组tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(0, 0, 10, 45))


def quadratic(a, b, c):
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type')

    delta = b * b - 4 * a * c
    if a == 0:
        x0 = -c / b
        return x0
    elif delta < 0:
        return ('此方程无解')
    elif delta == 0:
        x1 = x2 = -b / 2 * a
        return x1, x2
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        return x1, x2


# a = int(input('请输入a的值:'))
# b = int(input('请输入b的值:'))
# c = int(input('请输入c的值:'))
# print(quadratic(a, b, c))


# 默认参数不能在前
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=[]):
    L.append("end")
    return L


print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i * i
    return sum


print(calc(*[1, 2, 3]))
print(calc(1, 2, 3))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


# 命名关键字参数  *后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person('Jack', 24, 'Beijing', 'Engineer')


def product(x, *y):
    result = x
    for i in y:
        result = result * i
    return result
