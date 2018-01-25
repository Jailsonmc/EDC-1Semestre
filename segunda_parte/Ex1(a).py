def funcaoEncriptacao(frase):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    fe = []
    for i in range(len(frase)):
        for j in range(len(alfabeto)):
            if frase[i] == alfabeto[j]:
                fe.append(alfabeto[(19 * j - 7) % 27])
                break
            else:
                continue
    fraseEncriptada = ''.join(fe)
    return fraseEncriptada
frase = "tempestade no mar"
print(frase)

print(funcaoEncriptacao(frase))