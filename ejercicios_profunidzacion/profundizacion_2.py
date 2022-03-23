# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input('Ingrese el primer numero entero:\n'))

numero_2 = int(input('Ingrese el segundo numero entero:\n'))

numero_3 = int(input('Ingrese el tercer numero entero:\n'))

if numero_1 >=0:
    resultado = numero_1 % 2
    if resultado == 0:
        print('Numero uno es par')
    else:
        print('Numero uno es impar')
else:
    print('Numero uno no es entero')

if numero_2 >=0:
    resultado = numero_2 % 2
    if resultado == 0:
        print('Numero dos es par')
    else:
        print('Numero dos es impar')
else:
    print('Numero dos no es entero')

if numero_3 >=0:
    resultado = numero_3 % 2
    if resultado == 0:
        print('Numero tres es par')
    else:
        print('Numero tres es impar')
else:
    print('Numero tres no es entero')

    
