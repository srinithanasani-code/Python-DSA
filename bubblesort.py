a = [8, 3, 5, 1, 7, 2, 6, 4]

for i in range(7):
    for j in range(7 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)