'''for char in 'wrghehtrhrtdhrjt':
    print(char, end='')
    char = 1
    print(char)'''
'''for i in range(10, 1, -3):
    print(i)
    '''

'''senha_cad = '1234'
for i in range(3):
    senha = input("Senha: ")
    if senha == senha_cad:
        print("ACESSO LIBERADO")
        break
    print(f"hacker?????????vc tem só mais {2-i} tentativas!")
if senha != senha_cad:
    print("saí")
'''
#ex1 some todos o num de 1 a 10 usando for
'''cont = 0
for i in range(101):
    cont += i
print(cont)
'''
#ex2 peça 10 num para o usario e conte qts pares e impares
'''par = 0

impar = 0
for i in range(10):
    num = input("Digite um número")
    while not num.isnumeric():
        print("errado")
        num = input("Digite um número")
    num = int(num)
    if num % 2 == 0:
        par +=1
    else:
        impar+=1
print(f'par = {par}')
print(f'ímpar = {impar}')'''

#ex3 peça 10 num para o usario e faça soma e media
'''soma = 0
media = 0

for i in range(10):
    num = input("Digite um número")
    while not num.isnumeric():
        print("errado")
        num = input("Digite um número")
    num = int(num)
    soma +=num
media = soma/10
print(soma)
print(media)'''
#ex4 tabuada de 1 a 10
'''valor = 5
for i in range(11):
    tabuada = valor*i
    print(f'{valor}X{i} = {tabuada}')
'''
#ex5 qtd de vogais numa string digitada
vogais = 0
palavra = input("digite algo: ")
for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vogais += 1
print(f'vogais {vogais}')
