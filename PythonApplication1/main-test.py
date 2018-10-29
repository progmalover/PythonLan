import math
#from os import getcwd
from os import *
from functools  import *
import os as _os
import calendar
import urllib
import html
import http
 
 

__test__=["this","is","an","test"]
t = ("test","demo","this","job")

for  val in enumerate(t):
    print(val)

for i in range(len(t)):
    print(t[i])

for var in t:
    print(var)

l = list(t)
del l[0]
del l[0]
print(l)

for i in range(len(l)):
    print(l[i])

for s in l:
    print(s)

for  val in enumerate(l):
    print(val)

#a = unichr(233)
#print(a)

#str =input("请输入：")
#print("inputstr is:"+ str)

print("\n"*2)
print(_os.getcwd())

print("os items:")
vlist = dir(_os)
print(vlist)

print("\n"*2)
print("calendar items:")
print(dir(calendar))

import time
print("\n"*2)
m = time.localtime()[1]
print(calendar.month(m,1))

 
print("\n"*2)
print(dir(time))
print("timezone:" ,time.timezone)

_map={
0x10:"test1",
0x20:"test2",
0x30:"test3"
   
}
print(type(_map))
#print()
print(_os.name)
#print()

t = lambda x: x**2
for i in range(1,6):
 print(t(i))

def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()

from  ctypes import *
try:
    libc = cdll.msvcrt
except Exception as ee:
    print(ee.args)
else:
    print("success")
finally:
    print("finally")
libc.printf("hello libc")


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

'''
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
'''
 

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (type(e.args))
else:
    print("yes success")

"""
a=[99,88,77,66]
if __name__ == '__main__':
    N = len(a) 
    print(a)
    for i in range(int(len(a) / 2)):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print(a)


x=[1,2,3,4]
y=[5,6,7,8]   
aa = [a + b for a in x for b in y if a%2 == 0 and b%2 ==0]
print(aa)


def a(**x):print(x)
a(x=1,y=2,z=3)

from threading import *

i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)

aa=[1,2,3,5]
bb = aa[:]
print(bb)
aa[0]=3
print(bb)
 

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)
 
Sn = reduce(lambda x,y : x + y,Sn)
print ("计算和为：",Sn)
"""

import weakref
class C :

    def __init__(self):
        self.s_status = True
        self._status=4
        self.__status = 5
       
    def method(self):
        print("method called!" ,self.s_status)

class D(C):
        def __init__(self):
            C.__init__(self)
            print(self.s_status)
            print(self._status)
#           print(self.__status) """ this will occur exception"""

d=D()
c = C()
rr = weakref.ref(c)
print(type(rr))

oo = rr()
if oo is not None:
    oo.method();
else:
    print("weakref released!");

rr = weakref.WeakMethod(c.method)
rr()()

del c
#del rr
del oo
oo=rr()
if oo is None:
    print("c released!")
else:
    print("not release!")
if rr._alive :
      print("rr alive!")
else:
      print("rr un-alive")

def _get_exports_list(module):
    try:
        return list(module.__all__)
    except AttributeError:
        return [n for n in dir(module) if n[0] != '_']

#_get_exports_list(module = PythonApplication1)
"""
strlist=["a","b","ccc","aaa","ddd"]
def _get_yield_try():
      yield from strlist
yyl = _get_yield_try()
print(yyl)
for a in yyl:
    print(a)

def _get_yield_try2(size = 0):
    i = 0
    while i < size :
        i = i+1
        if i % 2 == 1:
            yield i

yyl2 = _get_yield_try2(100)

#for i in range(10):
#ttl = yyl2.next() 
for ttl in yyl2:
    print(ttl)
"""

 
import threading
import time
import random

tcount = 0;
lock = threading.Lock()
cond = threading.Condition( threading.Lock())
 
def threadfunc():
    global lock
    global tcount
    global cond
    wt = random.randint(1,9)% 5 
    time.sleep(wt )
    lock.acquire()
    tcount+=1
    lock.release()
    cond.acquire()
    #cond.wait()
    print( "count " + str(tcount) + " thread " + str(threading.get_ident()) + " wait " + str(wt)) 
    #cond.notify()
    cond.release()

def threadnotify():
    global cond
    cond.acquire()
    time.sleep(10)
   # cond.notify()
    cond.release()
  

q = []

ttrd = threading.Thread(target=threadnotify)
ttrd.start()

for i in range(5):
    q.append(threading.Thread(target=threadfunc))

for j in range(5):
    q[j].start()

for j in range(5):
    q[j].join()

#from module1 import *
import module1
from module1 import *
def print_import_vars():
    print(gl_test2)
    print(gl_test1)
    print(_gl_test3)
    print(dir(module1))

if __name__ == "__main__":
    print_import_vars()


    