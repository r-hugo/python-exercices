import os
import shutil

dossier_source = "SOURCE"
dossier_pdf = "PDF"
dossier_doc = "DOC"
dossier_autres = "AUTRES"


def trier_fichiers(dossier_source, dossier_pdf, dossier_doc, dossier_autres):
    if not os.path.isdir(dossier_pdf):
        os.mkdir(dossier_pdf)
    if not os.path.isdir(dossier_doc):
        os.mkdir(dossier_doc)
    if   not os.path.isdir(dossier_autres):
        os.mkdir(dossier_autres)
        for fichier in os.listdir(dossier_source):
            if fichier.endswith(".pdf"):
                source = os.path.join(dossier_source, fichier)
                destination_pdf = os.path.join(dossier_pdf, fichier)
                shutil.move(source, destination_pdf)

            elif fichier.endswith(".doc") or fichier.endswith(".docx"):
                source = os.path.join(dossier_source, fichier)
                destination_doc = os.path.join(dossier_doc, fichier)
                shutil.move(source, destination_doc)

            else:
                source = os.path.join(dossier_source, fichier)
                destination_autres = os.path.join(dossier_autres, fichier)
                shutil.move(source, destination_autres)