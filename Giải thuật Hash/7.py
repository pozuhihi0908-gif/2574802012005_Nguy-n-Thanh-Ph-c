size = 4

table = [None] * size

dem = 0

def put(key):

    global size
    global table
    global dem

    if dem / size > 0.75:

        size = size * 2

        bang_moi = [None] * size

        for i in range(len(table)):
            if table[i] != None:
                index = table[i] % size
                bang_moi[index] = table[i]

        table = bang_moi

    index = key % size

    while table[index] != None:
        index = (index + 1) % size

    table[index] = key

    dem = dem + 1

put(10)
put(20)
put(30)
put(40)
put(50)

print(table)