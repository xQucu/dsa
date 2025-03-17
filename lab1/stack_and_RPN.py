from arrayStack import Stack

priority = {
    "+": 4,
    "-": 3,
    "*": 2,
    "/": 2,
    "(": 1,
}


def main() -> None:
    infix_expression = input(
        "Provide infix expression\n")
    processed_expression = toPostfixWithCorrection(infix_expression)
    print("Processed expression: ", processed_expression)
    evaluated_expression = evaluatePostfix(processed_expression)
    print("\nEvaluated expression: ", evaluated_expression)


def toPostfixWithCorrection(e: str) -> str:
    tokens = e.split(" ")
    operators: Stack[str] = Stack(len(e))
    result = ""
    for t in tokens:
        if t == "(":
            operators.push(t)
        elif t == ")":
            while operators.top() != "(":
                result += operators.pop()
            operators.pop()
        elif priority.get(t) == None:
            result += t
        else:
            if operators.size() == 0:
                operators.push(t)
            elif priority[operators.top()] < priority[t]:
                operators.push(t)
            else:
                result += operators.pop()
                operators.push(t)

    while operators.size() > 0:
        # if operators.top() != "(":
        result += operators.pop()
        # operators.pop()

    return result


def evaluatePostfix(e: str) -> int:
    return 0


if __name__ == "__main__":
    main()
