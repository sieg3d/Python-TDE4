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

#3. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
'''
def limitador(a, b, limite):
    return a + b > limite
        
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
limite = float(input('Digite o limite: '))

print(limitador(a, b, limite))
'''

#4. Escreva uma função que recebe dois números (a e b) como parâmetro e retorna a quantidade (0, 1 ou 2) deles que é maior que um terceiro parâmetro, chamado limite.
'''
def conta_se_maior(a, b, limite):
   quantidade = 0
   if a > limite:
      quantidade+=1
   
   if b > limite:
      quantidade+=1

   return quantidade

        
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
limite = float(input('Digite o limite: '))

print('Quantidade de números maiores que limite:', conta_se_maior(a, b, limite))
'''

#5. Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

'''
def conceito(nota):
    if nota >= 9:
        return 'A (Excelente!)'
    elif nota < 9 and nota >= 7:
        return 'B (Bom!)'
    elif nota < 7 and nota >= 5:
        return 'C (Regular.)'
    elif nota < 5 and nota >= 3:
        return 'D (Insatisfatório.)'
    elif nota < 3 and nota > 0:
        return 'E (Fraco.)'
    else:
        return 'F (Falha!)'
    

nota = float(input('Insira a nota do aluno: '))

print(f'A nota {nota} convertida em conceito é:', conceito(nota))
'''

#6. Escreva uma função que recebe como entrada uma lista ordenada de números e retorna o índice do primeiro elemento maior que um elemento limite.
#Se nenhum elemento da lista for maior que o limite desejado, retorne o valor -1.

def maior_elemento(lista, limite):
    posicao = None
    for valor in lista:
        if valor > limite:
            posicao = lista.index(valor)
            break
        else:
            posicao = -1

    return posicao


lista = [10,20,30,40,50,60,70,80,90]
limite = float(input('Digite o elemento limite: '))
maior_elemento(lista, limite)


print(maior_elemento(lista, limite))