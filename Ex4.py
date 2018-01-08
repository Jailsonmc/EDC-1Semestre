from random import randint

def insertionSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    return array

a1 = [3, 2, 5, 17, 1]

print(insertionSort(a1))

a2 = [randint(0, 3000)]

i = 1
while i < 300:
    n = randint(0, 3000)
    for j in range(0, len(a2) - 1):
        if a2[j - 1] == n:
            i = i - 1
            break
    a2.append(n)
    i += 1

print("\n")
print(insertionSort(a2))