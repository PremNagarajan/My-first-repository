import sys, tty, termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

sys.stdout.write('Email :: ')
email = ""
while True:
    ch = getch()
    if ch == '\r':
        break
    email += ch

res = ""
seen_ast = False
added_first = False
prev = None
for i in range(len(email)):
    if not added_first:
        res += email[i]
        added_first = True
        continue
    
    if seen_ast:
        res += email[i]
        continue
        
    if email[i] == '@':
        seen_ast = True
        if prev:
            res = res[:-1] + prev + email[i]
        else:
            res += email[i]
        continue

    res += '*'
    prev = email[i]
    
print res

sys.stdout.write('Phone :: ')
phone = ""
while True:
    ch = getch()
    if ch == '\r':
        break
    phone += ch

res = ""
for i in range(len(phone)-4):
    if phone[i] == '(' or phone [i] == ')' or phone[i] == ' ':
        continue
    elif phone[i] == '+' or phone[i] == '-':
        res += phone[i]
    else:
        res += '*'
    
for i in range(len(phone)-4, len(phone)):
    res += phone[i]
    
print res

