def validar_tarjeta(numero_tarjeta):
    # Eliminar espacios en blanco
    numero_tarjeta = numero_tarjeta.replace(" ", "")

    # Verificar si el número de tarjeta es solo numérico
    if not numero_tarjeta.isdigit():
        return False

    # Verificar longitud del número de tarjeta (debe ser entre 13 y 19 dígitos según las normas comunes)
    if not (13 <= len(numero_tarjeta) <= 19):
        return False

    # Convertir número de tarjeta en una lista de dígitos
    digitos = list(map(int, numero_tarjeta))

    # Aplicar el algoritmo de Luhn
    checksum = 0
    for i in range(len(digitos) - 1, -1, -1):
        if (len(digitos) - i) % 2 == 0:
            doubled = digitos[i] * 2
            checksum += doubled if doubled < 10 else doubled - 9
        else:
            checksum += digitos[i]

    # La tarjeta es válida si el checksum es divisible por 10
    return checksum % 10 == 0

def main():
    # Solicitar al usuario que ingrese el número de tarjeta
    numero_tarjeta = input("Ingrese el número de tarjeta de crédito: ")

    # Validar el número de tarjeta
    if validar_tarjeta(numero_tarjeta):
        print(f"El número de tarjeta {numero_tarjeta} es válido.")
    else:
        print(f"El número de tarjeta {numero_tarjeta} no es válido.")

if __name__ == "__main__":
    main()
