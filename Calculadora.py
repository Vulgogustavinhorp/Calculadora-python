"""Calculadora"""
while True:
    numero_1= input('Digite um número: ')
    numero_2= input('Digte outro Número: ')
    operador = input('Digite o operador (+-/*)')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

     ###
    print('Realizando sua conta confira o Resultado abaixo')
    
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
         print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
         print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
         print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)

        
       


    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
      break
    """Calculadora"""

    