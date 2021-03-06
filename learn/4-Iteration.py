#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
for val in d.values():
    print(val)
for k, v in d.items():
    print(k, v)


def findMinAndMax(L):
    if len(L) <= 0:
        return None, None
    min = max = L[0]
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
