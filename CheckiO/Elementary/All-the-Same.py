from typing import List,Any

lst = ['Geeks','Geeks', 'Geeks', 'Geeks']  

def all_the_same1(lst): 
    return len(set(lst)) <= 1 # there cannot be duplicate elements in a set
all_the_same1(lst)

# Method 2: Using 
def all_the_same2(elements):
   return elements[1:] == elements[:-1]
all_the_same2(lst)

# Method 3: Lambda
all_the_same3 = lambda e: e[1:] == e[:-1]
all_the_same3(lst)

# Method 4:
def all_the_same4(e):
    return len(e) < 1 or len(e) == e.count(e[0])

# Method 5 : Using iter,next generator
def all_the_same5(elements):
    el = iter(elements)
    first = next(el, None)
    return all(element == first for element in el)
all_the_same5(lst)

# Method 6 : Using Counter
from collection import Counter
def all_the_same6(e):
    return len(Counter(e)) < 2
all_the_same6(lst)


# Method 7: reduce and and_
from functools import reduce
from operator import and_

def all_the_same(elements):
    return reduce(and_ , [a==b for (a, b) in zip(elements, elements[1:])], True)

# Method 8: Using reduce
from functools import reduce
compose = lambda *fs: lambda x: reduce((lambda y, f: f(y)), reversed(fs), x)