#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

# print(os.environ)

print(os.environ.get('path'))

dirs = [x for x in os.listdir('D:\Programs') if os.path.isdir(x)]
print(list(dirs))

