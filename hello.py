#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-


# 余额宝 = 23742.70
# # l余额宝 = 4.0240
# 网商银行 = 1150
# # l网商银行= 3.8
# 京东金融 = 5057.51
# # l京东金融 = 4.5106
# 微信理财通 = 2280.41
# # l微信理财通 = 4.2410
# qq理财通 = 4122.20
# # lqq理财通 = 4.09

# sum = 余额宝 +网商银行 +京东金融+微信理财通+qq理财通
# print(sum)


# from enum import Enum
# 'a test module'

# _author_ = 'test ge'


# Month = Enum('Month', (
#     'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
#     ))

# for name, member in Month.__members__.items():
#     print(name, '==>', member, ',', member.value)
# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):  # 定义可以实例的方法, 而不需要类.方法()来使用
#         print('My name is %s' % self.name)


# s = Student('DageDa')
# s()
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path

#     def __getattr__(self, path):  # 链式调用, 不清楚
#         return Chain('%s/%s' % (self._path, path))

#     def __str__(self):
#         return self._path

#     __repr__ = __str__


# print(Chain().status.timeline.list)  # /status/timeline/list 链式调用
# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self, attr):  # 对所有未经定义的属性设置,找不到attr就来这里找
#         if attr == 'score':
#             return 99
#         elif attr == 'age':
#             return lambda: 25
#         else:
#             pass


# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())  # 返回函数都木得问题啊
# print(s.sex)  # 默认返回None, 所以输出None

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化开始
    
#     def __iter__(self):  # 返回自身数据
#         return self
    
#     def __next__(self):  # 迭代器访问内容
#         self.a, self.b = self.b, self.a + self.b
#         if(self.a > 10000):
#             raise StopIteration()
#         return self.a
    
#     def __getitem__(self, n):  # 可以使用索引下标[]形式访问list
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a+b
#         return a


# for n in Fib():
#     print(n)

# print(Fib()[5])


# class  Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Student object (name %s)' % self.name


# print(Student('Michael'))
# s = Student('lili')
# s


# #生父
# class Father():
#     def func(self):
#         print('生父打儿子')


# #隔壁老王
# class LaoWang():
#     def func(self):
#         print('老王打儿子')
        
        
# #继父
# class StepFather():
#     def func(self):
#         print('继父打儿子')


# #神秘人
# class Mysterious(StepFather,Father,LaoWang):
#     pass


# ##让我们看看到底谁打了儿子
# s=Mysterious()
# s.func()

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

# class Student(object):
#     __slots__ = ('name', 'age')


# s = Student()
# s.name = 'zs'
# s.age = '14'
# print(s.name + ' ' + s.age)


# s = Student()
# s.name = 'zs'
# s.age = '14'
# print(s.name + ' ' + s.age)
# 使用__slotes__限定了对象类型
# s.addr = 'unknown1'
# print(s.name + ' ' + s.age + ',.:' + s.addr)

# test224
# test2234
# class Screen(object):
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value

#     @property
#     def resolution(self):
#         return self._width * self._height


# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# # assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution