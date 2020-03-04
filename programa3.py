def multiple():
    # Esto es una lista que representa elalfabeto español
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Esto es una lista donde se almacenarán los elementos resultantes
    results = []

    # Se recorre el alfabeto enumerado para tener el valor y la posición
    # Se obtiene una tupla con la posición y el elemento al llamar al médoto enumerate
    for position, letter in enumerate(alphabet):
        
        # Valida si es un elemento no multiplo de 3
        # Se valida con la posición + 1 porque los índices empiezan en 0
        if (position + 1) % 3 != 0:
            # Se añade el elemento no multiplo de 3 a la lista usando el médoto append y el valor en letter
            results.append(letter)

    # Se pide el resultado
    print(results)