import random


# Función que define al DFA del primer punto, con sus estados y transiciones
def dfa1():
    initial_state = 0
    final_state = 0

    transition_table = {
        (0, '0'): 0,
        (0, '1'): 1,
        (1, '0'): 2,
        (1, '1'): 0,
        (2, '0'): 1,
        (2, '1'): 2,
    }


# Función que lee el string ingresado por el usuario
def read_string():
    binary_number = input('Please write the string of any length you want in binary (1s and 0s): ')
    binary_number = binary_number.strip()
    return binary_number


# Función que valida si el string está vacío o no es binario
def validate_empty_or_non_binary_string(binary_number):
    printed_message = False #Empezamos con que todavía no se ha impreso ningún mensaje

    #Verifica si el string está vacío
    if not binary_number:
        print('The DFA accepts the string') #Imprime si está vacío

    # Verifica si el string es numérico y si no...
    elif not binary_number.isnumeric():
        if not printed_message:
            print('The DFA rejects the string') #Se imprime si todavía no se había impreso nada
            mensaje_impreso = True

    # Si el string es numérico...
    else:
        is_binary = True

        #Revisamos los digitos del string a ver si son distintos de 0-1
        for digit in binary_number:
            if digit not in '01':
                is_binary = False
                break
        if not is_binary:
            if not printed_message:
                print('The DFA rejects the string') #Se imprime si el numero no es binario
                mensaje_impreso = True


# Función para convertir el número binario ingresado a base 10
def convertion_to_decimal(binary_number):
    decimal_number = 0

    # Ciclo que recorre todos los digitos del string binario y va realizando la conversión
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * (2 ** (len(binary_number) - i - 1))
    return decimal_number


# Función que revisa si el número en base 10 es divisible por 3
def divisible_by_3 (decimal_number):
    is_divisible = True
    if decimal_number % 3 == 0:
        return is_divisible
    else:
        is_divisible = False
        return is_divisible


# Función que imprime el mensaje dependiendo de si el número es múltiplo de 3 o no
def print_message(is_divisible):
    if is_divisible == True:
        print('The DFA accepts the string')
    else:
        print('The DFA rejects the string')


# Acá empieza el segundo punto, con una función que pide el tamaño para la generación del string
def ask_size():
    size = int(input('Please enter the size you want for the string: '))
    return size


# Función que le pide al usuario si quiere que el string tenga una cantidad de 1s múltiplo de 3 o no
def ones_multiple_of_3():
    multiple_of_3_1s = True
    answer = int(input('Please enter 1 if you want the generated string to have an amount of ones which is multiple of 3, or enter 0 if you dont want to: '))
    if answer == 1:
        return multiple_of_3_1s
    elif answer == 0:
        multiple_of_3_1s = False
        return multiple_of_3_1s
    else:
        print('You wrote an invalid answer...')


# Función que genera el string con los parametros de tamaño y cantidad de 1s múltiplo de 3 ingresados por el usuario
def generate_string(size, multiple_of_3_1s):
    # Generar un string binario de longitud 'size' con solo 0s
    binary_string = '0' * size

    # Calcular el número de 1s que se necesitan
    if multiple_of_3_1s == True:
        ones_count = 3 * (size // random.randint(1, size - 1))  # Hacer que el número de 1s sea múltiplo de 3
    else:
        ones_count = 2 * (size // random.randint(1, size - 1))  # Elegir un número aleatorio de 1s que sea multiplo de 2, para ahorrar tiempo de ejecución
        """
        while ones_count % 3 == 0:
            ones_count = random.randint(1, size - 1)
        """

    # Colocar los 1s en posiciones aleatorias del string
    ones_positions = random.sample(range(size), ones_count)   # Creamos una lista con las posiciones aleatorias de los 1s (ones_count nos da la cantidad de posiciones) dentro del rango de size
    for pos in ones_positions:   # Iteramos todas las posiciones aleatorias de la lista
        binary_string = binary_string[:pos] + '1' + binary_string[pos + 1:]   # Reemplaza el carácter en la posición pos de binary_string por '1' y se asigna de nuevo a binary_string, y así vamos construyendo el string con 1s en posiciones random

    return binary_string, ones_count


# Función con la que validamos que el número de 1s que contiene el string sea múltiplo de 3 e imprimimos el mensaje correspondiente
def validate_multiple_of_3(binary_string, ones_count):
    if ones_count % 3 == 0:
        print('The DFA accepts the string')
    else:
        print('The DFA rejects the string')



def main():
    binary_number = read_string()
    validate_empty_or_non_binary_string(binary_number)
    decimal_number = convertion_to_decimal(binary_number)
    print('Your binary number, converted to decimal, is:', decimal_number)
    is_divisible = divisible_by_3(decimal_number)
    print_message(is_divisible)

    print()
    size = ask_size()
    multiple_of_3_1s = ones_multiple_of_3()
    binary_string, ones_count = generate_string(size, multiple_of_3_1s)
    #print('The generated string:', binary_string)
    print('The size of the String is:', size)
    print('The number of ones:', ones_count)
    validate_multiple_of_3(binary_string, ones_count)



if __name__ == '__main__':
    main()