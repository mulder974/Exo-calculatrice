
def addition(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre à additionner, entrée pour obtenir le résultat: ")
        if number.isdigit():
            list_numbers.append(float(number))

    return sum(list_numbers)


def soustraction(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre à additionner, entrée pour obtenir le résultat: ")

        if number.isdigit():
            list_numbers.append(float(number))

    first_number = list_numbers[0]
    result = first_number
    del list_numbers[0]
    for e in list_numbers:
        result -= e

    return result


def multplication(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre à additionner, entrée pour obtenir le résultat: ")

        if number.isdigit():
            list_numbers.append(float(number))

    result = 1
    for e in list_numbers:
        result *= e

    return result


def division(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre à diviser, entrée pour obtenir le résultat: ")

        if number.isdigit():
            list_numbers.append(float(number))

    first_number = list_numbers[0]
    result = first_number
    del list_numbers[0]

    for e in list_numbers:
        result /= e

    return result


def exposer(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre, entrée pour obtenir le résultat: ")
        if number.isdigit():
            list_numbers.append(float(number))

    first_number = list_numbers[0]
    result = first_number
    del list_numbers[0]

    for e in list_numbers:
        result **= e

    return result

def racine(number):
    list_numbers = []
    while number.isdigit():
        number = input("Saisir un chiffre, entrée pour obtenir le résultat: ")

        if number.isdigit():
            list_numbers.append(float(number))

    first_number = list_numbers[0]
    result = first_number
    del list_numbers[0]

    for e in list_numbers:
        result **= 1/e

    return result

def fibonnaci():
    n = int(input("Entrez le nombre d'élements que vous souhaitez afficher pour la suite"))

    n1 = 0
    n2 = 1
    list = [n1, n2]

    for i in range(2, n):
        suivant = n1 + n2
        list.append(suivant)
        n1 = n2
        n2 = suivant

    return list

def joke():
    print(" Clément est con :P ")

