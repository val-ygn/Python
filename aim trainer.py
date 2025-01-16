import tkinter as tk
import random

# Initialisation des variables globales
score = 0
time_left = 30  # Temps en secondes
button_size = 50  # Taille initiale du bouton

# Fonction pour déplacer le bouton à un nouvel endroit aléatoire
def move_button():
    global score, button_size

    # Augmenter le score
    score += 1
    score_label.config(text=f"Score : {score}")
    
    # Réduire la taille du bouton pour augmenter la difficulté
    button_size = max(20, button_size - 1)  # Taille minimale de 20
    button.config(width=button_size // 10, height=button_size // 20)

    # Déplacer le bouton à une position aléatoire
    new_x = random.randint(0, window.winfo_width() - button_size)
    new_y = random.randint(0, window.winfo_height() - button_size)
    button.place(x=new_x, y=new_y)

# Fonction pour mettre à jour le chronomètre
def update_timer():
    global time_left

    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Temps restant : {time_left}s")
        window.after(1000, update_timer)  # Appelle cette fonction dans 1 seconde
    else:
        end_game()

# Fonction pour terminer le jeu
def end_game():
    button.place_forget()  # Cache le bouton
    timer_label.config(text="Temps écoulé !")
    result_label.config(text=f"Votre score final : {score}")

# Initialisation de la fenêtre principale
window = tk.Tk()
window.title("Aim Trainer")
window.geometry("600x400")

# Chronomètre
timer_label = tk.Label(window, text=f"Temps restant : {time_left}s", font=("Arial", 14))
timer_label.pack()

# Score
score_label = tk.Label(window, text=f"Score : {score}", font=("Arial", 14))
score_label.pack()

# Résultat
result_label = tk.Label(window, text="", font=("Arial", 16), fg="red")
result_label.pack()

# Bouton d'entraînement
button = tk.Button(window, text=" ", command=move_button)
button.place(x=100, y=100)

# Lancer le chronomètre
update_timer()

# Lancer l'application
window.mainloop()
