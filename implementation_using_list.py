Implementation using list
Python’s buil-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of stack while pop() removes the element in LIFO order.
Unfortunately, list has a few shortcomings. The biggest issue is that it can run into speed issue as it grows. The items in list are stored next to each other in memory, if the stack grows bigger than the block of memory that currently hold it, then Python needs to do some memory allocations. This can lead to some append() calls taking much longer than other ones.

filter_none
edit
play_arrow

brightness_4
# Python program to  
# demonstrate stack implementation 
# using list 
  
  
stack = [] 
  
# append() function to push 
# element in the stack 
stack.append('a') 
stack.append('b') 
stack.append('c') 
  
print('Initial stack') 
print(stack) 
  
# pop() fucntion to pop 
# element from stack in  
# LIFO order 
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
print(stack) 
  
# uncommenting print(stack.pop())   
# will cause an IndexError  
# as the stack is now empty 
Traceback (most recent call last):
  File "/home/2426bc32be6a59881fde0eec91247623.py", line 25, in <module>
    print(stack.pop())  
IndexError: pop from empty list
