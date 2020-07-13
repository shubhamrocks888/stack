class Conversion:

    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting 
        self.output = []
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

    
    # Check if the precedence of operator is strictly 
    # less than top of stack or not
    def precedences(self,operator):
        if len(self.array)==0 or self.array[-1]=='(':
            self.array.append(operator)

        elif self.precedence[self.array[-1]] < self.precedence[operator]:
            self.array.append(operator)
    
        else:
            
            while self.precedence[self.array[-1]] >= self.precedence[operator]:
                
                self.output.append(self.array.pop())
                if len(self.array)==0 or self.array[-1]=='(':
                    break
            self.array.append(operator)

    def infix_to_postfix(self):
        for i in self.capacity:

            if i=='(':
                self.array.append(i)
            
            elif i.isalpha():
                self.output.append(i)

            elif i==')':
                
                while self.array[-1]!='(':
                    self.output.append(self.array.pop())
                self.array.pop()
                
            else:
                self.precedences(i)

        while len(self.array)!=0:
            self.output.append(self.array.pop())


            
    def print_input(self):
        for i in self.output:
            print (i,end="")

z = Conversion("a+b*(c^d-e)^(f+g*h)-i")
z.infix_to_postfix()
z.print_input()


        
        

    

    
