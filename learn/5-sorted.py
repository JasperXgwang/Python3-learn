#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(m):
    return m[0]


def by_score(m):
    return m[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
