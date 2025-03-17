from arrayStack import Stack

priority = {
    "+": 2,
    "-": 2,
    "*": 1,
    "/": 1,
}


def main() -> None:
    infix_expression = input(
        "Provide infix expression with reversed priority\n")
    processed_expression = toPostfixWithCorrection(infix_expression)
    print("Processed expression: ", processed_expression)
    evaluated_expression = evaluatePostfix(processed_expression)
    print("\nEvaluated expression: ", evaluated_expression)


def toPostfixWithCorrection(e: str) -> str:
    tokens = e.split(" ")
    for t in tokens:
        print(t, priority[t])
    return ""


def evaluatePostfix(e: str) -> int:
    return 0


if __name__ == "__main__":
    main()
