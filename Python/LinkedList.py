class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def appendNodes(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        
    
ll = LinkedList()
ll.appendNodes(1)
ll.appendNodes(2)
ll.appendNodes(3)

ll.printLinkedList()