import re

texte = "Contactez-nous à support@exemple.fr pour [info.]"
# Recherche d'un motif d'email
motif = r"\[(.*?)\]"
resultat = re.search(motif, texte)

if resultat:
    print(resultat.group())