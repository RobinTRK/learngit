#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# %.. & .format about string
#print('hello,%s:%s,you have 0x%x,actually is %4d,%4.2f,%%'%('Michael',100,100,100,100))
#print('hello,{0}:{1},you have 0x{2:x},actually is {3:4d},{4:4.2f},%%,%d,%d'.format('Michael',100,100,100,100)%(100,200))


# about list
#classmates=['a','b','c']
#print(classmates,len(classmates),classmates[0],classmates[1],classmates[2],classmates[-1],classmates[-2],classmates[-3])
#classmates.append('d')
#print(classmates)
#classmates.insert(1,'site1')
#print(classmates)
#print(classmates.pop(1),classmates)
#classmates[1]='c1'
#print(classmates)
#L=['a',1,True]
#S=['a','b',['c','d'],'e']
#print(S[2][2])

# about tuple tuple的永远不变是指，每个元素的指向永远不变，tuple use '(' ')'
# 如果指向的是List，就不能改成指向其他对象，但指向的这个List自身是可变的


# dict 内部存放的顺序和key放入的顺序没关系
#d={'a':1,'b':2,'c':3,'d':4}
#print(d['a'])
#d['e']=5
#print(d['e'])
#d['a']=1.1
#print(d['a'])
#print('f' in d)
#print(d.get('f',-1))

# list & dict 
# dict-查找插入极快，不会随着key增加而变慢，占用大量内存，内存浪费多 空间换时间
# list-相反
# dict的key必须是不可变对象——通过key计算位置->哈希算法——字符串、整数等都是不可变的，可以作为key，list是可变的，不能作为key

# set 和 dict 类似，是一组key的几何，但不储存value


# 定义函数
#def my_abs(x):
#    if not isinstance(x,(int,float)):
#        raise TypeError('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x

#print(my_abs('19'))
#print(my_abs(20))

#import math
#def move(x,y,step,angle=0):
#    nx=x+step*math.cos(angle)
#    ny=y-step*math.sin(angle)
#    return nx,ny

#r = move(100,100,60,math.pi/6)
#print(r)


#
# def add(L=[]):
#     return L
# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('end')
#     return L

# M=None
# if M is None:
#     M=[]
#     print(M)
# print(add_end())
# print(add_end())
# M=None
# if M is None:
#     M=[]
#     print(M)
# print(add(5))
# print(add([1]))
# print(add())
# print(add())


# jdef cale(numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum

# print(cale([1,2,3]))
# print(cale([1,3,5,7]))

# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# def f2(a,b,c=0,*,d=1,**kw):
#     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

# f1(1,2)
# f1(1,2,c=3)
# f1(1,2,3)
# f1(1,2,3,'a','b')
# f1(1,2,3,'a','b',x=99)
# f2(1,2,d=99,ext=None)
# f2(1,2,3,ext=None)
# # f2(1,2,3,4,ext=None)

# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,product*num)

# print(fact(1))
# print(fact(5))
# print(fact(1000))

# def move(n,a,b,c):
#     if n == 1:
#         print(a,'-->',c)
#         return
#     move(n-1,a,c,b)
#     # print(a,'-->',c)
#     move(1,a,b,c)
#     move(n-1,b,a,c)

# move(3,'A','B','C')


# def _odd_iter():
#     n=1
#     while True:
#         n=n+1
#         yield n

# def _not_divisible(n):
#     return lambda x:x%n>0

# def primes():
#     it=_odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(_not_divisible(n),it)

# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

# f = lambda x,y:x*x+y*y

# print(f(5,1))

# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print('a')
# now()
# print('%s' % now.__name__)
# def log1(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():' % (text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
# @log1('execute')
# def now():
#     print('b')

# now()
# print('%s' % now.__name__)


# print("%s" % __name__)

# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

# class Student(object):
#     pass

# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s=Student()
# s.name='Michael'
# print(s.name)
# Student.set_age=MethodType(set_age,Student)
# s.set_age(25)
# print(s.age)
# e=Student()
# e.set_age=MethodType(set_age,e)
# e.set_age(15)
# print(e.age)
# print(s.age)
# f=Student()
# f.set_age=MethodType(set_age,f)
# f.set_age(16)
# print(e.age)
# print(f.age)
# print('finish')

# class Student(object):
#     pass
# from types import MethodType
# def set_score(self,score):
#     self.score=score
# Student.set_score=set_score
# s=Student()
# s.name='michael'
# s.set_score(100)
# s2=Student()
# s2.set_score(99)
# print('%d' %s.score)

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name:%s)'%self.name
#     __repr__=__str__
# print(Student('Michael'))
# s=Student('Micheal')
# print(s)

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
# for n in Fib():
#     print(n)

# class Chain(object):
#     def __init__(self,path=''):
#         self._path=path
#     def __getattr__(self,path):
#         return Chain('%s/%s' % (self._path,path))
#     def __str__(self):
#         return self._path
#     __repr__=__str__
# print(Chain().status.user.timeline.list)

# from enum import Enum
# Month=Enum('Mon',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)

# from enum import Enum,unique
# @unique
# class Weekday(Enum):
#     Sun=0
#     Mon=1
#     Tue=2
#     Wed=3
#     Thu=4
#     Fri=5
#     Sat=6
# day1=Weekday.Mon
# print(day1)
# print(day1.value)

# class Field(object):

#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type

#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)

# print(Field('A',int))

# try:
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('valueError:',e)
# except Exception as e:
#     print('zero',e)
# finally:
#     print('finally...')

# s='0'
# n=int(s)
# print(10)

# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(**kw)
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#     def __setattr__(self,key,value):
#         self[key]=value

# import unittest
# class Dict(dict):

#     def __init__(self, **kw):
#         super().__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value
# class TestDict(unittest.TestCase):
#     def setUp(self):
#         print('setUp')
#     def tearDown(self):
#         print('tearDown')
#     def test_init(self):
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEqual(d.key,'value')
#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'],'value')
#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(KeyError):
#             value=d['empty']
#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value=d.empty
# if __name__=='__main__':
#     unittest.main()

# from io import BytesIO
# f=BytesIO('abc'.encode('utf-8'))
# f.readline()
# print(f.tell())
# f.write(b'123')
# print(f.tell())
# print(f.getvalue())

# import os
# def searchfile(name='Model',path='C:\Work'):
#     os.chdir(path)
#     listall=os.listdir(path)
#     for x in listall:
#         join_path=os.path.join(path,x)
#         if os.path.isfile(join_path) and name in os.path.basename(join_path):
#             print(os.path.dirname(join_path))
#             print(os.path.basename(join_path))
#         elif os.path.isdir(join_path):
#             searchfile(name,join_path)
# searchfile()

# import pickle
# d=dict(name='bob',age=20,score=99)
# print(pickle.dumps(d))
# with open('C:\\Work\\test.txt','wb') as f:
#     pickle.dump(d,f)
# with open('C:\\Work\\test.txt','rb') as f:
#     d=pickle.load(f)
# print(d)

# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('child process %s (%s)'%(name,os.getpid()))
# if __name__=='__main__':
#     print('parent process %s' %os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child end')

# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code',r)

# from multiprocessing import Process,Queue
# import os,time,random
# def write(q):
#     print('Process to write:%s'%os.getpid())
#     for value in ['a','b','c']:
#         print('put %s to ueue'%value)
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('Process to read:%s'%os.getpid())
#     while True:
#         value=q.get(True)
#         print('get %s from queue'%value)
# if __name__=='__main__':
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# import time, threading
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# import time, threading

# # 假定这是你的银行存款:
# balance = 0

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import multiprocessing
# print(multiprocessing.cpu_count())

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)