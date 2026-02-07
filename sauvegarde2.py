import os
from datetime import datetime
import shutil



profile = os.environ["USERPROFILE"]
source = os.path.join(profile, "Desktop")
destination = os.path.join(profile, "Desktop", "Sauvegarde")

present = datetime.now()
date = present.strftime("%Y-%m-%d_%H-%M-%S")
nom_date = os.path.join(destination, "Sauvegarde_"+date)
creer_dossier = os.makedirs(nom_date, exist_ok=True)

def sauvegarder(source):
    for fichier in os.listdir(source):
        chemin_source = os.path.join(source, fichier)
        chemin_destination = os.path.join(nom_date, fichier)
        if os.path.isfile(chemin_source):
            shutil.copy2(chemin_source, chemin_destination)
            print(f"Fichier copié : {fichier}")

        elif os.path.isdir(chemin_source):
            if not os.path.exists(chemin_destination):
                shutil.copytree(chemin_source, chemin_destination)
                print(f"Dossier copié : {fichier}")
            else:
                print(f"Dossier déjà existant: {fichier}")

sauvegarder(source)

#copie fichiers et dossiers