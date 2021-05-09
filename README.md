# P6
Openclassroom Projet 6

OS: Debian9
Python: Python3

Le script est un script en python3 pour automatiser les sauvegardes d'un site wordpress et sa database.


Le fichier Config.yaml nous sert à orchestrer les variables du script.


Le fichier: "main.py" permet de link tout les fichier ensembles est exécuter le script.

Le make_archive: création des sauvegardes en dossier compressé.

Le ssh_func: grâce à l'utilisation du ssh via ce script, il crée une connection entre le site distant et le local pour pouvoir copier les fichiers de sauvegarde sur le serveur distant qui nous sert d'espace de stockage
