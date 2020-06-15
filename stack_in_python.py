# Python program for implementation of stack 
# import maxsize from sys module  
# Used to return -infinite when stack is empty 


##Pros: The linked list implementation of stack can grow and shrink according to the needs at runtime.
##Cons: Requires extra memory due to involvement of pointers.


from sys import maxsize

# Function to create a stack. It initializes size of stack as 0
def create_stack():
    stack = []
    return stack

# Stack is empty when stack size is 0

def is_empty(stack):
    return len(stack)==0

# Function to add an item to stack. It increases size by 1
def push(stack,item):
    stack.append(item)
    print(item ,"pushed to satck")


# Function to remove an item from stack. It decreases size by 1
def pop (stack):
    if is_empty(stack):
        return str(-maxsize -1)

    return stack.pop()

# Function to return the top from stack without removing it
def peek(stack):
    if is_empty(stack):
        return str(-maxsize -1)
    return stack[-1]
s = create_stack()
push(s,1)
push(s,2)
push(s,3)
print(pop(s))
print(pop(s))
print(pop(s))
print(pop(s))
