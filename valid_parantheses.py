def isValid(self, s: str) -> bool:
    stack = []

    for par in s:
        if par == "(" or par == "[" or par == "{":
            stack.append(par)
        else:
            if stack == []:
                return False
            check = stack.pop()
            if check == "(" and par != ")":
                return False
            if check == "[" and par != "]":
                return False
            if check == "{" and par != "}":
                return False

    if stack == []:
        return True
    else:
        return False
