from arrayStack import Stack
from singlyLinkedList import SinglyLinkedList


def main() -> None:
    # print("Is Palindrome" if (i := input("Provide string\n")) == i[::-1] else "Not Palindrome")
    s = input("Provide string to check if it is palindrome\n")
    s = ''.join(c for c in s.lower().strip() if c.isalnum())
    if isPalindrome(s):
        print("It is a palindrome")
    else:
        print("It is NOT a palindrome")


def isPalindrome(s: str) -> bool:
    stack = Stack[str](len(s))
    singlyList: SinglyLinkedList = SinglyLinkedList()

    for v in s:
        stack.push(v)
        singlyList.add(v)

    while singlyList.size() > 0 and singlyList.size() > 0:
        if stack.pop() != singlyList.remove():
            return False

    return True


if __name__ == "__main__":
    main()
