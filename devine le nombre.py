import random

def deviner_le_nombre():
    print("Bienvenue dans le jeu Devine le Nombre !")
    nombre_secret = random.randint(1, 100)
    essais = 0
    devine = False

    print("Je pense à un nombre entre 1 et 100. À toi de deviner !")

    while not devine:
        try:
            guess = int(input("Entre ton nombre : "))
            essais += 1

            if guess < nombre_secret:
                print("C'est plus !")
            elif guess > nombre_secret:
                print("C'est moins !")
            else:
                print(f"Bravo ! Tu as trouvé en {essais} essais !")
                devine = True
        except ValueError:
            print("S'il te plaît, entre un nombre valide.")

# Lancer le jeu
deviner_le_nombre()
