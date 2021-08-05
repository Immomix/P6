# P6
Openclassroom Projet 6

# Définition du Script:
Script pour création et application de backup pour un serveur wordpress et sa database.

## Pré-requis:
2 Serveurs sous debian 9
Python3
le ssh d'installez sur les 2 serveurs.
wordpress et maria-db sur le serveur (local).


## Utilisation:
Télécharger le script sur le serveur local.
configuration du config.yaml pour le ssh.

## Config.yaml
Ce fichier est le coeur du script il contient la totalité des variables utilisé dans le script.
Il est primordial de changer les variable suivante:
"ip_address" (l'ip de votre serveur de sauvegarde distant)
"name" (l'utisalisateur root de votre serveur distant)
"passw" (le mot de pass de l'utilisateur du serveur distant)
"bdd" (le nom de votre database wordpress)
"bdd_user" (l'identifiant de l'utilisateur database wordpress)
"bdd_pass" (le mot de pass de l'utilisateur database wordpress)

## Fonctionnement:
Comment exécuter le script?:
1ere option: Uniquement effectuer une création de backup
être dans le répertoire courant où se situe le script et exécuter la commande "Python3 main.py config.yaml"

2eme option: Effectuer une restauration d'un backup crée ultérieurement:
Choisir la date du backup à appliquer (modifiable dans le config.yaml).
Effectuer la commande dans le répertoire courant: Python3 main.py config.yaml restore


## Code erreur
1 = main.py: le config.yaml est inexistant
2 = main.py: erreur 2eme argument
3 = main.py: erreur 1er argument
4 = make_archive.py: tarfile.CompressionError
5 = make_archive.py: tarfile.tarError
6 = ssh_func.py: erreur fonction connect
7 = ssh_func.py: erreur fonction copy
8 = ssh_func.py: erreur fonction delete
9 = applybackup.py: erreur dans la fonction extract

## Attention:
Ce script gère uniquement les backups crée par celui-ci.
Pensez à bien modifier le config.yaml pour rendre le script fonctionnel sur votre serveur.


### Auteur:
Xavier Richard
