#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


today()
print(today.__name__)


def metric(fn):
    @functools.wraps(fn)
    # *args 可变参数
    # **kw  关键字参数 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time();
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')

print(int('1010101', base=2))
int2 = functools.partial(int, base=2)
print(int2('1010101'))
