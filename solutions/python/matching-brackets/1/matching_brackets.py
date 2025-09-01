def is_paired(input_string):
    openers = {"(", "{" , "["}
    matches = {")":"(", "]":"[", "}":"{"}
    stack = []

    for ch in input_string:
        if ch in openers:
            stack.append(ch)
        elif ch in matches:
            if not stack or stack[-1] != matches[ch]:
                return False

            stack.pop()
    return not stack
