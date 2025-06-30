# Este programa calcula el área de un círculo y convierte unidades de longitud
# entre metros y kilómetros. Utiliza diferentes tipos de datos y sigue la
# convención de identificadores snake_case.

import math

def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.
    
    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    return math.pi * (radio ** 2)

def convertir_metros_a_kilometros(metros: float) -> float:
    """
    Convierte metros a kilómetros.
    
    :param metros: La longitud en metros.
    :return: La longitud en kilómetros.
    """
    return metros / 1000

def convertir_kilometros_a_metros(kilometros: float) -> float:
    """
    Convierte kilómetros a metros.
    
    :param kilometros: La longitud en kilómetros.
    :return: La longitud en metros.
    """
    return kilometros * 1000

def main():
    # Solicitar al usuario el radio del círculo
    radio_str = input("Ingrese el radio del círculo en metros: ")
    radio = float(radio_str)  # Convertir a float

    # Calcular el área del círculo
    area = calcular_area_circulo(radio)
    print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")

    # Solicitar al usuario una longitud en metros
    metros_str = input("Ingrese una longitud en metros para convertir a kilómetros: ")
    metros = float(metros_str)  # Convertir a float

    # Convertir metros a kilómetros
    kilometros = convertir_metros_a_kilometros(metros)
    print(f"{metros} metros son {kilometros:.2f} kilómetros.")

    # Solicitar al usuario una longitud en kilómetros
    kilometros_str = input("Ingrese una longitud en kilómetros para convertir a metros: ")
    kilometros = float(kilometros_str)  # Convertir a float

    # Convertir kilómetros a metros
    metros_convertidos = convertir_kilometros_a_metros(kilometros)
    print(f"{kilometros} kilómetros son {metros_convertidos:.2f} metros.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
