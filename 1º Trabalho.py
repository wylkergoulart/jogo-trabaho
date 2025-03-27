#Exercicio 2/4

#Mensagem de boas vindas

print('Sejam bem-vindos a sorveteria do Wylker Aparecido Peres Goulart')

#Menu da Sorveteria

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- CARDAPIO -_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-')
print('-_-  Nº de Bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)-_-')
print('-_-       1      |          R$6,00        |        R$7,00     |          R$8,00     -_-')
print('-_-       2      |          R$11,00       |        R$13,00    |          R$15,00    -_-')
print('-_-       3      |          R$15,00       |        R$18,00    |          R$21,00    -_-')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-')

# Variáveis para guardar os valores
valor_pedido = 0
valor_total = 0

    #Laço de repetição

while True:

    #Entrada dos sabores e quantidade


    sabor = input('Entre com o sabor de sorvete desejado (tr/pr/es):')
    if (sabor != 'tr') and (sabor != 'pr') and (sabor != 'es'):
        print('Sabor Inválido, digite um sabor válido.')
        continue #Se o cliente errar volta para o começo do while

    if (quantidade != '1') and (quantidade != '2') and (quantidade != '3'):
        print('Quantidade Inválida, digite uma das opções acima.')
        continue #Se o cliente errar volta para o começo do while

    quantidade = int(quantidade)  # Convertendo para inteiro

    # Preço de acordo com o cardápio
    if sabor == 'tr':
        if quantidade == 1:
            valor_pedido = 6
        elif quantidade == 2:
            valor_pedido = 11
        else:
            valor_pedido = 15
    elif sabor == 'pr':
        if quantidade == 1:
            valor_pedido = 7
        elif quantidade == 2:
            valor_pedido = 13
        else:
            valor_pedido = 18
    elif sabor == 'es':
        if quantidade == 1:
            valor_pedido = 8
        elif quantidade == 2:
            valor_pedido = 15
        else:
            valor_pedido = 21

        # Atualização do valor total
    valor_total += valor_pedido

    outro_pedido = input('Deseja pedir algo mais? (s/n):')
    if outro_pedido == 'n':
        print('Valor total a ser pago R${:.2f}'.format(valor_total))
        break

print('Obrigado por escolher a sorveteria do Wylker Aparecido Peres Goulart!')