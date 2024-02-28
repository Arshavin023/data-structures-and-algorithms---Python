from collections import deque 

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, value):
        reversed = value[::-1]
        self.push(reversed)
    
    


stack = Stack()
stack.push('https://www.cnn.com/')
stack.push('https://www.cnn.com/world')
stack.push('https://www.cnn.com/india')
stack.push('https://www.cnn.com/china')
stack.push('https://www.cnn.com/korea')
stack.reverse_string('https://www.cnn.com/korea')
print(stack.peek())
# print(stack.pop())
# print(stack.pop())
print(stack.is_empty())
# print(stack.peek())
print(stack.size())

