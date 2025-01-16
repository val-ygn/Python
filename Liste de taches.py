import tkinter as tk

# Fonction pour ajouter une tâche
def ajouter_tache():
    tache = entry_tache.get()
    if tache:
        listbox_taches.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)

# Fonction pour supprimer une tâche
def supprimer_tache():
    try:
        selected_task = listbox_taches.curselection()
        listbox_taches.delete(selected_task)
    except IndexError:
        pass

# Fenêtre principale
root = tk.Tk()
root.title("To-Do List")

# Entrée pour ajouter des tâches
entry_tache = tk.Entry(root, width=40)
entry_tache.pack(pady=10)

# Bouton pour ajouter des tâches
btn_ajouter = tk.Button(root, text="Ajouter", width=20, command=ajouter_tache)
btn_ajouter.pack(pady=10)

# Liste des tâches
listbox_taches = tk.Listbox(root, width=40, height=10)
listbox_taches.pack(pady=10)

# Bouton pour supprimer une tâche
btn_supprimer = tk.Button(root, text="Supprimer", width=20, command=supprimer_tache)
btn_supprimer.pack(pady=10)

# Démarrer l'application
root.mainloop()
