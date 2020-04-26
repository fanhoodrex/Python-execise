# float_check.py
def double(number: float) -> float:
    return 2 * number
double(3.14)
double("I'm not a float")

# draw_line.py
from typing import Literal

def draw_line(direction: Literal["horizontal", "vertical"]) -> None:
    if direction == "horizontal":
        ...  # Draw horizontal line
    elif direction == "vertical":
        ...  # Draw vertical line
    else:
        raise ValueError(f"invalid direction {direction!r}")
draw_line("up")

# calculator.py
from typing import Union

ARABIC_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for arabic, roman in ARABIC_TO_ROMAN:
        count, number = divmod(number, arabic)
        result.append(roman * count)
    return "".join(result)

def add(num_1: int, num_2: int, to_roman: bool = True) -> Union[str, int]:
    """Add two numbers"""
    result = num_1 + num_2

    if to_roman:
        return _convert_to_roman_numeral(result)
    else:
        return result

@overload
def add(num_1: int, num_2: int, to_roman: Literal[True]) -> str: ...
@overload
def add(num_1: int, num_2: int, to_roman: Literal[False]) -> int: ...

# final_id.py
from typing import Final
ID: Final = 1
ID += 1

# final_class.py

from typing import final
@final
class Base:
class Sub(Base):

# typed_dict.py
py38 = {"version": "3.8", "release_year": 2019}

from typing import TypedDict
class PythonVersion(TypedDict):
    version: str
    release_year: int

py38 = PythonVersion(version="3.8", release_year=2019)

# protocol.py

from typing import Protocol

class Named(Protocol):
    name: str

def greet(obj: Named) -> None:
    print(f"Hi {obj.name}")

class Dog:
    name = 'Good Dog'
    
x = Dog()
greet(x)