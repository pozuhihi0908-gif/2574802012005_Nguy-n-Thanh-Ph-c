size = 10

key = [None] * size
value = [None] * size

def put(k, v):

    index = k % size

    while key[index] != None:
        if key[index] == k:
            value[index] = v
            return

        index = (index + 1) % size

    key[index] = k
    value[index] = v

def get(k):

    index = k % size

    while key[index] != None:

        if key[index] == k:
            return value[index]

        index = (index + 1) % size

    return -1

put(10,100)
put(20,200)
put(30,300)

print(get(20))
print(get(40))