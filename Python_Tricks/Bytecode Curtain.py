# You can use Python's built-in "dis"
# module to disassemble functions and
# inspect their CPython VM bytecode:

def greet(name):
    return 'Hello,'+name+'!'
a = greet('Dan')
print(a)

import dis
dis.dis(greet)
