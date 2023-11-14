a = 2
b = 10

def compare_numbers(a, b):
    if a == b:
        return "Equal"
    elif a > b:
        return "Greater than"
    else:
        return "Less than"

print(compare_numbers(a, b))

"""
>=
<=
==
!=
<
>


"""

print(a!=b)

print("a"=="A")



#Floats Comparation

x = 3.6
y = 2.4 + 1.2

print(x)
print(y)

#z = format(y,'.0f')
z = round(y,0)
print(z)
print(type(z))

print(x==y)
print(z==4)

tolerance = 0.1
print(abs(x-y)<tolerance)
