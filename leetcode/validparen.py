def isValid(s: str) -> bool:
    

    # so first i need to see the String 
    # and then use a stack, so 
    # if i see an open paren (,{,[, then i push/append
    # the closed paren on the stack ),},] 
    #  and then 
    # once i see the closed paren, when i go through the string
    #  we pop the closed charater
    mystack = []
    for ch in s:
        if ch == '(':
            mystack.append(')')
        elif ch == '{':
            mystack.append('}')
        elif ch == '[':
            mystack.append(']')
        else:
            if not mystack or ch != mystack.pop():
                return False
    return not mystack

s = "({[]}"
print(isValid(s))