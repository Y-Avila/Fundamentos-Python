text = "Esta es una practica para strings"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[1:len(text)])

print(text[len(text)-1])
print(text[-1])

print(text[-1])


print(text.find("para"))


print(text[text.find("para"):len(text)-1])
print(text[text.find("para"):])

print(text[::2])