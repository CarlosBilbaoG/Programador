"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

#Operadores

'''Operadores Aritmeticos'''

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Division Entera: 10 // 3 = {10 // 3}") # Divide y redondea el resultado hacia abajo al entero mas cercano
print(f"Modulo: 10 % 3 = {10 % 3}") # Devuelve el resto de la división
print(f"Exponente: 10 ** 3 = {10 ** 3}") # Eleva el primer valor a la potencia del segundo

'''Operadores De Asignacion'''

a = 10 # Asignación
a += 3 # Suma y Asignación

print(f"Asignacion y Suma: a += 3 -> a = {a}")
a -= 3
print(f"Asignacion y Resta: a -= 3 -> a = {a}")
a *= 3
print(f"Asignacion y Multiplicacion: a *= 3 -> a = {a}")
a /= 3
print(f"Asignacion y Division: a /= 3 -> a = {a}")
a //= 3
print(f"Asignacion y Division Entera: a //= 3 -> a = {a}")
a %= 3
print(f"Asignacion y Modulo: a %= 3 -> a = {a}")
a **= 3
print(f"Asignacion y Exponente: a **= 3 -> a = {a}")

'''Operadores De Comparacion'''

print(f"Igual a: 10 == 3 -> {10 == 3}")
print(f"Distinto de: 10 != 3 -> {10 != 3}")
print(f"Mayor que: 10 > 3 -> {10 > 3}")
print(f"Menor que: 10 < 3 -> {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 -> {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 -> {10 <= 3}")

'''Operadores Logicos'''

print(f"AND &&: (10 > 3) and (10 < 20) -> {(10 > 3) and (10 < 20)}") # Devuelve TRUE si ambas condiciones son verdaderas, de lo contrario seria FALSE
print(f"OR ||: (10 > 3) or (10 > 20) -> {(10 > 3) or (10 > 20)}") # Devuelve TRUE si al menos una de las condiciones es verdadera, si ambas son falsas el resultado será FALSE
print(f"NOT !: not (10 > 3) -> {not (10 > 3)}") # Invierte el valor logico de una condición. Si la condición es TRUE, not la convierte en FALSE y viceversa

# Tabla de verdad Operadores Logicos

"""AND"""
'''A        B          A and B'''
#True      #True       #True
#True      #False      #False
#False     #True       #False
#False     #False      #False
"""OR"""
'''A        B          A or B'''
#True      #True       #True
#True      #False      #True
#False     #True       #True
#False     #False      #False
"""NOT"""
'''A        not A'''
#True      #False       
#False     #True      

'''Operadores De Identidad'''

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"Es: a is b -> {a is b}")  # Falso, ya que aunque los valores sean iguales, no son la misma instancia
print(f"Es: a is c -> {a is c}")  # Verdadero, ya que c es la misma instancia que a
print(f"No es: a is not b -> {a is not b}")  # Verdadero

'''Operadores De pertenencia'''

print(f"En: 1 in [1, 2, 3] -> {1 in [1, 2, 3]}") # Comprueba que 1 este dentro de [1, 2, 3]
print(f"No en: 4 not in [1, 2, 3] -> {4 not in [1, 2, 3]}")


'''Operadores De Bit'''

a = 10 # 1010
b = 3  # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: -10 = {-10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

''' Estructuras de Control'''

#Condicionales: Sirven para que nosotros le indiquemos a nuestro codigo como tomar diferentes caminos IF ELIF ELSE

my_string = "BilbaoDev"

if my_string == "BilbaoDev":
    print ("my_string es 'BilbaoDev' ")

elif my_string == "Carlos":
    print ("my_string es 'Carlos' ")

else:
    print("my_string no es 'BilbaoDev' ni 'Carlos' ")

#Iterativas: Para crear bucles 
    #FOR: Sirve para recorrer estructuras que tienen mas de un elemento o para ejecutar una acción varias veces
    #WHILE: Sirve para aplicar una condicion siempre y cuando esta sea verdadera

for i in range(11):
    print(i)

i = 0 

while i <= 10:
    print(i)
    i += 1


#Manejo de Excepciones

try:
    print(10 / 0)
except: # En otros lenguajes se conoce como catch, intenta que el codigo no se rompa y devuelve un resultado ante un error
    print("Se ha producido un error")
finally: # Finally es una ultima instruccion que se ejecutara se produzca o no un error
    print("Ha finalizado el manejo de excepciones")


