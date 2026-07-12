class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)

arr = []

tam = head

while tam != None:
    arr.append(tam.data)
    tam = tam.next

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            tam = arr[i]
            arr[i] = arr[j]
            arr[j] = tam

head = Node(arr[0])

tam = head

for i in range(1,len(arr)):
    tam.next = Node(arr[i])
    tam = tam.next

tam = head

while tam != None:
    print(tam.data,end=" -> ")
    tam = tam.next

print("None")