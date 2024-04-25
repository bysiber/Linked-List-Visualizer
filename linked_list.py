class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

class LinkedList():
    def __init__(self):
        self.head = None
    
    def get_last_node(self):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        return temp

    def add_node(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            last_node = self.get_last_node()
            last_node.next = Node(data)
            last_node.next.prev = last_node
    
    def print_nodes(self):
        temp = self.head
        counter = 1
        while(temp != None):
            print(f"{counter}.Node.data = {temp.data}")
            temp = temp.next
