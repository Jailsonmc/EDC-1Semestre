"""1ªPergunta"""
"""Declara os métodos"""
def negar(s):
    return not s
def naoAOuB(a,b):
    return not a or b
def espaco(e):
    return (8 - len(str(e))) * ' ' + "|"
def aImplicaB(a,b):
    if a == b:
        return True
    elif a != b:
        if a == True:
            return False
        else:
            return True

"""Definir os valores de p, q e uma lista de textos"""
p = [ True, True, False, False]
q = [ True, False, True, False]
textos = ['p','q','~p','p -> q','~pvq']

"""Define os espaços  e escreve a expressão inicial (linha 0)"""
for i in range(len(textos)):
    if i == len(textos) - 1:
        print(textos[i],espaco(textos[i]))
    else:
        print(textos[i],espaco(textos[i]),end="")


"""Define os espaços  e escreve os restantes resultados (linhas de 1 à 4)"""
for i in range(len(p)):
    print(str(p[i]),espaco(str(p[i])), end='')
    print(str(q[i]), espaco(str(q[i])) , end='')
    print(str(negar(p[i])), espaco(str(negar(p[i]))) , end ='' )
    print(str(aImplicaB(p[i],q[i])), espaco(str(aImplicaB(p[i],q[i]))), end='')
    print(str(naoAOuB(p[i],q[i])), espaco(str(naoAOuB(p[i],q[i]))))
