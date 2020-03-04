def palindromo():
    x = input("Favor ingrese su texto o palabra a evaluar: ")

    # Se reemplazan los espacios en blanco con vacío porque los palíndromos pueden ser frases
    x = x.replace(' ', '')

    if x == x[::-1]:
       print("Es un palíndromo")
    else:
        print("No es un palíndromo")