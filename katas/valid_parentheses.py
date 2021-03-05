def is_valid(string):
    stack = []
    brackets = {'(':')', '[':']', '{':'}'}
    for i in range(len(string)):
        if string[i] in brackets:
            stack.append(string[i])
        elif stack:
            if brackets[stack.pop()] != string[i]:
                return False
        else:
            return False
    return stack == []




