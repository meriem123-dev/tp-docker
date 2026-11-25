Q1 : étapes :
 1- le client docker a envoyé une demande au moteur qui gère les conteneurs (daemon)
 2- le daemon a téléchargé l'image depuis Docker hub (registre des images)
 3- le daemon a crée le conteneur à partir de l'image (instanciation) et a exécuté son programme .
 4-le programme a généré un message que Docker a envoyé à mon terminal .

Q2 : -i : pour garder le clavier (entrée standrd) ouvert pour intéragir avec le shell
     -t : crée un terminal virtuel pour intérragir avec le shell 

Q3 : parce que quand on éxecute exit le processus principal s'arrète (le shell) , et donc le conteneur s'arrète .

Q4 : Oui, le fichier existe toujours, car arrêter un conteneur ne supprime pas son système de fichiers.

Q5 : non il n'existe plus car la commande a supprimé l'ancien système de fichiers .

Q6: --rm : supprime auotmatiquement le conteneur quand il s'arrete .

Q7: "IPAddress": "172.17.0.2",
      "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8081"
                    }
                ]
            },

Q8: docker run : crée un conteneur et le démarre .
    docker exec : éxecute une commande dans un conteneur existant .

Q9: Non. Lorsque on arrêtes puis supprime le conteneur, sa couche de mofications est supprimée.

    En recréant un conteneur Nginx à partir de l'image originale, la page d'accueil revient à son contenu initial .

Q10 : Avec -it, nous pouvons interagir avec le programme depuis le terminal, et répondre aux    questions avec input() en Python.

Q11: une image est le modèle utilisé pour créer des conteneurs et ne peux pas etre éxecutée , contrairement à un conteneur qui peut etre démarré ,executé, arreté , supprimé .

