import subprocess

def pinger_ips(liste_ips):
    for i, ip in enumerate(liste_ips, start=1):
        commande = ["ping", ip, "-n", "1"]
        resultat = subprocess.run(commande, capture_output=True, text=True)
        statut = resultat.returncode
        
        if statut == 0:
            print(i, ip, "HAUT")
        else:
            print(i, ip, "BAS")

shortlist_ips = ["1.1.1.1", "8.8.8.8", "9.9.9.9"]
pinger_ips(shortlist_ips)