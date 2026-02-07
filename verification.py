import os
import time


profil = os.environ["USERPROFILE"]
dossier = os.path.join(profil, "Desktop")

def verifier_dossier ():
    fichiers = os.listdir(dossier)
    print(fichiers)

    while True:
        nouveaux_fichiers = os.listdir(dossier)
        time.sleep(2)

        for f in nouveaux_fichiers:
            if f not in fichiers:
                print("nouveau fichiers", f)
        
        for f in fichiers:
            if f not in nouveaux_fichiers:
                print("fichies supprimes", f)
                
        fichiers = nouveaux_fichiers
