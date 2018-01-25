from random import randint

def insertionSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    return array

a1 = [3, 2, 5, 17, 1]

print(insertionSort(a1))

a2 = []
a2.append(randint(0, 3000))

i = 1
conf = True
while i < 300:
    n = randint(0, 3000)
    for a in range(len(a2)):
        if n < a2[a-1] or n > a2[a-1]:
            conf = True
        else:
            conf = False
            break
    if conf == True:
        a2.append(n)
        i += 1
    else:
        i -= 1

print("\n")
print(insertionSort(a2))