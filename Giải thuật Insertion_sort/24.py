a = [5, 2, 4, 6, 1, 3]

n = len(a)

bubble = a.copy()

bubble_compare = 0
bubble_swap = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        bubble_compare += 1
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
            bubble_swap += 1

selection = a.copy()

selection_compare = 0
selection_swap = 0

for i in range(n - 1):

    min = i

    for j in range(i + 1, n):
        selection_compare += 1
        if selection[j] < selection[min]:
            min = j

    if min != i:
        selection[i], selection[min] = selection[min], selection[i]
        selection_swap += 1

insertion = a.copy()

insertion_compare = 0
insertion_shift = 0

for i in range(1, n):

    key = insertion[i]
    j = i - 1

    while j >= 0:

        insertion_compare += 1

        if insertion[j] > key:
            insertion[j + 1] = insertion[j]
            insertion_shift += 1
            j -= 1
        else:
            break

    insertion[j + 1] = key

print("Bubble Sort")
print("Mang:", bubble)
print("So sanh:", bubble_compare)
print("Swap:", bubble_swap)

print()

print("Selection Sort")
print("Mang:", selection)
print("So sanh:", selection_compare)
print("Swap:", selection_swap)

print()

print("Insertion Sort")
print("Mang:", insertion)
print("So sanh:", insertion_compare)
print("Shift:", insertion_shift)