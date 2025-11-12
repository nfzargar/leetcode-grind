class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatstart(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertatstart(5)
    ll.insertatstart(6)
    ll.print()