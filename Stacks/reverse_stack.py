def insert_at_bottem(s, element):
    if not s:
        s.append(element)
    else:
        top = s.pop()
        insert_at_bottem(s, element)
        s.append(top)

def reverse_stack(s):
    if not s:
        return
    last = s.pop()
    reverse_stack(s)
    insert_at_bottem(s, last)
    
s = list()
s.append(1)
s.append(2)
s.append(3)
print s
reverse_stack(s)
print s