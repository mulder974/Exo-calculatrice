from calculatrice import addition, multplication, division, soustraction, exposer, racine, joke, fibonnaci


def display_interface():
    choice = 1
    while int(choice) != 0:
        choice = input("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4
        5. Exposer Tape 5
        6. Mettre à la racine Tape 6
        7  Afficher la suite de Fibonnaci tape 7
        8. Connaitre la vérité Tape 8
        0. Quitter Tape 0
        """)

        try:
            int(choice)

        except ValueError:
            print('Merci de rentrer un chiffre valide')
            continue

        if int(choice) == 0:
            break

        elif int(choice) == 1:
            result = addition(choice)

        elif int(choice) == 2:
            result = soustraction(choice)

        elif int(choice) == 3:
            result = multplication(choice)

        elif int(choice) == 4:
            result = division(choice)

        elif int(choice) == 5:
            result = exposer(choice)

        elif int(choice) == 6:
            result = racine(choice)

        elif int(choice) == 7:
            result = fibonnaci()

        elif int(choice) == 8:
            joke()
            continue



        print(f"Le resultat est ==> {result}")

    print('\n\nArrêt du programme........ \n PS: Clément est con :D ')


display_interface()
