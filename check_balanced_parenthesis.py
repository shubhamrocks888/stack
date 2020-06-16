##Check for balanced parentheses in an expression
##Given an expression string exp , write a program to examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.

##the main algo is LAST UNCLOSED FIRST CLOSED

# Python3 program to check for 
# balanced parenthesis. 

# function to check if 
# paranthesis are balanced 
def areParanthesisBalanced(expr) : 
	stack = [] 

	# Traversing the Expression 
	for char in expr: 
		if char in ["(", "{", "["]: 

			# Push the element in the stack 
			stack.append(char) 
		else: 

			# IF current character is not opening 
			# bracket, then it must be closing. 
			# So stack cannot be empty at this point. 
			if not stack: 
				return False
			current_char = stack.pop() 
			if current_char == '(': 
				if char != ")": 
					return False
			if current_char == '{': 
				if char != "}": 
					return False
			if current_char == '[': 
				if char != "]": 
					return False

	# Check Empty Stack 
	if stack: 
		return False
	return True


# Driver Code 
if __name__ == "__main__" : 
	expr = "{(a)}[]"; 
	if areParanthesisBalanced(expr) : 
		print("Balanced"); 
	else : 
		print("Not Balanced"); 






##SELF MADE CODE






##def check_parenthesis(expr):
##    stack = []
##
##    for i in expr:
##        if i in ['(','{','[']:
##            stack.append(i)
##        else:
##            if len(stack)==0:
##                 print ("unbalanced")
##                 return
##                
##            elif i==')' and stack[-1]=='(':
##                stack.pop()
##            elif i=='}' and stack[-1]=='{':
##                stack.pop()
##            elif i==']' and stack[-1]=='[':
##                stack.pop()
##            else:
##                print ("unbalanced")
##                return
##
##    if len(stack)==0:
##        print ("Balanced")
##        return
##    print("Unbalanced")
##
##
##
##
##
##if __name__ == "__main__":
##    expr = "(a){}[]{}[]"
##    check_parenthesis(expr)
