texto = "Mi edad es "
edad = 20

print(texto + str(edad))
print(f"{texto} {edad}")

edad = str(edad)
print(type(edad))

edad = int(edad)
print(type(edad))


name = 'Juana'
print(name)
age = '10'
print(age)


template = "Hola mi nombre es " + name + ", tengo "+str(age)+ "años y en 10 años tendré "+ str(int(age)+10)
print(template)
