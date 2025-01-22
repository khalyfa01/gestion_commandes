# app.py
# API Flask
from flask import Flask, jsonify, request
from commande import Commande
from tasks import traiter_commande

app = Flask(__name__)

commandes = []

@app.route('/commandes', methods=['POST'])
def ajouter_commande():
    data = request.get_json()
    commande = Commande(data['id_commande'], data['produit'], data['quantite'], data['prix_unitaire'])
    commandes.append(commande)
    traiter_commande.delay(commande.id_commande)  # Envoi à Celery pour traitement
    return jsonify({'message': 'Commande ajoutée et en traitement', 'id_commande': commande.id_commande}), 201

@app.route('/commandes', methods=['GET'])
def lister_commandes():
    return jsonify([commande.__dict__ for commande in commandes])

if __name__ == '__main__':
    app.run(debug=True)
