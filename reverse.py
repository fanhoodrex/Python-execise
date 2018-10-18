#Python code to reverse a string  
#using loop 
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

# Python code to reverse a string  
# using recursion 
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

# Python code to reverse a string  
# using extended slice syntax  
# Function to reverse a string 
def reverse(string): 
    string = string[::-1] 
    return string 

# Python code to reverse a string  
# using reversed() 
# Function to reverse a string 
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
print (reverse('abc'))

