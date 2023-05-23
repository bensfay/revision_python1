"""
1 : ouverture et fermeture de navigateur se repetent dans chaque test
    a eviter : (dry = don t repeat yourself)
    pour eviter cela : il fau creer deux fonctions (setup_function et teardown_fonction comme des pre_conditions et des
    post_conditions )
    les lignes de code qui se reproduisent on les met dans (setup_function et teardown_function )ou (teardown_module et teardown_module)

"""
import pytest
#important : function s'apllique pour chaque de test et module s'applique pour toute la suite de test
# cette fonction va s executer une fois avant le debut de chaque  cas de test (chaque cas de test va s'executer avec ce setup_function)
def setup_function(function):
    print("ouvrir le navigateur : ")

# cette fonction va s executer une fois  apres la fin  chaque  cas detest( chaque cas de test va s'executer avec ce teardouwn_function)
def teardown_function(function):
    print("fermer le navigateur : ")


#  le module est la suite de test c a d le fichier de test ou nous avons creer nos tests
# les fonction setup_module et teardown_module : s'executent une seule fois apres avoir executer le pytest
# setup_module : s'execute une seule fois au debut de l'execution de notre suite de test
# teardown_module : s'execute une seule fois a la fin de l'exeution de notre suite de test
def setup_module(module):
    print("ouverture de la base de donnée : ")

def teardown_module(module):
    print("fermeture de la base de donnée: ")

# les fonctions a tetser sont : test_login , test_creerCompte
def test_login():
    # print("ouvrir le navigateur : ")
    print("se connecter sur google : ")
    # print("fermer le navigateur : ")

def test_creerCompte():
    #  print("ouvrir le navigateur : ")
    print("creer un compte google  : ")
    # print("fermer le navigateur : ")

