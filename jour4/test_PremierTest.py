# 1 : installer "pytest" => pip install pytest
# 2 : creer un fichier python  => doit contenir le mot "test" au debut
# 3 : importer le package "pytest"
#4 : creer des fonctions => elle doivent commencer par "test"
# 5 : pour executer les tests  on doit aller dans le dossier des tests et on execute la commande :
#( pytest test_PremierTest.py -s -v )  s : pour afficher le contenu en forme de caractere  , v: pour afficher

import pytest
# les noms des  fonctions de tests doivent commencer par "test "
def test_login():
    print("se connecter sur google : ")

def test_creerCompte():
    print("creer compte utilisateur google : ")