
def is_valid(s: str) -> bool:
    stack = []
    parenthesis = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for i in s:
        if i in parenthesis:
            stack.append(i)
        else:
            if not stack:
                return False
            if parenthesis[stack.pop()] != i:
                return False
    return len(stack) == 0


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
