# Importation des programmes nécessaires
import folium
import webbrowser
import time

# Créer une carte centrée sur le point [0, 0]
carte = folium.Map(location=[47.214522, -1.550184], zoom_start=15)

# Ajouter un marqueur "Paris"
folium.Marker([48.8566, 2.3522], popup="Paris").add_to(carte)

# Enregistrer la carte dans un fichier HTML
carte.save('carte1.html')

# Répéter 100 fois
for i in range(100):  
    print(" ")

print("Carte crée et enregistrée dans 'carte1.html'.")
nom_fichier = "carte1.html"

# Pause de 5 secondes avec la fonction time.sleep
time.sleep(5) 

for i in range(100):  # Répéter 100 fois
    print(" ")

# Pause de 5 secondes avec la fonction time.sleep
time.sleep(5) 

# Ouvrir automatiquement le fichier
print("Ouverture du fichier en cours...")

# Pause de 5 secondes avec la fonction time.sleep
time.sleep(5) 

# Répéter 5 fois
for i in range(5): 
    print(" ")

# Ouvrir la carte
webbrowser.open(nom_fichier)

# Répéter 100 fois
for i in range(100):  
    print(" ")
