while True:
    stack = []
    txt = input()
    
    if txt == '.':
        break
    
    for ch in txt:
        if ch == '[' or ch == '(':
            stack.append(ch)
        
        elif ch == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')