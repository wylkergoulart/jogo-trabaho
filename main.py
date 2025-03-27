#x = int(input('Digite um valor inteiro:'))
#y = int(input('Digite outro valor inteiro:'))

#if (x > y):
 #   print('O primeiro valor é maior que o segundo: {}'.format(x))

#else:
#   print('O segundo valor é maior: {}'.format(y))

# par ou impar

#x = int(input('Digite um valor inteiro:'))

#if (x % 2 == 0 ):
#    print('O número é par!')

#else:
#    print('O número é ímpar:')


# aluno exercicio

#m1 = float(input('digite a nota da 1ª matéria:'))
#m2 = float(input('digite a nota da 2ª matéria:'))
#m3 = float(input('digite a nota da 3ª matéria:'))

#if m1 >= 7 and m2 >= 7 and m3 >= 7:
#    print("Situação:Aprovado!")
#else:
#    print('Situação:Reprovado!')


# loja com menu
                    #MENU
#print('Escolha qual produto deseja comprar:')
#print('1 - Maça')
#print('2 - Laranja')
#print('3 - Banana')
#produto = int(input("Qual produto deseja comprar?"))
#qtd = int(input('Quantas unidades deseja?'))
#if produto == 1:
#    pagar = qtd *  2.3
 #   print('Você comprou {} maças. Total a pagar R${}'.format(qtd,pagar))
#elif produto == 2:
#    pagar = qtd * 3.6
#     print('Você comprou {} laranjas. Total a pagar R${}'.format(qtd,pagar))
#elif produto == 3:
#      pagar = qtd * 1.85
#      print('Você comprou {} bananas. Total a pagar R${}'.format(qtd,pagar))
#else:
      #print('Produto inexistente')


#nome = input('Digite seu nome:')
#idade = int(input('Digite sua idade:'))

#if nome == 'wylker':
#    print('ola, {}'.format(nome))
#elif idade < 18:
#    print('Você não é o Wylker! e é menor de idade')
#elif idade >= 100:
#    print('Diferente de voçê o Wylker não é imortal.')

#print( 2 + 2 <4)
#print( 7 // 3 == 1 + 1)
#print( 3 **2 + 4 **2 == 25)
#print(2 + 4 + 4 > 12)
#print(1387 // 7)
#print(31 % 2 == 0 )

    #exercicio 1.0

#idade = int(input('Digite uma idade:'))
#if (idade > 60):
#    print('Você tem direito aos benefíocios!')
#else:
#    print('Você não tem direiro aos beneficios.')

    #exercicio 1.1

#kwh = float(input('Qual a quantidade de kWh?'))
#tipo = input('Qual o tipo de instalção (R, I OU C)')

#if (tipo == 'R'):
#    if kwh <= 500:
#        preco = 0.4
#    else:
 #       preco = 0.65

#elif (tipo == 'I'):
#    if kwh <= 5000:
#        preco = 0.55
#    else:
 #       preco = 0.6
#
#elif (tipo == 'c'):
 #   if kwh <= 1000:
  #      preco = 0.55
   # else:
    #    preco = 0.6
#else:
 #   print('Instalação invalida!')

#print('Quantidade de kWh consumida {}. Valor a pagar R${}'.format(kwh, kwh * preco))

#LAÇO DE REPETIÇÃO

#for i in range (3,13,1):
#    print(i)

#i = 1
#while (i < 13):
#    print(i)
#    i += 1


#CALCULADORA COM LAÇO DE REPETIÇÃO

#print('CALCULADORA')
#print('Adição +')
#print('Subtração -')
#print('Multiplicação *')
#print('divisão / ')
#print('sair s')


#op = input('Digite a operação desejada:')
#if op == '+' or op == '-' or op == '*' or op == '/':
#    x = int(input('Digite o primeiro valor:'))
#    y = int(input('Digite o segundo valor:'))

#while (op != 's'):
#    if (op == '+'):
#        res = x + y
#        print('Resultado: {} + {} = {}'.format(x,y,res))
#    elif (op == '-'):
#        res = x - y
#        print('Resultado: {} - {} = {}'.format(x,y,res))
#    elif (op == '*'):
#        res = x * y
#        print('Resultado: {} * {} = {}'.format(x,y,res))
#    elif (op == '/'):
#        res = x / y
#        print('Resultado: {} / {} = {}'.format(x,y,res))
#    else:
#        print('Operação ínvalida.')

#   op = input('Digite a operação desejada:')
#    if op == '+' or op == '-' or op == '*' or op == '/':
#        x = int(input('Digite o primeiro valor:'))
#        y = int(input('Digite o segundo valor:'))

#print('Encerrando progarama....')

#CINEMA

#dinheiro = 0
#total = 0

#while True:

#    idade = input('Qual sua idade?')
#    if idade == 'sair':
#        break
#    idade = int(idade)
#    total += 1

#    if (idade < 3):
#        ingresso = 0
#    else:
 #       if (idade > 12):
 #           ingresso = 30
 #       else:
 #           ingresso = 15
#    dinheiro += ingresso

#media = dinheiro / total

#print('Total de pessoas {}'.format(total))
#print('Dinheiro arrecadado {}'.format(dinheiro))
#print('media de dinheiro arrecadado {}'.format(media))


#Mensagem de boas vindas da loja

#print('Sejam bem-vindos a loja do Wylker Aparecido Peres Goulart')

#Entreda de valor e quantidade do produto

#valor_unitario = 0
#quantidade = 0
#valor_unitario = float(input('Digite o valor unitario do produto:'))
#quantidade = int(input('Digite a quantidade:'))

#valor total sem desconto

#valor_total_sem_desconto = valor_unitario * quantidade

#desconto_percentual = 0

# Aplicação dos descontos com base nas quantidades

#if (quantidade < 200):
#    desconto_percentual = 0
#elif ( (quantidade >= 200) and (quantidade < 1000 ) ):
#    desconto_percentual = 0.05
#elif  (quantidade < 2000) :
#    desconto_percentual = 0.10
#else:
#    desconto_percentual = 0.15

#Calculo do valor com desconto
#valor_com_desconto = valor_total_sem_desconto - valor_total_sem_desconto * desconto_percentual

#Saida do console

#print('Valor total dos produtos sem desconto foram de R${}'.format(valor_total_sem_desconto))
#print('Foi Gerado um desconto de {}%'.format(desconto_percentual * 100))
#print('Valor total dos produtos com desconto R${}'.format(valor_com_desconto))

