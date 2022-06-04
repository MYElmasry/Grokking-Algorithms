class queue:
    def __init__(self):
        self.q = []
        
    def enqueue(self, x):
        self.q.append(x)
        
    def dequeue(self):
        self.q.pop(0)
    
    def printQ(self):
        print(self.q)
        
q = queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.dequeue()
q.printQ()