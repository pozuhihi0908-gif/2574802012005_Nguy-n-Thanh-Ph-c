arr = ["apple","ant","banana","ball","cat","car"]

nhom = {}

for i in arr:

    key = i[0]

    if key not in nhom:
        nhom[key] = []

    nhom[key].append(i)

for i in nhom:
    print(i,"=",nhom[i])