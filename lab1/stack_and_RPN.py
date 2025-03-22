from arrayStack import Stack

priority = {
    "-": 3,
    "+": 3,
    "*": 2,
    "/": 2,
    "(": 1,
}


def main() -> None:
    infix_expression = input(
        "Provide infix expression\n")
    infix_expression = infix_expression.strip()
    processed_expression = toPostfixWithCorrection(infix_expression)
    print("Processed expression: ", processed_expression)
    evaluated_expression = evaluatePostfix(processed_expression)
    print("Evaluated expression: ", int(evaluated_expression) if int(
        evaluated_expression) == evaluated_expression else evaluated_expression)


def toPostfixWithCorrection(e: str) -> str:
    tokens = e.split(" ")
    operators = Stack[str](len(e))
    result = Stack[str](len(e))
    for t in tokens:
        if t == "(":
            operators.push(t)
        elif t == ")":
            while operators.top() != "(":
                result.push(operators.pop())
            operators.pop()
        elif priority.get(t) == None:
            result.push(t)
        else:
            if operators.size() == 0:
                operators.push(t)
            elif priority[operators.top()] < priority[t]:
                operators.push(t)
            else:
                result.push(operators.pop())
                operators.push(t)

    while operators.size() > 0:
        result.push(operators.pop())

    return " ".join(result.toArray())


def evaluatePostfix(e: str) -> float:
    tokens = e.split(" ")
    stack: Stack = Stack(len(e))
    for t in tokens:
        if t.lstrip('-').isdigit():
            stack.push(int(t))
        else:
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            result = calc(num1, num2, t)
            stack.push(result)

    return stack.pop()


def calc(num1: float, num2: float, operator: str) -> float:
    if operator == "+":
        return num1+num2
    if operator == "-":
        return num2-num1
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num2 / num1
    return 0


if __name__ == "__main__":
    main()
