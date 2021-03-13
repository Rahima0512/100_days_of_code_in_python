'''import time
import sched

s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time(), a)

def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

print_some_times()'''
        
from tkinter import *
def hello(event):
    print("Single Click got as input!!!") 
def quit(event):                           
    print("Double Click got as input , time to stop!!!!!!!!!!!") 
    import sys; sys.exit() 

widget = Button(None, text='Hiii click here buddy!!')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()



class Person: 
    def __init__(self, age = 0): 
         self._age = age 
      
    
    def get_age(self): 
        return self._age 
      
    
    def set_age(self, x): 
        self._age = x 
  
P1 = Person() 


P1.set_age(25) 
  

print(P1.get_age()) 
  
print(P1._age) 