# Condicionales [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('{} es mayor alfabeticamente a {}'.format(texto_1, texto_2))
elif texto_1 == texto_2:
    print('Las palabras ingresadas son iguales')
else:
    print('{} es mayor alfabeticamente a {}'.format(texto_2, texto_1))


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print('la primera palabra tiene mas caracteres')
elif len(texto_1) == len(texto_2):
    print('las dos palabras tienen los mismos caracteres')
else:
    print('la segunda palabra tiene mas caracteres')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print('la primera letra de la primera palabra es mayor')
elif texto_1[0] == texto_2[0]:
    print('las dos palabras comienzan con la misma letra')
else:
    print('la primera letra de la segunda palabra es mayor')

    

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if texto_1 == copia_texto_1:
    print('las palabras ingresadas son iguales')
else:
    print('las palabras ingresadas son diferentes')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_2 != copia_texto_1:
    print('las palabras ingresadas son distintas')
else:
    print('las palabras ingresadas son iguales')

