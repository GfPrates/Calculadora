#Calculadora Python

#Perguntar para usuario qual o tipo de operação deseja fazer
#Perguntar o primeiro numero
#Perguntar o segundo numero
#Realizar o calculo
#Mostrar o resultado

print ( 'Seja bem vindo a minha primeira calculadora')

operacao = input ('Qual operação (+,-,*,/) voce deseja utilizar?')
n1 = int (input ('Digite o primeiro numero:'))
n2 = int (input ('Digite o segundo numero:'))

if operacao == '+':
    total = n1 + n2
    print (total)
elif operacao == '-':
    total = n1 - n2
    print (total)
elif operacao == '*':
    total = n1 * n2
    print (total)
elif operacao == '/':
    total = n1 / n2
    print (total)
else:
    print ('Dados invalidos')







