class A(object):
  def __init__(self):
   pass

  def foo(self):

    print('A foo')

class B(object):
  def __init__(self):
   pass

  def foo(self):

    print ('B foo')

class C(B,A): #print out:B foo
#class C(A,B) #print out:A foo
 def __init__(self):

    pass

 

testc = C()

testc.foo()