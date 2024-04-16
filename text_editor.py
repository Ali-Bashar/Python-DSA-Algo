from Stack import Stack

def text_editor(text,pattern):

    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == "u":
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)

    res = ""

    while(not u.is_empty()):
        res = u.pop() + res

    return res


x = text_editor("Hello","uuu")
print(x)