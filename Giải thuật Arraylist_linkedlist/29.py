class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(2)
a.next = Node(4)
a.next.next = Node(3)

b = Node(5)
b.next = Node(6)
b.next.next = Node(4)

nho = 0

while a != None or b != None or nho != 0:

    tong = nho

    if a != None:
        tong = tong + a.data
        a = a.next

    if b != None:
        tong = tong + b.data
        b = b.next

    print(tong % 10, end=" -> ")

    nho = tong // 10

print("None")