import requests #dependency
import random #random``
import tkinter as tk
import time #time

imput = ''
url = "WEBHOOK" 

def on_check_button_click():
    if check_var.get():
        print(check_var)
    else:
        print(check_var)

def afficher_texte():
   if check_var.get():
      for i in range(int(entreetxt.get())):
            imput = entree_texte.get()
            data = {
               "content" : "",
               "username" : "hookers gang"
            }
 
            data["embeds"] = [
            {
               "description" : "",
               "title" : imput,
               "color": "14177041"
            }
            ]

            result = requests.post(url, json = data)
            try:
               result.raise_for_status()
            except requests.exceptions.HTTPError as err:
               print(err)
            else:
               print("Payload delivered successfully, code {}.".format(result.status_code))
            time.sleep(1)
   else:
    imput = entree_texte.get()
    data = {
       "content" : "",
       "username" : "hookers gang"
    }
 
    data["embeds"] = [
    {
        "description" : "",
        "title" : imput,
        "color": "14177041"
    }
    ]

    result = requests.post(url, json = data)
    try:
       result.raise_for_status()
    except requests.exceptions.HTTPError as err:
       print(err)
    else:
       print("Payload delivered successfully, code {}.".format(result.status_code))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("webhook sender")

# Création d'un label
label = tk.Label(fenetre, text="Entrez votre texte:")
label.pack()

# Création d'un champ de texte
entree_texte = tk.Entry(fenetre)
entree_texte.pack()

# Création d'un bouton
bouton = tk.Button(fenetre, text="Send", command=afficher_texte)
bouton.pack()

# checkbox
check_var = tk.BooleanVar()

# Créer la check box et l'ajouter à la fenêtre
check_button = tk.Checkbutton(fenetre, text="loop", variable=check_var, command=on_check_button_click)
check_button.pack(padx=10, pady=10)

#delay
entreetxt = tk.Entry(fenetre)
entreetxt.pack()
# Lancement de la boucle principale
fenetre.mainloop()
