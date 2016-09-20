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
                print 'False'
                return
            while stack:
                top = stack.pop()
                if curr == ']' and top == '[':
                    break
                elif curr == '}' and top == '{':
                    break
                elif curr == ')' and top == '(':
                    break
                else:
                    print 'False'
                    return

    if stack:
        print 'False'
    else:
        print 'True'

def main():
    exp = "[}]"
    check_exp(exp)
    
main()