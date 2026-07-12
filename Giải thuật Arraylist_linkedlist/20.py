class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)

x = 2

if head.data == x:
    head = head.next
else:
    tam = head

    while tam.next != None:
        if tam.next.data == x:
            tam.next = tam.next.next
            break
        tam = tam.next

tam = head

while tam != None:
    print(tam.data, end=" -> ")
    tam = tam.next

print("None")