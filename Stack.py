from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,value):
        
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def size(self):

        if self.top == None:
            return "Empty Stack"
        
        temp = self.top
        count = 0

        while temp != None:
            temp = temp.next
            count += 1
        return count

    def pop(self):

        if(self.is_empty()):
            return "Empty Stack"
        else:
            data = self.top.data
            self.top = self.top.next
            return data


s = Stack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(s.pop())
