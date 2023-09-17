from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex) # 

Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector[T]) -> T:
    return sum(x*y for x, y in v)
def dilate(v: Vector[T], scale: T) -> Vector[T]:
    return ((x * scale, y * scale) for x, y in v)
vec = []  # type: Vector[float]


from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex) # 

def inproduct( v: Iterable[Tuple[T, T]] )-> T:
    return sum(x*y for x, y in v)
def dilate(v: Iterable[Tuple[T, T]], scale: T) -> Vector[T]:
    return ((x * scale, y * scale) for x, y in v)
vec = []  # type: Vector[float]