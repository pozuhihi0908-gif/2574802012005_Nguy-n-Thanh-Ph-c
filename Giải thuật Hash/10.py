arr = "leetcode"

dem = {}

for i in arr:

    if i in dem:
        dem[i] = dem[i] + 1
    else:
        dem[i] = 1

for i in arr:

    if dem[i] == 1:
        print(i)
        break