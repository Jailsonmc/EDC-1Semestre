def ePrimo(a):
    for i in range(2, a):
        if a % i == 0:
            print(a, "não é número primo")
            break
    return 0

def invAmoduloB(a, b):
    for k in range(b):
        if (a*k-1)%b == 0:
            return k
            break
    else:
        print(str(a) + " não tem inverso em Z" + str(b))
        quit()

a = int(input("a = "))
n = int(input("n = "))

ePrimo(a)
ePrimo(n)

print("\n")

print(str(a) + "x ≡" + str(n) + " 1")

print("\n")

res = invAmoduloB(a, n)

print("O inverso da congruência é", res)