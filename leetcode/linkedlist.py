class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,node):
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def print(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def detect(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=self.head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                print(slow.data)
                break
    def find(self, n):
        if n <= 0:
            return None
    
        slow = fast = self.head

    # Move the fast pointer n steps ahead
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next

    # Move both pointers until the fast pointer reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        return slow

        
li=linkedlist()
li.append(node(1))
li.append(node(2))
li.append(node(3))
li.append(node(4))
li.append(node(5))
li.append(node(6))

#li.detect()

print(li.find(2).data)

#li.print()
