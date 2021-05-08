class Stack():
    def __init__(self,data):
        self.data = data

    next = None

    def peek(self):
        chk = self
        print(chk.data)
        while chk.next:
            chk = chk.next
            print(chk.data)
    def push(self,val):
        new_ent = Stack(val)
        new_ent.next = self
        self = new_ent
        return self
    def pop(self):
        popped = self.data
        print("Popped: ",popped)
        self = self.next
        return self

stk = Stack(10)
stk = stk.push(2)
stk = stk.push(8)
stk.peek()
stk = stk.pop()
stk.peek()
