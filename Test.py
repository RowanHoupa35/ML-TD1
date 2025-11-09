def hello_world():
    print("Hello, World!")


def addition_de_deux_nombres():
    a = float(input("Entrez le premier nombre: "))
    b = float(input("Entrez le deuxième nombre: "))
    print("La somme est:", a + b)


def conversion_celsius_fahrenheit_fahrenheit_celsius():
    choice = input("Choisissez une option (1-2): ")
    if choice == '1':
        celsius = float(input("Entrez la température en Celsius: "))
        fahrenheitTemp = (celsius * 9 / 5) + 32
        print(f"Celsius: {celsius} -> Fahrenheit: {fahrenheitTemp}")
    elif choice == '2':
        fahrenheit = float(input("Entrez la température en fahrenheit: "))
        celsiusTemp = (fahrenheit - 32) * 5 / 9
        print(f"Fahrenheit: {fahrenheit} -> Celsius: {celsiusTemp}")
    else:
        print("Option invalide, veuillez réessayer.")


def calcul_factorielle():
    import math
    n = int(input("Entrez un nombre: "))
    print(f"Factorielle de {n} est {math.factorial(n)}")


def liste_nombres_pairs():
    n = int(input("Entrez un nombre: "))
    pairs = [i for i in range(n + 1) if i % 2 == 0]
    print(f"Nombres pairs jusqu'à {n}:", pairs)


def liste_nombres_premiers():
    def est_premier(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = int(input("Entrez un nombre: "))
    premiers =[i for i in range(2, n + 1) if est_premier(i)]
    print(f"Nombres premiers jusqu'à {n}:", premiers)


def table_multiplication():
    def multiplication(n):
        if n == 0:
            print("Les valeurs obtenues pour la table de multiplication de 0 sont toutes 0.")
        else:
            print(f"La table de multiplication de {n} est :")
            for i in range(1, 11):
                print(f"{n} * {i} = {n * i}")

    val = int(input("Veuillez entrer un nombre/chiffre : "))
    multiplication(val)


def Nombres_voyelles():
    def liste_voyelles(text):
        n = 0
        voyelles = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
        for char in text:
            if char in voyelles:
                n += 1
        print(f"Le nombre de voyelles dans le texte entré est : {n}")

    essay = input("Veuillez entrer un texte : ")
    liste_voyelles(essay)

def retourner_mot ():
    def reverse_w(mot):
        reverse = ''
        for char in mot:
            reverse = char + reverse
        print(f"La version renversée de {mot} est: {reverse}")

    word = str(input('Entrez un mot: '))
    reverse_w(word)

def Trouver_nombre():
    import random

    def deviner_nombre():
        nombre_a_deviner = random.randint(1, 100)
        essais = 0
        devine = False

        print("Bienvenue dans le jeu de devinette!")
        print("J'ai choisi un nombre entre 1 et 100. Pouvez-vous le deviner?")

        while not devine:
            try:
                utilisateur_essai = int(input("Entrez votre devinette : "))
                essais += 1

                if utilisateur_essai < 1 or utilisateur_essai > 100:
                    print("Veuillez entrer un nombre entre 1 et 100.")
                elif utilisateur_essai < nombre_a_deviner:
                    print("C'est plus grand.")
                elif utilisateur_essai > nombre_a_deviner:
                    print("C'est plus petit.")
                else:
                    print(f"Félicitations! Vous avez deviné le nombre en {essais} essais.")
                    devine = True
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    deviner_nombre()


def Moyene():
    import statistics
    valeurs = input("Entrez vos valeurs les unes après les autres séparées par une virgule: ")
    valeurs_liste = [float(val) for val in valeurs.split(',')]
    moyenne = statistics.mean(valeurs_liste)
    print(f"La moyenne est: {moyenne}")


def calcul_de_l_ecart_type():
    import statistics
    data = list(map(float, input("Entrez les nombres séparés par des espaces: ").split()))
    ecart_type = statistics.stdev(data)
    print(f"L'écart type est: {ecart_type}")


# Ajoutez toutes les autres fonctions ici

def menu():
    print("\nOptions:")
    print("1. Hello World")
    print("2. Addition de deux nombres")
    print("3. Celsius -> Fahrenheit & Fahrenheit -> Celsius")
    print("4. Calcul Factorielle")
    print("5. Liste des nombres pairs jusqu'à n")
    print("6. Liste des nombres premiers jusqu'à n")
    print("7. Table de mutiplication de n")
    print("8. Nombres de voyelles présentes dans un texte")
    print("9. Retourner/inverser une chaines de caractères")
    print("10. Deviner un nombre aléatoirement choisi par l'ordinateur")
    print("11. Calculer la moyenne des valeurs d'une liste")
    # Ajoutez toutes les autres options ici
    print("50. Calcul de l'écart type")
    print("0. Quitter")

def main():
    while True:
        menu()
        choice = input("Choisissez une option (0-50): ")
        if choice == '0':
            break
        elif choice == '1':
            hello_world()
        elif choice == '2':
            addition_de_deux_nombres()
        elif choice == '3':
            conversion_celsius_fahrenheit_fahrenheit_celsius()
        elif choice == '4':
            calcul_factorielle()
        elif choice == '5':
            liste_nombres_pairs()
        elif choice == '6':
            liste_nombres_premiers()
        elif choice == '7':
            table_multiplication()
        elif choice == '8':
            Nombres_voyelles()
        elif choice == '9':
            retourner_mot()
        elif choice == '10':
            Trouver_nombre()
        elif choice == '11':
            Moyene()
        # Ajoutez toutes les autres options ici
        elif choice == '50':
            calcul_de_l_ecart_type()
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
