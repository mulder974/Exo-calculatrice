def ask_user(sentence = "Saisir un chiffre"): # do_something $
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number): # do_something $
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers) # do_something
    return result
    
def soustraction(number):
    list_numbers = []
    while number.isdigit(): # do_something
        if number.isdigit():
            list_numbers.append(int(number)) # do_something
        number = ask_user("Saisir un ciffre à soustraire ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return aaaa

def multplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # do_something $
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0: 
            result = list_number
        else:
            result = result * list_number # do_something
        i = i + 1
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # do_something
        number = ask_user("Saisir un ciffre à diviser ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result / list_number # do_something
        i = i + 1
    return result

menu = """
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4"""

def display_interface():
    choice = ask_user(menu)
    while choice.isdigit():
        if choice == "1":
            choice = ask_user("Saisir un ciffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == "2":
            choice = ask_user("Saisir un ciffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == "3":
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(choice)
        elif choice == "4":
            choice = ask_user("Saisir un ciffre à DIVISER ou clicker sur '=' ")
            result = division(choice)
        else: 
            result = "Veuillez entrez un chiffre valid"

        print(f"Le resultat est ==> {result}")
        choice = ask_user(menu)


