class Stack:
    def __init__(self, values) :
        self.values = values

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if len(self.values) == 0:
            return None
        else: 
            self.values.pop(len(self.values) - 1)
            return self.values   

    def peek(self):
        if len(self.values) == 0:
            return None
        else: return self.values[len(self.values) - 1]

    def __str__(self):
        return f"{self.values}"
    
q1 = Stack([1,2,3])
print(q1)
print(q1.pop())
q1.push(4)
print(q1)
print(q1.peek())


