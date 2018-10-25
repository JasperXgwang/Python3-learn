#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# datetime
from datetime import datetime
from urllib import request, parse

now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%a, %b %d %H:%M'))

# urllib提供了一系列用于操作URL的功能。


with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


