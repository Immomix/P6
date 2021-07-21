# P6
Openclassroom Projet 6

#Definition du Script:
Script pour création et application de backup pour un serveur wordpress et sa database.

#Pré-requis:
2 Serveur sous debian 9
Python3
le ssh d'installez sur les 2 server.
wordpress et maria-db sur le server (local).


#Utilisation:
Telecharger le script sur le serveur local.
configuration du config.yaml pour le ssh.

#Config.yaml
Ce fichier est le coeur du script il contient la totalité des variable utilisé dans le script.

#Fonctionnement:
Comment executer le script?:
1ere option: Uniquement effectuer une création de backup
être dans le répertoire courant où se situe le script et executer la commande "Python3 main.py config.yaml"

2eme option: Effectuer une restoration d'un backup crée ultérieurement:
Choisir la date du backup à appliquer (modifiable dans le config.yaml).
Effectuer la commande dans le répertoire courant: Python3 main.py config.yaml restore


#Attention:
Ce script gère uniquement les backups crée par celui-ci.
pensez à bien modifiez le config.yaml pour rendre le script fonctionnel sur votre serveur.


#Auteur:
Xavier Richard
