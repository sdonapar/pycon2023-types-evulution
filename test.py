from typing import TypeVar

T = TypeVar("T")

def my_func(l:list[T]) -> T:
    return l[0]

my_func([1,2,"text"])