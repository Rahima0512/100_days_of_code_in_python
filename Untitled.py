'''class Example(object):
    _itsProblem = "inside protected member"
    def eg(self) :
        print(self._itsProblem)


theExample = Example()
print(theExample.eg())'''

#Program to implement concept of encapsulation
class Example:
    def __init__(self):
         
        self._a = 2
    
class eg(Example):
    def __init__(self):
         
        Example.__init__(self) 
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = eg()
         
obj2 = Example()
print(obj2._a)

#Inheritence implementation
print("******Inheritence implementation******")
class Parent():
       def first(self):
           print('first function')
 
class Child(Parent):
       def second(self):
          print('second function')
 
ob = Child()
ob.first()
ob.second()

    
