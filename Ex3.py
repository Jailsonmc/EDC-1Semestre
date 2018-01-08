def eNumeroPrimo(n):
    ePrimo = True

    for i in range(2, n):
        if n % i == 0:
            ePrimo = False
            break

    if n == 1 or n == 0:
        return False
    elif ePrimo or n == 2:
        return True
    else:
        return False

print("Introduza um número para verificação na conjetura de Goldbach:")
p = int(input())

if p%2==0 and p > 2:
    for q in range(2, int(p/2 + 1)):
         if eNumeroPrimo(q) == True:
             for r in range(p, 2, -1):
                 if eNumeroPrimo(r) == True:
                     if p == q + r:
                         print(p, "=", q, "+", r)
else:
    print("NÚMERO INVÁLIDO")