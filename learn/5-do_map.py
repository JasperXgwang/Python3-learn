#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

'''
  lower()、upper()、capitalize()、title()、swapcase()
  这几个方法分别用来将字符串转换为小写、大写字符串、将字符串首字母变为大写、将每个首字母变为大写以及大小写互换，
  这几个方法都是生成新字符串，并不对原字符串做任何修改 
'''


def normalize(name):
    return name[0].upper() + name[1:len(name)].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# def prod(L):
#     # return reduce(lambda x, y: x * y, L)
#     return reduce(prodF, L)
#
#
# def prodF(x, y):
#     return x * y


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(x):
        return DIGITS[x]

    return reduce(fn, map(char2num, s))


print(type(str2int("123")))

# def str2float(s):
#     p = s.index('.')
#     s1 = s[0:p]
#     s2 = s[(p + 1):]
#
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#         DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return DIGITS[s]
#
#     return reduce(fn, map(char2num, s1)) + reduce(fn, map(char2num, s2))(10 ** (0 - len(s2)))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
