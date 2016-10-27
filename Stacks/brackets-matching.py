open_exp = ['[', '(', '{']
close_exp = [']', ')', '}']

def check_exp(exp):
    stack = list()
    for i in range(0, len(exp)):
        curr = exp[i]
        if curr in open_exp:
            stack.append(exp[i])
        elif curr in close_exp:
            if not stack:
                return 'False'
            while stack:
                top = stack.pop()
                if curr == ']' and top == '[':
                    break
                elif curr == '}' and top == '{':
                    break
                elif curr == ')' and top == '(':
                    break
                else:
                    return 'False'

    if stack:
        return 'False'
    else:
        return 'True'

def main():
    exp = "[{}]"
    print check_exp(exp)
    
main()