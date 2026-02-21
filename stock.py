
# Mini projet Gestionnaire de Stock v1 – Base Python


#  Stock vide au départ (liste recoi des dictionnaires)
stock = []

#  Ajouter un produit
def ajouter_produit(nom, prix, quantite):
    produit = {
        "nom": nom,
        "prix": prix,
        "quantite": quantite
    }
    stock.append(produit)
    print(f"Produit '{nom}' ajouté avec succès !")

#  Afficher tous les produits
def afficher_stock():
    if not stock:
        print("Le stock est vide.")
        return

    print("\n--- Stock actuel ---")
    for produit in stock:
        print(f'Nom: {produit["nom"]} | Prix: {produit["prix"]} | Quantité: {produit["quantite"]}')
    print("-------------------\n")

#  Supprimer un produit
def supprimer_produit(nom):
    for produit in stock:
        if produit["nom"] == nom:
            stock.remove(produit)
            print("Produit supprimé avec succès")
            return
    print("Produit introuvable")

#  Modifier le prix d’un produit
def modifier_prix(nom, nouveau_prix):
    for produit in stock:
        if produit["nom"] == nom:
            produit["prix"] = nouveau_prix
            print("Prix modifié avec succès")
            return
    print("Produit introuvable")


# Mon Menu interactif

while True:
    choix = input(
        "Que voulez-vous faire ?\n"
        "1 - Ajouter un produit\n"
        "2 - Afficher le stock\n"
        "3 - Supprimer un produit\n"
        "4 - Modifier le prix\n"
        "5 - Quitter\n"
        "Votre choix : "
    )

    if choix == "1":
        nom = input("Nom du produit : ")
        prix = float(input("Prix : "))
        quantite = int(input("Quantité : "))
        ajouter_produit(nom, prix, quantite)

    elif choix == "2":
        afficher_stock()

    elif choix == "3":
        nom = input("Nom du produit à supprimer : ")
        supprimer_produit(nom)

    elif choix == "4":
        nom = input("Nom du produit à modifier : ")
        nouveau_prix = float(input("Nouveau prix : "))
        modifier_prix(nom, nouveau_prix)

    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.")