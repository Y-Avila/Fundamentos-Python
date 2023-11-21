option_gamer = input('Ingrese opción de juego entre: piedra, papel o tijera: ')

option_CPU = 'tijera'


if option_gamer == 'piedra':
    print('Elegiste piedra')
elif option_gamer == 'papel':
    print('Elegiste papel')
elif option_gamer == 'tijera':
    print('Elegiste tijera')
else:
    print('Opción incorrecta')


if option_gamer == option_CPU :
  print('Empate')
elif option_gamer == 'piedra' and option_CPU == 'papel':
  print('Perdiste')
elif option_gamer == 'piedra' and option_CPU == 'tijera':
  print('Ganaste')
elif option_gamer == 'tijera' and option_CPU  == 'papel':
  print('Ganaste')
elif option_gamer == 'tijera' and option_CPU  == 'piedra':
  print('Perdiste')
elif option_gamer == 'papel' and option_CPU  == 'piedra':
  print('Ganaste')
elif option_gamer == 'papel' and option_CPU  == 'tijera':
  print('Perdiste')


#Generado por IA
if option_gamer == option_CPU:
  print('Empate')
elif (option_gamer == 'piedra' and option_CPU == 'papel') or (option_gamer == 'tijera' and option_CPU == 'piedra') or (option_gamer == 'papel' and option_CPU == 'tijera'):
  print('Perdiste')
else:
  print('Ganaste')

