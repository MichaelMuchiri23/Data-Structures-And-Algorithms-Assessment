def is_balanced(brackets):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for item in brackets:
        if item in opening_brackets:
            stack.append(item)
        elif item in closing_brackets:
            if not stack:
                return False
            if opening_brackets.index(stack.pop()) != closing_brackets.index(item):
                return False
        
    return not stack        
                  
print(is_balanced("[(}]"))
print(is_balanced("()[]"))
