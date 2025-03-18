from arrayStack import Stack
from singlyLinkedList import SinglyLinkedList


def main() -> None:
    # print("Is Palindrome" if (i := input("Provide string\n")) == i[::-1] else "Not Palindrome")
    s = input("Provide string to check if it is palindrome\n")
    if isPalindrome(s):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


def isPalindrome(s: str) -> bool:
    stack: Stack = Stack(len(s))
    list: SinglyLinkedList = SinglyLinkedList()

    for v in s:
        stack.push(v)
        list.add(v)

    while list.size() > 0 and list.size() > 0:
        if stack.pop() != list.remove():
            return False

    return True


if __name__ == "__main__":
    main()
