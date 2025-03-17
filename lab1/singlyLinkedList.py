from typing import Generic, TypeVar, List, Optional
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__length = 0

    def add(self, item: T) -> None:
        new_node = Node(item)
        if self.__tail is None:
            self.__head = new_node
        if self.__tail is not None:
            self.__tail.next = new_node
        self.__tail = new_node
        self.__length += 1

    def remove(self) -> Optional[T]:
        if self.__head is None:
            return None

        item = self.__head

        if self.__length == 1:
            self.__head = None
            self.__tail = None
            self.__length -= 1
            return item.value

        self.__head = self.__head.next
        self.__length -= 1
        return item.value

    def peek(self) -> Optional[T]:
        if self.__head is not None:
            return self.__head.value
        return None

    def size(self) -> int:
        return self.__length