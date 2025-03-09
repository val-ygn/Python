# Avant de lancer ce programme, il faut faire cette commande dans le terminal : pip install pandas openpyxl pip install vobject
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import pandas as pd
import vobject  # Importation de la bibliothèque pour lire les fichiers vCard

# Initialisation de la liste de contacts
contacts = []

# Fonction pour mettre à jour la vue des contacts dans l'interface
def mettre_a_jour_liste():
    for row in tree.get_children():
        tree.delete(row)
    for i, contact in enumerate(contacts, start=1):
        tree.insert("", "end", values=(i, contact["Nom"], contact["Prénom"], contact["Téléphone"], contact["Email"]))

# Vérifier si un contact est un doublon
def est_doublon(contact):
    for c in contacts:
        if (c["Nom"] == contact["Nom"] and
            c["Prénom"] == contact["Prénom"] and
            c["Téléphone"] == contact["Téléphone"] and
            c["Email"] == contact["Email"]):
            return True
    return False

# Ajouter un contact
def ajouter_contact():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    telephone = entry_telephone.get()
    email = entry_email.get()
    if nom and prenom and telephone and email:
        nouveau_contact = {"Nom": nom, "Prénom": prenom, "Téléphone": telephone, "Email": email}
        if not est_doublon(nouveau_contact):
            contacts.append(nouveau_contact)
            mettre_a_jour_liste()
            entry_nom.delete(0, tk.END)
            entry_prenom.delete(0, tk.END)
            entry_telephone.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Doublon détecté", "Ce contact existe déjà.")
    else:
        messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")

# Supprimer un contact
def supprimer_contact():
    selected_item = tree.selection()
    if selected_item:
        index = int(tree.item(selected_item)["values"][0]) - 1
        del contacts[index]
        mettre_a_jour_liste()
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un contact à supprimer.")

# Exporter vers Excel
def exporter_excel():
    if not contacts:
        messagebox.showwarning("Attention", "Aucun contact à exporter.")
        return
    fichier = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if fichier:
        df = pd.DataFrame(contacts)
        df.to_excel(fichier, index=False, engine="openpyxl")
        messagebox.showinfo("Succès", f"Contacts exportés dans {fichier}.")

# Exporter vers CSV
def exporter_csv():
    if not contacts:
        messagebox.showwarning("Attention", "Aucun contact à exporter.")
        return
    fichier = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if fichier:
        df = pd.DataFrame(contacts)
        df.to_csv(fichier, index=False)
        messagebox.showinfo("Succès", f"Contacts exportés dans {fichier}.")

# Importer depuis vCard
def importer_vcard():
    fichier = filedialog.askopenfilename(filetypes=[("vCard Files", "*.vcf"), ("All Files", "*.*")])
    if fichier:
        try:
            doublons_ignores = 0
            with open(fichier, "r") as file:
                vcf_data = file.read()
                vcards = vobject.readComponents(vcf_data)
                for vcard in vcards:
                    try:
                        nom = vcard.fn.value.split()[0] if hasattr(vcard, 'fn') else ""
                        prenom = vcard.fn.value.split()[1] if len(vcard.fn.value.split()) > 1 else ""
                        email = vcard.email.value if hasattr(vcard, 'email') else ""
                        telephone = vcard.tel.value if hasattr(vcard, 'tel') else ""

                        # Création du contact
                        nouveau_contact = {"Nom": nom, "Prénom": prenom, "Téléphone": telephone, "Email": email}

                        # Ajouter le contact s'il n'est pas un doublon
                        if not est_doublon(nouveau_contact):
                            contacts.append(nouveau_contact)
                        else:
                            doublons_ignores += 1
                    except Exception as e:
                        print(f"Erreur lors de la lecture d'un contact : {e}")
            mettre_a_jour_liste()
            if doublons_ignores > 0:
                messagebox.showinfo("Importation terminée", f"Importation réussie.\n{doublons_ignores} doublon(s) ignoré(s).")
            else:
                messagebox.showinfo("Importation terminée", "Tous les contacts ont été importés avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'importer le fichier vCard : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de Contacts")

# Cadre pour les champs d'entrée
frame_entrer = tk.Frame(root)
frame_entrer.pack(pady=10)

tk.Label(frame_entrer, text="Nom").grid(row=0, column=0, padx=5, pady=5)
entry_nom = tk.Entry(frame_entrer)
entry_nom.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrer, text="Prénom").grid(row=1, column=0, padx=5, pady=5)
entry_prenom = tk.Entry(frame_entrer)
entry_prenom.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrer, text="Téléphone").grid(row=2, column=0, padx=5, pady=5)
entry_telephone = tk.Entry(frame_entrer)
entry_telephone.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_entrer, text="Email").grid(row=3, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_entrer)
entry_email.grid(row=3, column=1, padx=5, pady=5)

btn_ajouter = tk.Button(frame_entrer, text="Ajouter Contact", command=ajouter_contact)
btn_ajouter.grid(row=4, column=0, columnspan=2, pady=10)

# Tableau pour afficher les contacts
frame_tableau = tk.Frame(root)
frame_tableau.pack(pady=10)

columns = ("#", "Nom", "Prénom", "Téléphone", "Email")
tree = ttk.Treeview(frame_tableau, columns=columns, show="headings", height=10)
tree.pack(side="left")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

# Barre de défilement pour le tableau
scrollbar = ttk.Scrollbar(frame_tableau, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscroll=scrollbar.set)

# Cadre pour les boutons d'action
frame_actions = tk.Frame(root)
frame_actions.pack(pady=10)

btn_supprimer = tk.Button(frame_actions, text="Supprimer Contact", command=supprimer_contact)
btn_supprimer.grid(row=0, column=0, padx=5)

btn_exporter_excel = tk.Button(frame_actions, text="Exporter vers Excel", command=exporter_excel)
btn_exporter_excel.grid(row=0, column=1, padx=5)

btn_exporter_csv = tk.Button(frame_actions, text="Exporter vers CSV", command=exporter_csv)
btn_exporter_csv.grid(row=0, column=2, padx=5)

btn_importer_vcard = tk.Button(frame_actions, text="Importer depuis vCard", command=importer_vcard)
btn_importer_vcard.grid(row=1, column=0, padx=5)

# Lancer la fenêtre principale
root.mainloop()
