from typing import Any,TypeVar,Generic

T = TypeVar("T")

class Record(Generic[T]):
    id: int
    value: T
    def __init__(self,id:int,value:T):
        self.id = id
        self.value = value

    def get(self)-> T:
        return self.value


class Records:
    def __init__(self,records: list[Record[T]]):
        self.records = records

record1 : Record[str]  = Record(10,"Ten")
record2 : Record[float]  = Record(5,"Five")

records = [
    record1,
    record2
]