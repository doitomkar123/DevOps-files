class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.stack or len(self.stack) < 1:
            return "stack is empty"
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
        if not self.stack or len(self.stack) < 1:
            return "stack is empty"
        return self.stack[0]
    
    def printStack(self):
        print(self.stack)


st = Stack()

for x in range(1,11):
    st.append(x)

st.printStack()

print(st.pop())
print(st.pop())

st.printStack()

print(st.isEmpty())

print(st.top())