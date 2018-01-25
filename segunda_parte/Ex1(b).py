def funcaoDesencriptacao(frase):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    fe = []
    for i in range(len(frase)):
        for j in range(len(alfabeto)):
            if frase[i] == alfabeto[j]:
                print("-----"+str(j))
                print((19 * j - 7))
                print((19 * j - 7) % 27)
                print("-----")
                fe.append(alfabeto[(19 * j - 7) % 27])
                break
            else:
                continue
    fraseDesencriptada = ''.join(fe)
    return fraseDesencriptada

#alfabeto2 = 'abcdefghijklmnopqrstuvwxyz'
#print(len(alfabeto2))

frase = "ypopbyublpttubxubpldtpnu"
print(frase)

print(funcaoDesencriptacao(frase))

