class queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)
    
    def delete(self):
        if not self.queue or len(self.queue) < 1:
            return "Queue is Empty"
        return self.queue.pop(0)

    def top(self):
        if not self.queue or len(self.queue) < 1:
            return "Queue is Empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def printQueue(self):
        print(self.queue)


q = queue()

for x in range(1,11):
    q.insert(x)

q.printQueue()

print(q.delete())

q.printQueue()

print(q.delete())
q.printQueue()

print(q.isEmpty())
print(q.top())