#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数

# 利用递归函数移动汉诺塔:
# 因为汉诺塔的游戏规则是从大到小，一次往上排序

# 第一步：所以在A柱有三个圆盘的时候首先要把上面2个较小的圆盘移动到B柱

# 第二步：此时再将A柱下最大的圆盘直接移动到C柱

# 第三步：这时候再将B柱上的两个圆盘再移动到C柱上

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
