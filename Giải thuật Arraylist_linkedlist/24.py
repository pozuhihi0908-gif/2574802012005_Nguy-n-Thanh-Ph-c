class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)

head = None
tail = None

while a != None and b != None:

    if a.data < b.data:
        node = a
        a = a.next
    else:
        node = b
        b = b.next

    if head == None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

while a != None:
    tail.next = a
    break

while b != None:
    tail.next = b
    break

tam = head

while tam != None:
    print(tam.data,end=" -> ")
    tam = tam.next

print("None")