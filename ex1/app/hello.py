"""Mini-quiz interactif pour le TP Docker (exercice 1)."""
import os
import platform
import socket


def poser_question(question, bonne_reponse):
    reponse = input(f"{question} ").strip().lower()
    if reponse == bonne_reponse:
        print("  ✔ Bonne réponse !")
        return 1
    print(f"  ✘ Mauvaise réponse (attendu : {bonne_reponse})")
    return 0


def main():
    print("=" * 40)
    print("   Mini-quiz Docker")
    print("=" * 40)
    print(f"Environnement        : {os.getenv('APP_ENV', 'dev')}")
    print(f"Conteneur (hostname) : {socket.gethostname()}")
    print(f"Système              : {platform.system()} - Python {platform.python_version()}")
    print()

    nom = input("Quel est votre nom ? ").strip() or "étudiant"
    print(f"Bonjour {nom} !\n")

    score = 0
    score += poser_question("Quelle commande lance un conteneur ? (run/build)", "run")
    score += poser_question("Quelle option garde STDIN ouvert ? (-i/-d)", "-i")
    score += poser_question("Un volume sert à... (persister/compiler) ?", "persister")

    print(f"\nScore : {score}/3")
    if os.getenv("APP_ENV") == "prod":
        print("(mode production : résultats non enregistrés)")


if __name__ == "__main__":
    main()
