from Node import Node

class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1


    def __str__(self):

        current = self.head
        result = ''

        while current != None:
            result = result + str(current.data) + "->"
            current = current.next

        return result[:-2]


    def append(self,value):

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n += 1


    def insert_after(self,after,value):

        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return "Item not found"

    def clear(self):
        self.head = None
        self.n = 0


    def delet_head(self):
        if self.head == None:
            return "Empty Linked List"

        self.head = self.head.next
        self.n -= 1

    def  pop(self):

        if self.head == None:
            return "Empty Linked List"

        curr = self.head

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n -= 1


x = linked_list()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.pop()
print(x)
