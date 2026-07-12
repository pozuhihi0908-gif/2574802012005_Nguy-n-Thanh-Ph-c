text = "zabcd"
pattern = "abc"

m = len(pattern)

for i in range(len(text) - m + 1):

    if text[i:i+m] == pattern:
        print("Vị trí:", i)
        break