#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import BytesIO

path = 'E:\data\py.log'

with open(path, 'w') as f:
    f.write("hello python3\n")

with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    print(f.read())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
