from Stack import Stack

def revers_string(text):

    s = Stack()

    for i in text:
        s.push(i)
    
    res = ''

    while(not s.is_empty()):
        res = res + s.pop()

    return res


x = revers_string("Hello")
print(x)