q1 = []
q2 = []

q1.append(1)
q1.append(2)
q1.append(3)

while len(q1) > 1:

    q2.append(q1.pop(0))

print("Pop:", q1.pop(0))

q1, q2 = q2, q1

print(q1)