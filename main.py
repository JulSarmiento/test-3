from menu import menu, salir
from programa1 import palindromo
from programa2 import lista
from programa3 import multiple
from programa4 import asignaturas

import os 

while True: 

    x = menu()

    if x == 'a':
        palindromo()
    elif x == 'b':
        lista()
    elif x == 'c':
        multiple()
    elif x == 'd':
        asignaturas()
    elif x == 'e':
        salir()
    else:
        input('Buen día, favor seleccione una opción: ')
        os.system('cls||clear')