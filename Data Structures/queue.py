class Que:
    next = None
    def __init__(self, data):
        self.data = data



    def isEmpty(self):
        return None
    def peek(self):
        chk = self
        print(chk.data)
        while chk.next:
            chk = chk.next
            print(chk.data)

    def addo(self,val):
        node_new = Que(val)
        self.next = node_new
    def remove(self):
        print("removed: ",self.data)
        self = self.next
        return self


node = Que(10)
node.addo(6)
node.next.addo(7)
node.peek();
node = node.remove()
