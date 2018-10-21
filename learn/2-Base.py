#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的语法比较简单，采用缩进方式，写出来的代码就像下面的样子：
a = 100
if a > 0:
    print(a)
else:
    print(-a)

print('''line1
line2
line3''')

# r''表示''内部的字符串默认不转义
print(r'''hello,\n
world''')

age = 10;
if age <= 18:
    print("未成年")
else:
    print("成年人")

a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

x = 10
x = x + 2
print(x)

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

print(ord('中'))
print(chr(20013))

name = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(name)

tips = 'Hi, %s, you have $%d. %s' % ('Michael', 1000000,"thinks")
print(tips)
