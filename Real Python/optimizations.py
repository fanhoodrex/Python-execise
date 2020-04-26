import collections
from timeit import timeit
Person = collections.namedtuple("Person", "name twitter")
raymond = Person("Raymond", "@raymondh")

a = timeit("raymond.twitter", globals=globals())
b = timeit("raymond.twitter", globals=globals())
print(a)
print(b)