number = [1,2,3,4,5,6,7,8,9,10]

print(number)
print(type(number))

# Lista com nomes
names = ['João', 'Maria', 'José', 'Pedro', 'Ana']  

print(names)
print(type(names))

lista_doble = [names, number]

print(lista_doble)
print(type(lista_doble))


print(lista_doble[0][1:2])



"""
Métodos de las listas++

    append(): Añade un ítem al final de la lista.
    clear(): Vacía todos los ítems de una lista.
    extend(): Une una lista a otra.
    count(): Cuenta el número de veces que aparece un ítem.
    index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
    insert(): Agrega un ítem a la lista en un índice específico.
    pop(): Extrae un ítem de la lista y lo borra.
    remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
    reverse(): Le da la vuelta a la lista actual.
    sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""