# -*- coding: utf-8 -*-
"""Atividade de LPC

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17NPAaUXQ5Bh82b3RuKCMJLN6tMMmPzxF
"""

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Questão 10

nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo : ')
if sexo == 'm':
    print(f'{nome} é do sexo Masculino')
elif sexo == 'f':
    print(f'{nome} é do sexo Feminino')
else:
    print('Sexo Inválido.')

# Questão 11
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
if letra in 'aeiou':
    print(f'{letra} é uma vogal.')
else:
    print(f'{letra} é uma consoante.')

#Questão 5
#Faça um Programa que converta metros para centímetros.

metro = float(input('Digite uma medida em metros: '))
cent = metro * 100
print(f'{metro} metros convertido para centímetros é igual a {cent} centímetros.')

#Questão 8
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_recebido_por_hora = float(input('Digite o quanto você recebe por hora: '))
horas_trabalhadas = int(input('Quantas horas você trabalha diariamente? '))
salario = (valor_recebido_por_hora * horas_trabalhadas) * 23
print(f'O seu salário é igual a R${salario}')

#Questão 1
#Faça um Programa que mostre a mensagem "Olá mundo" na tela.

print ("Olá Mundo!")

#Questão 2
#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].


número = input('Digite um número: ')
print(f'O número informado foi {número}')

#Questão 3
#Faça um Programa que peça dois números e imprima a soma.

#Função que soma os dois números digitados
def sum(num1, num2):
    return num1 + num2
    
#Atribui valores nas variáveis
print("\tSoma de dois números\n")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

#Imprime resultado na tela
print ("")
print ("O resultado da soma é %d" %sum(num1, num2))

#Questão 4
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
 
n1 = float(input('primeira nota do aluno'))
n2 = float(input('segunda nota do aluno'))
n3 = float(input('terceira nota do aluno'))
n4 = float(input('quarta nota do aluno'))
média = (n1+n2+n3+n4) / 4
print('a média entre {:.1f}, {:.1f}, {:.1f} e {:.1f} é igual a {:.1f}'. format(n1, n2, n3, n4, média))



# Questão 6
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math #importar a matemática para o pi.
raio_circulo = input('Qual o raio do cículo (em metros) ? ')
calculo_area = math.pi*float(raio_circulo)*float(raio_circulo)
print('A área do círculo é: ', round(calculo_area,2), 'm')

# Questão 9
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um valor: \n'))

if valor >= 0:
    print('Este valor é positivo.')
else:
    print('Este valor é negativo.')

#Questão 7
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = input('Qual o tamanho do lado do quadrado (em metros) ? ')

area_quadrado = float(lado)*float(lado)
dobro_area = float(area_quadrado)*2

print('A área do quadrado é: ', round(area_quadrado,2), 'm\nO dobro da sua área é: ', round(dobro_area,2), 'm')

