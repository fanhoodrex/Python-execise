# The lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:
add_ = lambda x,y:x+y
a = add_(5,3)
print(a)

# You could declare the same add() 
# function with the def keyword:
def add(x,y):
    return x+y
b = add(5,3)
print(b)

# So what's the big fuss about?
# Lambdas are *function expressions*:
c = (lambda x,y:x+y)(5,3)
print(c)

# • Lambda functions are single-expression 
# functions that are not necessarily bound
# to a name (they can be anonymous).

# • Lambda functions can't use regular 
# Python statements and always include an
# implicit `return` statement.