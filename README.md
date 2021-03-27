# P6
Openclassroom Projet 6

Le script est un script en python3 pour automatisé les sauvegarde
d'un site wordpress et sa database.

Le fichier Config.yaml nous sert à orchestré les variable du script.



Le script en lui même est séparer en 3 fichier bien disctint:

Le main: Le coeur/cerveau du script

Le make_archive: Creation des sauvegarde en dossier comprésser (site+database)

Le ssh_func: grace à l'utilisation du ssh via ce script il crée une connection entre le site distant et le local.
il copie les fichier de sauvegarde sur le serveur distant qui nous sert d'espace de stockage sécuriser
et il supprime les fichier qui ont dépassez une date donné.
