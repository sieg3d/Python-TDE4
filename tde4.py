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