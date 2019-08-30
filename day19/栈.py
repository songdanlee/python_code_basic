
class Stack:

    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise ValueError("栈为空")
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():
            raise ValueError("栈为空")
        return self.stack[-1]


s = Stack()
for i in range(5):
    s.push(i)
print(s.isEmpty())

while not s.isEmpty():
    print(s.pop())