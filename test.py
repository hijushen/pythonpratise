# -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85
# r = (s2-s1)/s1 * 100
# print('提高 %.3f %%' %r);
# #len('abc'.encode('utf-8')

# #b'ABC'.decode('ascii')
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# #打印apple
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

#  import math
# def quadratic(a,b,c):
#     f=b**2-4*a*c
#     if f<0:
#       return ('方程无解')
#     elif f==0:
#       return (-b/(2*a))
#     else:
#       x1=(-b-math.sqrt(f))/(2*a)
#       x2=(-b+math.sqrt(f))/(2*a)
#       return (x1,x2)
# print(quadratic(4,8,2))
# print(quadratic(1,2,3));    
# def power(x,n):
#     s = 1
#     while n> 0:
#         n = n -1 
#         s = s*x
#     return s

# print(power(2,4));

# 默认参数指向不可变对象
# def add_END(L=None):
#     if L is None:
#         L = [];
#     L.append('END');
#     return L;

# print(add_END(['1','2']));
# print(add_END());
# print(add_END());
# print(add_END(['1','2']));

## 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# nums = [1,2,3];
# print(calc(*nums))


## 关键字参数
# def person(name, age, **kw):
#     print('name',name, ' age: ',age, ' other: ',kw);

# person('michale',30,city='beijing', job='error')    

## 递归
# def fact(n):
#     if n == 1:
#         return n;
#     else:
#         return n*fact(n-1);

##尾递归
# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)   

# print(fact(3))

##汉诺塔
# def Hanno1(n):
#     Hanno(n,*('a','b','c'));

# list_d = []
# def Hanno(n, a,b,c):
#     if(n==1):
#         list_d.append(a + ' --> ' + c)
#     else:
#         Hanno(n-1,a,c,b);
#         list_d.append(a + ' --> ' + c)
#         Hanno(n-1,b,a,c)

# Hanno1(3)
# print(list_d)  
# 
# 高级特性
## 切片
# L = list(range(100))
# print(L)
# print(L[:10])     
# print(L[-10:])
# print(L[10:20])
# print(L[:10:2])
# print(L[::5])
# print(L[:])
# print('abcdefg'[:3])
# print('dfdfdfdf'[::2])

## 迭代
### for in
# d={'a':1,'b':2,'c':3}
# for value in d.values():
#     print(value)

# for key in d:
#     print(key)

# for k,v in d.items():
#     print(k + ": " + str(v))

## 列表生成器
# print(list(range(1,11)))
# print([x * x  for x in range(1,11)])
# print([m+n for m in 'abc' for n in 'xyz'])
# L = ['Hello', 'World', 18 , 'Apple',None]
# L2 = [x.lower() for x in L if isinstance(x,str)]
# print(L2)

# from collections import Iterator
# print(isinstance((x for x in range(10)),Iterable))
# print(isinstance(100, Iterable))
# print(isinstance(iter('abc'), Iterator))

# print((1,2,3,4)[2])
# print({'0':0,'1':1,'2':2,'3':3}['2']) #好厉害

# s = set((1,[2,3)])
# print(list(s))

# l = sorted([36,5,-12,9,-21], key =abs,reverse=True)
# print(l)

# L = [('Bob',75),('Adam',92),("bart",66),("Lisa",88)]
# # print(sorted(L,key=itemgetter(0)))
# def by_name(t):
#     # print(t)
#     return t[0].lower()

# def by_score(t):
#     return t[1]
# # L2 = sorted(L,key=by_name);
# # print(L2);    
# L3 = sorted(L,key=by_name,reverse=True)
# print(L3)

# def not_empty(s):
#     return s and s.strip()

# l = list(filter(not_empty, ['a','','b','',None,'c','   ']))
# print(l)


# def is_palindrome(n):
#     if(n < 10): return False    
#     L1 = [x for x in str(n)]
#     return L1 == L1[::-1]

# output = filter(is_palindrome,range(1,1000))
# print(list(output))

# de

# def count():
#     def f(j):
#         def g():
#             return j *j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs    

# f1,f2,f3 = count();
# print(f1())
# print(f2())
# print(f3())
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' %func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):

# @log
# def now():
#     print('2017-7-18');


# now()
# 偏函数 固定住某个值
# int2 = functools.partial(int,base=2)
# m = int2('10000')
# print(m)