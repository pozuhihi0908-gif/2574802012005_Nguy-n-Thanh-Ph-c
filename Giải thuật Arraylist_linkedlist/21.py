class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

truoc = None
hienTai = head

while hienTai != None:
    sau = hienTai.next
    hienTai.next = truoc
    truoc = hienTai
    hienTai = sau

head = truoc

tam = head

while tam != None:
    print(tam.data, end=" -> ")
    tam = tam.next

print("None")