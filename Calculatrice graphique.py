import tkinter as tk

# Fonction pour mettre à jour l'affichage du calcul
def press(key):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(key))

# Fonction pour calculer l'expression
def calculate():
    try:
        current = display.get()
        result = eval(current) 
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erreur")

# Fonction pour vider l'affichage
def clear():
    display.delete(0, tk.END)

# Fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Zone d'affichage
display = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

# Boutons de la calculatrice
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Création des boutons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda key=text: press(key))
    btn.grid(row=row, column=col)

# Démarrer l'application
root.mainloop()
