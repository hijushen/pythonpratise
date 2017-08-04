#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-

'a test module'

_author_ = 'test ge'

# import sys
# def test():
#     args = sys.argv
#     if len(args) ==1:
#         print('Hello World')
#     elif len(args) ==2:
#         print('Hello %s!' %args[1])
#     else:
#         print('Too many args')

# if __name__=='__main__':
#     test()

# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score= score

#     def print_score(self):
#         print("大家%s: %d" %(self.__name,self.__score))

# # def print_score(std):
# #     print("%s: %s" %(std.name, std.score))
# bar = Student('li',23)
# bar.print_score()
# print(bar._Student__score)
# # print_score(bar)
# # bar.name = 'zhang'
# # print(bar.name)
# # print(bar.score)
# # print(bar)

# class Animal(object):
#     def run(self):
#         print('Animal myself')

# class Dog(Animal):
#     def run(self):
#         print('dog here')

# class Duck(Animal):
#     def run(self):
#         print('Duck here')

# def print_twice(an):
#     an.run()


# print_twice(Dog())
# print_twice(Duck())
# print_twice(Animal())

# import math
# print(round(1.755,2))
# print(round(1.7555,3))
# print("%.2f" % 1.755)
# print("%.3f" % 1.7555)

class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'zs'
s.age = '14'
print(s.name + ' ' + s.age)

#使用__slotes__限定了对象类型
# s.addr = 'unknown1'
#print(s.name + ' ' + s.age + ',.:' + s.addr)
