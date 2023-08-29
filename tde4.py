#1.Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.
'''
def pos_ou_neg(n):
    if n < 0:
        print(f'{n} é um número negativo.')
    else:
           print(f'{n} é um número positivo.')   
              
              
n = float(input('Digite um número: '))
pos_ou_neg(n)
'''

#2. Escreva uma função para imprimir o valor absoluto de um número.
'''
def valor_absoluto(numero):
    return abs(numero)

numero = float(input("Digite um número: "))
valor = valor_absoluto(numero)
print(f'O valor absoluto do numero {numero} é {valor}.')
'''