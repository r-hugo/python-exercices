import os
import re
import shutil

def supprimer_espace(dossier_source):
    for fichier in os.listdir(dossier_source):
        espace = r"\s+"
        if re.search(espace, fichier):
            fichier_sans_espace = re.sub(espace, "_", fichier)
            source = os.path.join(dossier_source, fichier)
            destination = os.path.join(dossier_source, fichier_sans_espace)
            shutil.move(source, destination)

        print ("Espaces supprimés !")

if __name__ == "__main__":
    dossier = input("Chemin du dossier à nettoyer : ").strip('"')
    if os.path.isdir(dossier):
        supprimer_espace(dossier)
        print("\nNettoyage terminé.")
    else:
        print("Chemin invalide.")

