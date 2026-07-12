class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

x = 2

tam = head
vitri = 0
tim = False

while tam != None:
    if tam.data == x:
        print(vitri)
        tim = True
        break

    tam = tam.next
    vitri = vitri + 1

if tim == False:
    print(-1)