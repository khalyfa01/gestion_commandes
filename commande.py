# commande.py
class Commande:
    def __init__(self, id_commande, produit, quantite, prix_unitaire):
        self.id_commande = id_commande
        self.produit = produit
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
        self.status = "en attente"  # Status initial de la commande

    def calculer_total(self):
        return self.quantite * self.prix_unitaire

    def marquer_commande_completee(self):
        self.status = "complétée"
        return self.status
