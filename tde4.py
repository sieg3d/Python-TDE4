#1.Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.

def pos_ou_neg(n):
    if n < 0:
        print(f'{n} é um número negativo.')
    else:
           print(f'{n} é um número positivo.')   
              
              
n = float(input('Digite um número: '))
pos_ou_neg(n)

