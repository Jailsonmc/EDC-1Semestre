"""2ªPergunta"""
"""Declara as funções"""
def negar(s):
    return not s
def aOuB(a,b):
    return a or b
def naoAOuB(a,b):
    return not a or b
def espaco(e):
    return (20 - len(str(e))) * ' '
def aImplicaB(a,b):
    if a == b:
        return True
    elif a != b:
        if a == True:
            return False
        else:
            return True

"""Definie os valores de p e q"""
p = [ True, True, True, True, False, False, False, False]
q = [ True, True, False, False, True, True, False, False]
r = [ True, False, True, False, True, False, True, False]
textos = ['p' ,'q' ,'r' ,'~p' , 'pvq', '~pvr', 'qvr', '(pvq)^(~p v r)-->(q v r)']

"""Defini os espaços  e escreve a expressão inicial(linha o)"""
for i in range(len(textos)):
    if i == len(textos) - 1:
        print(textos[i],espaco(textos[i]))
    else:
        print(textos[i],espaco(textos[i]),end="")

"""Defini os espaços  e escreve os restantes resultados (linhas de 1 à 4)"""
for i in range(len(p)):

    expressao = str(p[i])
    print(expressao, espaco(expressao), end = '')

    expressao = str(q[i])
    print(expressao, espaco(expressao), end = '')

    expressao = str(r[i])
    print(expressao, espaco(expressao), end = '')

    expressao = str(negar(p[i]))
    print(expressao, espaco(expressao), end = '')

    expressao =  str(aOuB(p[i],q[i]))
    print(expressao, espaco(expressao), end = '')

    expressao =  str((naoAOuB(p[i],r[i])))
    print(expressao, espaco(expressao), end = '')

    expressao =  str((aOuB(q[i], r[i])))
    print(expressao, espaco(expressao), end = '')

    expressao = str(   aImplicaB( ( aOuB(q[i], q[i]) and naoAOuB(p[i],r[i]) ) , aOuB(q[i],r[i]) ) )
    print( expressao , espaco( expressao ) )