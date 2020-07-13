##1. check if it is an alphabet, if it is add to the stack.
##2. if it is an '(' then add to the stack.
##3. if it is an ')' then pop the stack until '(' is found and at last '(' is pop.
##4. if it is an operator:
##    1. check length, if it is empty then add to the stack.
##    2. if its not check the precedence if its higher then add to the stack.
##    3. if its not pop the operator until its precedence is lower  and stop until length is 0 or '(' is found


class Conversion:

    def __init__(self,capacity):
    
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting 
        self.output = []
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

    def isempty(self):
        if len(self.array)==0:
            return True
        return False

    def peek(self):
        return self.array[-1]

    def push(self,op):
        self.array.append(op)

    def pop(self):
        if not self.isempty():
            return self.array.pop()
        return False
        
    # Check if the precedence of operator is strictly 
    # less than top of stack or not
    def precedences(self,operator):
        if self.isempty() or self.peek()=='(':
            self.push(operator)

        elif self.precedence[self.peek()] < self.precedence[operator]:
            self.push(operator)
    
        else:
            
            while self.precedence[self.peek()] >= self.precedence[operator]:
                
                self.output.append(self.pop())
                if self.isempty() or self.peek()=='(':
                    break
            self.push(operator)

    def infix_to_postfix(self):
        for i in self.capacity:
            if i.isalpha():
                self.output.append(i)

            elif i=='(':
                self.push(i)
            
            elif i==')':
                
                while self.peek()!='(':
                    self.output.append(self.array.pop())
                self.pop()
                
            else:
                self.precedences(i)

        while not self.isempty():
            self.output.append(self.pop())

    def print_input(self):
        for i in self.output:
            print (i,end="")

z = Conversion("a+b*(c^d-e)^(f+g*h)-i")
z.infix_to_postfix()
z.print_input()




        
        

    

    
