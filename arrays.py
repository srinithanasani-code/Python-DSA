arr = [10, 20, 30, 40, 50]
n = len(arr)


# 1. ACCESSING
def access(arr, index):
    return arr[index]


# 2. TRAVERSAL
def traverse(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# 3. INSERTION
def insert(arr, n, index, value):
    for i in range(n, index, -1):
        arr[i] = arr[i - 1]

    arr[index] = value
    return n + 1


# 4. DELETION
def delete(arr, n, index):
    for i in range(index, n - 1):
        arr[i] = arr[i + 1]

    return n - 1


# 5. LINEAR SEARCH
def search(arr, n, target):
    for i in range(n):
        if arr[i] == target:
            return i

    return -1


# 6. UPDATE
def update(arr, index, value):
    arr[index] = value


# 7. FIND LARGEST
def largest(arr, n):
    large = arr[0]

    for i in range(1, n):
        if arr[i] > large:
            large = arr[i]

    return large


# 8. FIND SMALLEST
def smallest(arr, n):
    small = arr[0]

    for i in range(1, n):
        if arr[i] < small:
            small = arr[i]

    return small


# 9. REVERSE
def reverse(arr, n):
    left = 0
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


# 10. COUNT ELEMENT
def count_element(arr, n, target):
    count = 0

    for i in range(n):
        if arr[i] == target:
            count += 1

    return count


# -------------------------
# FUNCTION CALLS
# -------------------------

print("Access:", access(arr, 2))

print("Traversal:")
traverse(arr, n)

n = insert(arr, n, 2, 25)
print("After insertion:")
traverse(arr, n)

n = delete(arr, n, 2)
print("After deletion:")
traverse(arr, n)

print("Search:", search(arr, n, 40))

update(arr, 0, 100)
print("After update:")
traverse(arr, n)

print("Largest:", largest(arr, n))
print("Smallest:", smallest(arr, n))

reverse(arr, n)
print("After reverse:")
traverse(arr, n)

print("Count of 30:", count_element(arr, n, 30))