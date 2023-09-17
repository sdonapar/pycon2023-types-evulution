from threading import Lock
from typing import Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

# Use this lock to ensure that only one thread is executing a function
# at any time.
my_lock = Lock()

def with_lock(f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    '''A type-safe decorator which provides a lock.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # Provide the lock as the first argument.
        return f(my_lock, *args, **kwargs)
    return inner

NumType = TypeVar("NumType",float,int)

@with_lock
def sum_threadsafe(lock: Lock, numbers: list[NumType]) -> NumType:
    '''Add a list of numbers together in a thread-safe manner.'''
    with lock:
        return sum(numbers)

# We don't need to pass in the lock ourselves thanks to the decorator.
sum_float = sum_threadsafe([1.1, 2.2, 3.3])
sum_int = sum_threadsafe([1, 2, 5,8])
sum_int_float = sum_threadsafe([1.0,2.5,3,8])

print(sum_int_float)