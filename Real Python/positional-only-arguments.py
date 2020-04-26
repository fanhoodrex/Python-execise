def incr(x, /):
    return x + 1
print(a := incr(3.8))

def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"
print(b := greet("Christopher"))
print(c := greet("Christopher", greeting="Awesome job"))

def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5
print(d := to_fahrenheit(celsius=40))

def headline(text, /, border="~", *, width=50):
    return f" {text} ".center(width, border)
print(e := headline("Python 3.8", "="))
print(f := headline("Real Python", border=":"))
print(g := headline("Python", "@", width=38))