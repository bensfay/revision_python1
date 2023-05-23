"""
autre methode au lieu d'utiliser les methodes utiliseés au fichier test_DeuxiemeTest.py :

def setup_function(function):
def teardown_function(function):
def setup_module(module):
def teardown_module(module):

mais ici on les remplace par setup et before


"""
import pytest


# def setup_function(function):
#     print("ouvrir le navigateur : ")
#
# def teardown_function(function):
#     print("fermer le navigateur : ")
#
#
#
# def setup_module(module):
#     print("ouverture de la base de donnée : ")
#
# def teardown_module(module):
#     print("fermeture de la base de donnée: ")

#on ajoute @pytest.fixture(scope="module")  avant la fonction setup() le scope ici c'est module : cad il va ettre appliqué a toute la suite de test
# yield dans la fonction setup() signifie que la fonction setup() executer ces prmieres lignes de codes au debut de l,execution de la suite de test  : dans ce cas :
# print("ouverture de la base de donnée : ") apres elle va attendre la fin de l'exceution de la suite de test grace au yield ,
# et par la fin executer les lignes de codes restants dans la fonction setup()
# dans ces fonction setup et before on peut mettre les post-conditions et les pre-conditions
@pytest.fixture(scope="module")
def setup():
    print("ouverture de la base de donnée : ")
    yield
    print("fermeture de la base de donnée: ")

#on ajoute @pytest.fixture(scope="function") avant la fonction before , le scope ici est function , cad il sera appliqué a chaque cas de test (chaque fonction)
# yield dans la fonction before() signifie que la fonction before() va executer ces prmieres lignes de codes au debut de l,execution de chaque cas de test   : dans ce cas :
#  print("ouvrir le navigateur : ") apres elle va attendre la fin de l'exceution du cas  de test grace au yield ,
# et par la fin executer les lignes de codes restants dans la fonction before()
@pytest.fixture(scope="function")
def before():
    print("ouvrir le navigateur : ")
    yield
    print("fermer le navigateur : ")

# les fonctions a tetser sont : test_login , test_creerCompte
def test_login(setup,before):
    # print("ouvrir le navigateur : ")
    print("se connecter sur google : ")
    # print("fermer le navigateur : ")

def test_creerCompte(setup,before):
    #  print("ouvrir le navigateur : ")
    print("creer un compte google  : ")
    # print("fermer le navigateur : ")

def test_renitionaliser(setup,before):
    #  print("ouvrir le navigateur : ")
    print("renitialiser mot de passe  : ")
    # print("fermer le navigateur : ")