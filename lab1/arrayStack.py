from typing import Generic, TypeVar, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__length = 0
        self.__array: List[T | None] = [None] * capacity

    def push(self, item: T) -> bool:
        if self.__length < self.__capacity:
            self.__length += 1
            self.__array[self.__length-1] = item
            return True
        return False

    def pop(self) -> T | None:
        if self.__length > 0:
            head = self.__array[self.__length-1]
            self.__length -= 1
            return head
        return None

    def top(self) -> T | None:
        if not self.is_empty():
            return self.__array[self.__length-1]
        return None
    

    def is_empty(self) -> bool:
        return self.__length == 0

    def size(self) -> int:
        return self.__length
