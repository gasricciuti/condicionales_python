# Condicionales [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"
#  --> En caso negativo (numero_1 no es mayor a 5)
#      verifique si el numero_2 es mayor a 5
#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

if numero_1 >= 5:
    if numero_2 > 0:
        print('{} es mayor a 5 y {} es un numero positivo'.format(numero_1, numero_2))
    else:
        print('{} es un numero negativo'.format(numero_2))
else:
    print('{} es menor a 5'.format(numero_1))



# Verifique la calificación de un estudiante según su
# puntaje en un examen
puntaje = 0

# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados

if puntaje >= 90:
    print('la calificacion del alumno es 90 o mayor')
elif puntaje >= 80:
    print('la calificacion del alumno es 80 0 mayor')
elif puntaje >= 70:
    print('la calificacion del alumno es 70 o mayor')
elif puntaje >= 60:
    print('la calificacion del alumno es 60 o mayor')
elif puntaje < 60 and puntaje > 0:
    print('la calificacion del alumno es menor a 60')
else:
    print('el alumno no tiene calificacion')