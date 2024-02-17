import random

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


def read_string():
    binary_number = input('Please write the string of any length you want in binary (1s and 0s): ')
    binary_number = binary_number.strip()
    return binary_number


def validate_empty_or_non_binary_string(binary_number):
    printed_message = False

    if not binary_number:
        print('The DFA accepts the string')
    elif not binary_number.isnumeric():
        if not printed_message:
            print('The DFA rejects the string')
            mensaje_impreso = True
    else:
        is_binary = True
        for digit in binary_number:
            if digit not in '01':
                is_binary = False
                break
        if not is_binary:
            if not printed_message:
                print('The DFA rejects the string')
                mensaje_impreso = True


def convertion_to_decimal(binary_number):
    decimal_number = 0
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * (2 ** (len(binary_number) - i - 1))
    return decimal_number


def divisible_by_3 (decimal_number):
    is_divisible = True
    if decimal_number % 3 == 0:
        return is_divisible
    else:
        is_divisible = False
        return is_divisible


def print_message(is_divisible):
    if is_divisible == True:
        print('The DFA accepts the string')
    else:
        print('The DFA rejects the string')


def ask_size():
    size = int(input('Please enter the size you want for the string: '))
    return size


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


def generate_string(size, multiple_of_3_1s):
    # Generar un string binario de longitud 'size' con solo 0s
    binary_string = '0' * size

    # Calcular el número de 1s que se necesitan
    if multiple_of_3_1s == True:
        ones_count = 3 * (size // random.randint(1, size - 1))  # Hacer que el número de 1s sea múltiplo de 3
    else:
        ones_count = 2 * (size // random.randint(1, size - 1))  # Elegir un número aleatorio de 1s que no sea múltiplo de 3
        while ones_count % 3 == 0:
            ones_count = random.randint(1, size - 1)

    # Colocar los 1s en posiciones aleatorias del string
    ones_positions = random.sample(range(size), ones_count)
    for pos in ones_positions:
        binary_string = binary_string[:pos] + '1' + binary_string[pos + 1:]

    return binary_string, ones_count


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