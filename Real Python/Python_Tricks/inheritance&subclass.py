# You can check for class
# inheritance relationships 
# with the "issubclass()" built-in:

class BaseClass:pass
class SubClass(BaseClass):pass

print(issubclass(SubClass, BaseClass))
print(issubclass(SubClass, object))
print(issubclass(BaseClass, SubClass))