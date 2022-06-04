class stack:
    def __init__(self):
        self.s = []
        
    def push(self, value):
        self.s.append(value)
        
    def pop(self):
        if self.isEmpty():
            print("Error")
        else:
            self.s.pop()
    
    def isEmpty(self):
        return len(self.s) == 0
    
    def top(self):
        if self.isEmpty():
            print("Error")
        else:
            return self.s[-1]