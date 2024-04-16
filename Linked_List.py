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


