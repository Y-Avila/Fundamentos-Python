#String
string = "texto"
string2='Texto'
print(type(string))
#Integer
int = 22
print(type(int))

#float
int = 22.5
print(type(int))

#Boolean Categoria inicia con mayuscula

Boolean = True
Boolean = False

#ingreso de informacion con input lo toma como STR

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Accessing elements in the list
print(numbers[0])  # Output: 1

# Modifying elements in the list
numbers[2] = 10
print(numbers)

# Adding elements to the list
numbers.append(6)
print(numbers)

# Removing elements from the list
"""
Remueve el valor asignado en el parametro de la funcion
mas no elimina por posicion del vector a diferencia de utilizar []
"""
numbers.remove(1)
print(numbers)

# Iterating over the list
for number in numbers:
    print(number)
    if number == 4:
      print("condicional")



