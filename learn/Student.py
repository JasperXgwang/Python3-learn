#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    # toString
    def __str__(self):
        return 'Student object (name: %s)' % self.__name


if __name__ == '__main__':
    bart = Student("bart", 60)
    lisa = Student("lisa", 90)

    bart.print_score()
    lisa.print_score()

    print(bart)


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
