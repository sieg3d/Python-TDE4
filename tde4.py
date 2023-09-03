# 1.Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.
'''
def pos_ou_neg(n):
    if n < 0:
        print(f'{n} é um número negativo.')
    else:
           print(f'{n} é um número positivo.')   
              
              
n = float(input('Digite um número: '))
pos_ou_neg(n)
'''

# 2. Escreva uma função para imprimir o valor absoluto de um número.
'''
def valor_absoluto(numero):
    return abs(numero)

numero = float(input("Digite um número: "))
valor = valor_absoluto(numero)
print(f'O valor absoluto do numero {numero} é {valor}.')
'''

# 3. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
'''
def limitador(a, b, limite):
    return a + b > limite
        
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
limite = float(input('Digite o limite: '))

print(limitador(a, b, limite))
'''

# 4. Escreva uma função que recebe dois números (a e b) como parâmetro e retorna a quantidade (0, 1 ou 2) deles que é maior que um terceiro parâmetro, chamado limite.
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

# 5. Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

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

# 6. Escreva uma função que recebe como entrada uma lista ordenada de números e retorna o índice do primeiro elemento maior que um elemento limite.
# Se nenhum elemento da lista for maior que o limite desejado, retorne o valor -1.
'''
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
'''

# 7.Escreva uma função que recebe como entrada um número inteiro positivo n e retorne a soma de todos os inteiros positivos menores ou iguais a n.
'''
def super_soma(n):
    soma = n
    for valor in range(n):
        soma += valor
    
    return soma

n = int(input('Digite um numero: '))

resultado = super_soma(n)
print(f'O resultado da soma do numero digitado e numeros menores que ele é {resultado}.')
'''

#8. Escreva uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. Caso contrário, retorne False.
'''
def check_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input("Insira o ano: "))
bissexto = check_bissexto(ano)
print(f'O ano {ano} é bissexto: {bissexto}')
'''

#9. Escreva uma função que recebe como entrada um número n e imprime todas as potências de 2 menores ou iguais a n.
'''
def potencia(n):
    for valor in range(n+1):
        print(f'{valor}² = {valor**2}')
    
n = int(input('Digite um numero: '))

potencia(n)
'''

#10. Escreva uma função que recebe como entrada um número inteiro positivo n e imprime a representação binária desse número.
'''
def converte_binario(n):
  print(f'O numero {n} convertido em binário é:', bin(n)[2:])

n = int(input('Digite um numero: '))
converte_binario(n)
'''

#11. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.
'''
time = {}

time['nome'] = input('Nome do Time: ')
time['titulo_libertadores'] = int(input('Quantos titulos da libertadores: '))
time['torcida'] = int(input('Quantidade de torcedores: '))

print(time)
'''

#12.Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. 
# Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

'''
frase = input("Insira uma frase:")
texto = {}

for letra in frase:
    if letra.isalpha():
        if letra in texto:
            texto[letra] +=1
        else:
            texto[letra] = 1

print(texto)
'''

#13. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

'''
lista_mercado = {}

for i in range(3):
    produto = input(f'Produto {i+1}: ')
    valor = float(input(f'Valor: '))
    lista_mercado[produto] = valor
    

for produto, valor in lista_mercado.items():
    print(f'{produto}: R${valor:.2f}')
'''

#14. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

notas = {}

for i in range(4):
    nota = float(input(f'Digite a nota {i+1}'))
    notas[f'Nota{i+1}'] = nota

soma = sum(notas.values())
media = soma / 4
print(notas)
print(soma)
print(media)
    
