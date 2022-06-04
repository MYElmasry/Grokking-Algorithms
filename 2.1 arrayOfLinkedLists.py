class linkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def appendNode(data, head):
    newNode = linkedList(data)
    if head == None:
        head = newNode
    else:
        p = head
        while p.next != None:
            p = p.next
        p.next = newNode
    return head

def printList(head):
    p = head
    while(p != None):
        print(p.data)
        p = p.next
    print("==========================")
    
def enterData(arr):
    name = input("Enter Your Name:").title()
    i = ord(name[0])-65
    arr[i] = appendNode(name, arr[i])  
    
arr = []
for i in range(26):
    arr.append(None)
enterData(arr)
enterData(arr)
enterData(arr)
