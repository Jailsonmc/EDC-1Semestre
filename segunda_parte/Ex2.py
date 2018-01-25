def funcaoEuler(n):
    mdc = n
    cont = 0
    for i in range(1, n):
        while n % mdc != 0 or i % mdc != 0:
            mdc = mdc - 1
        if mdc == 1:
            cont += 1
    return cont

print("Φ(4) = " + str(funcaoEuler(4)))
print("Φ(5) = " + str(funcaoEuler(5)))
print("Φ(116) = " + str(funcaoEuler(116)))
print("Φ(117) = " + str(funcaoEuler(117)))
print("Φ(2018) = " + str(funcaoEuler(2018)))