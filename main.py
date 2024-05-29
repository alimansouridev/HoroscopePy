# ⚠️⚠️⚠️ LES HOROSCOPES SONT FAUX, À UTILISER AVEC PRUDENCE ⚠️⚠️⚠️
# ⚠️⚠️⚠️ LES HOROSCOPES SONT FAUX, À UTILISER AVEC PRUDENCE ⚠️⚠️⚠️
# ⚠️⚠️⚠️ LES HOROSCOPES SONT FAUX, À UTILISER AVEC PRUDENCE ⚠️⚠️⚠️
# ⚠️⚠️⚠️ LES HOROSCOPES SONT FAUX, À UTILISER AVEC PRUDENCE ⚠️⚠️⚠️

# Messagebox est utilisé a travers le code https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
# Importations des modules
import tkinter as tk
from tkinter import ttk, messagebox
import random


# Fonction pour vérifier si une chaîne peut être convertie en nombre entier
# Python Try Except https://www.geeksforgeeks.org/python-try-except/
def est_nombre(chaine):
    try:
        int(chaine)
        return True
    except ValueError:
        return False


# Fonction pour vérifier si l'année est valide (entre 1900 et 2023)
def est_annee_valide(annee):
    return est_nombre(annee) and 1900 <= int(annee) <= 2023


# Fonction pour vérifier si le jour est valide (entre 1 et 31)
def est_jour_valide(jour):
    return est_nombre(jour) and 1 <= int(jour) <= 31


# Fonction pour vérifier si le mois est valide (entre 1 et 12)
def est_mois_valide(mois):
    return est_nombre(mois) and 1 <= int(mois) <= 12


# Fonction pour obtenir le signe astrologique en fonction du jour et du mois
def obtenir_signe_astrologique(jour, mois):
    if (mois == 3 and jour >= 21) or (mois == 4 and jour <= 19):
        return "Bélier"
    elif (mois == 4 and jour >= 20) or (mois == 5 and jour <= 20):
        return "Taureau"
    elif (mois == 5 and jour >= 21) or (mois == 6 and jour <= 20):
        return "Gémeaux"
    elif (mois == 6 and jour >= 21) or (mois == 7 and jour <= 22):
        return "Cancer"
    elif (mois == 7 and jour >= 23) or (mois == 8 and jour <= 22):
        return "Lion"
    elif (mois == 8 and jour >= 23) or (mois == 9 and jour <= 22):
        return "Vierge"
    elif (mois == 9 and jour >= 23) or (mois == 10 and jour <= 22):
        return "Balance"
    elif (mois == 10 and jour >= 23) or (mois == 11 and jour <= 21):
        return "Scorpion"
    elif (mois == 11 and jour >= 22) or (mois == 12 and jour <= 21):
        return "Sagittaire"
    elif (mois == 12 and jour >= 22) or (mois == 1 and jour <= 19):
        return "Capricorne"
    elif (mois == 1 and jour >= 20) or (mois == 2 and jour <= 18):
        return "Verseau"
    else:
        return "Poissons"


# Fonction pour obtenir les nombres chanceux en fonction du signe astrologique
def obtenir_nombres_chanceux(signe):
    nombres_chanceux = {
        "Bélier": [1, 9, 10, 19],
        "Taureau": [2, 8, 12, 21],
        "Gémeaux": [3, 7, 13, 22],
        "Cancer": [4, 6, 14, 23],
        "Lion": [5, 11, 15, 24],
        "Vierge": [9, 14, 18, 27],
        "Balance": [6, 15, 20, 30],
        "Scorpion": [8, 18, 22, 31],
        "Sagittaire": [3, 7, 12, 21],
        "Capricorne": [5, 14, 18, 24],
        "Verseau": [7, 15, 21, 29],
        "Poissons": [2, 9, 12, 27],
    }
    # get() : renvoie le texte actuel de l'entrée sous forme de chaîne.
    return nombres_chanceux.get(signe, [])


# Fonction pour afficher les traits de personnalité en fonction du signe astrologique
def afficher_traits_personnalite(signe, jour, mois, annee):
    traits_personnalite = {
        "Bélier": "Aventureux, énergique, confiant, impulsif",
        "Taureau": "Patient, déterminé, fiable, têtu",
        "Gémeaux": "Adaptable, intelligent, sociable, indécis",
        "Cancer": "Nurturant, sensible, protecteur, lunatique",
        "Lion": "Charismatique, généreux, passionné, autoritaire",
        "Vierge": "Analytique, fiable, modeste, préoccupé par les détails",
        "Balance": "Sociable, équilibré, charmeur, indécis",
        "Scorpion": "Passionné, déterminé, mystérieux, intense",
        "Sagittaire": "Aventureux, optimiste, enthousiaste, imprudent",
        "Capricorne": "Ambitieux, discipliné, prudent, réservé",
        "Verseau": "Original, indépendant, humanitaire, excentrique",
        "Poissons": "Compatissant, intuitif, créatif, émotif",
    }

    traits = traits_personnalite.get(signe, "Traits de personnalité non définis.")
    nombres_chanceux = obtenir_nombres_chanceux(signe)

    messagebox.showinfo(
        f"Traits de personnalité - {signe}",
        f"Traits de personnalité pour le signe {signe} en date du {jour}/{mois}/{annee} :\n{traits}\n\nNombres chanceux : {nombres_chanceux}",
    )


# Fonction pour afficher le bilan des entrées utilisateur
# F string : https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
def afficher_bilan():
    bilan = f"Bilan des entrées :\n\n"
    for entry in entrees_utilisateur:
        bilan += f"{entry}\n\n"
    messagebox.showinfo("Bilan des entrées", bilan)


# Fonction pour afficher les traits de personnalité à partir des entrées utilisateur
def afficher_traits_personnalite_from_entry():
    jour = entJour.get()
    mois = entMois.get()
    annee = entAnnee.get()

    if (
        not est_nombre(jour)
        or not est_nombre(mois)
        or not est_annee_valide(annee)
        or not est_jour_valide(jour)
        or not est_mois_valide(mois)
    ):
        messagebox.showerror(
            "Erreur",
            "Veuillez entrer des nombres valides pour le jour, le mois et l'année (entre 1900 et 2023), avec un jour entre 1 et 31 et un mois entre 1 et 12.",
        )
        return

    signe_astrologique = obtenir_signe_astrologique(int(jour), int(mois))
    afficher_traits_personnalite(signe_astrologique, jour, mois, annee)
    entrees_utilisateur.append(
        f"Date de naissance : {jour}/{mois}/{annee}, Signe astrologique : {signe_astrologique}"
    )


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Traits de personnalité par signe astrologique")

# Style de la fenêtre principale
style = ttk.Style()
style.configure("TLabel", padding=6, font=("Helvetica", 12), foreground="#333333")
style.configure(
    "TButton",
    padding=6,
    font=("Helvetica", 12),
    background="#4CAF50",
    foreground="#FFFFFF",
)
style.configure("TEntry", padding=6, font=("Helvetica", 12), width=10)

# Création des widgets

# Label Jour de naissance
lblJour = ttk.Label(fenetre, text="Jour de naissance:")
# Label Mois de naissance
lblMois = ttk.Label(fenetre, text="Mois de naissance:")
# Label Année de naissance
lblAnnee = ttk.Label(fenetre, text="Année de naissance:")

# Entrée pour les labels
entJour = ttk.Entry(fenetre)
entMois = ttk.Entry(fenetre)
entAnnee = ttk.Entry(fenetre)

btnTraitsPersonnalite = ttk.Button(
    fenetre,
    text="Afficher les traits de personnalité",
    command=afficher_traits_personnalite_from_entry,
)
btnBilan = ttk.Button(fenetre, text="Afficher le bilan", command=afficher_bilan)

# Image horoscope
fichierImage = "horo.gif"
img = tk.PhotoImage(file=fichierImage)
lblImage = ttk.Label(fenetre, image=img)
petit_image = img.subsample(1, 2)
lblImage = ttk.Label(fenetre, image=petit_image)

# Liste pour stocker les entrées de l'utilisateur
entrees_utilisateur = []

# Placement des widgets dans la fenêtre
lblJour.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entJour.grid(row=0, column=1, padx=10, pady=10)

lblMois.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entMois.grid(row=1, column=1, padx=10, pady=10)

lblAnnee.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entAnnee.grid(row=2, column=1, padx=10, pady=10)

# Ajout de l'image à la fenêtre
lblImage.grid(row=5, column=0, columnspan=2, pady=10)

#  Style pour l'état de survol
# .map() https://www.w3schools.com/python/ref_func_map.asp
style.map(
    "TButton", background=[("active", "#068a06")], foreground=[("active", "#FFFFFF")]
)

# Styles pour les boutons spécifiques
style_traits_personnalite = ttk.Style()
style_traits_personnalite.configure(
    "TraitsPersonnalite.TButton", background="#07ad07", foreground="#FFFFFF"
)
style_bilan = ttk.Style()
style_bilan.configure("Bilan.TButton", background="#07ad07", foreground="#FFFFFF")

# Bouton pour afficher un trait de personnalité au hasard
btnTraitsPersonnalite = ttk.Button(
    fenetre,
    text="Afficher les traits de personnalité",
    command=afficher_traits_personnalite_from_entry,
    style="TraitsPersonnalite.TButton",
)
btnBilan = ttk.Button(
    fenetre, text="Afficher le bilan", command=afficher_bilan, style="Bilan.TButton"
)

btnTraitsPersonnalite.grid(row=3, column=0, columnspan=2, pady=10)
btnBilan.grid(row=4, column=0, columnspan=2, pady=10)

# traits de personnalité en un dictionnaire
traits_personnalite = {
    "Bélier": "Aventureux, énergique, confiant, impulsif",
    "Taureau": "Patient, déterminé, fiable, têtu",
    "Gémeaux": "Adaptable, intelligent, sociable, indécis",
    "Cancer": "Nurturant, sensible, protecteur, lunatique",
    "Lion": "Charismatique, généreux, passionné, autoritaire",
    "Vierge": "Analytique, fiable, modeste, préoccupé par les détails",
    "Balance": "Sociable, équilibré, charmeur, indécis",
    "Scorpion": "Passionné, déterminé, mystérieux, intense",
    "Sagittaire": "Aventureux, optimiste, enthousiaste, imprudent",
    "Capricorne": "Ambitieux, discipliné, prudent, réservé",
    "Verseau": "Original, indépendant, humanitaire, excentrique",
    "Poissons": "Compatissant, intuitif, créatif, émotif",
}


# Fonction pour afficher les traits au hasard en utulisant random
def afficher_trait_aleatoire():
    signes_astrologiques = [
        "Bélier",
        "Taureau",
        "Gémeaux",
        "Cancer",
        "Lion",
        "Vierge",
        "Balance",
        "Scorpion",
        "Sagittaire",
        "Capricorne",
        "Verseau",
        "Poissons",
    ]

    signe_aleatoire = random.choice(signes_astrologiques)
    traits = traits_personnalite.get(
        signe_aleatoire, "Traits de personnalité non définis."
    )
    nombres_chanceux = obtenir_nombres_chanceux(signe_aleatoire)

    messagebox.showinfo(
        f"Trait de personnalité aléatoire - {signe_aleatoire}",
        f"Traits de personnalité aléatoires pour le signe {signe_aleatoire} :\n{traits}\n\nNombres chanceux : {nombres_chanceux}",
    )


# Afficher un trait de personnalité au hasard
style_trait_aleatoire = ttk.Style()
style_trait_aleatoire.configure(
    "BtnTraitAleatoire.TButton", background="#07ad07", foreground="#FFFFFF"
)

# Bouton pour afficher un trait de personnalité au hasard
btnTraitAleatoire = ttk.Button(
    fenetre,
    text="Trait de personnalité aléatoire",
    command=afficher_trait_aleatoire,
    style="BtnTraitAleatoire.TButton",
)
btnTraitAleatoire.grid(row=5, column=0, columnspan=2, pady=10)

# Boucle principale
fenetre.mainloop()
