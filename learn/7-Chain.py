#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import unique, Enum


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if type(gender) == Gender:
            self.gender = gender
        else:
            raise TypeError('输入有误')

    def __str__(self):
        return '%s:%s' % (self.name, self.gender)


if __name__ == '__main__':
    jasper = Student('jasper', Gender.Male)

    print(jasper)
