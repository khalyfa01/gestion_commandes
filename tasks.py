# tasks.py
from celery import Celery
from app import commandes
from commande import Commande

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task(bind=True, max_retries=3)
def traiter_commande(self, id_commande):
    try:
        commande = next((cmd for cmd in commandes if cmd.id_commande == id_commande), None)
        if commande:
            print(f"Commande {commande.id_commande} traitée. Total: {commande.calculer_total()}")
            commande.marquer_commande_completee()
            # Simuler l'envoi d'un email de confirmation
            print(f"Client notifié pour la commande {commande.id_commande}.")
    except Exception as exc:
        print(f"Erreur lors du traitement de la commande {id_commande}, tentative de réessai.")
        raise self.retry(exc=exc)
