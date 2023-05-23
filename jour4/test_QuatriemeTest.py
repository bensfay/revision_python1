"""
autre methode qui utilise des annotations au lieu d'utiliser les methodes utiliseés au fichier test_DeuxiemeTest.py :

def setup_function(function):
def teardown_function(function):
def setup_module(module):
def teardown_module(module):


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



@pytest.fixture(scope="module")
def setup():
    print("ouverture de la base de donnée : ")
    yield
    print("fermeture de la base de donnée: ")


@pytest.fixture(scope="function")
def before():
    print("ouvrir le navigateur : ")
    yield
    print("fermer le navigateur : ")

# les fonctions a tetser sont : test_login , test_creerCompte , test_renitialiser
#ici la fonction etait comme ca : def test_login(setup,before) , si on veut l'ecrire sans ces parametres comme ca :
#def test_login() on doit ajouter  @pytest.mark.usefixtures("setup","before") avant chaque fonction a tester

@pytest.mark.usefixtures("setup","before")
def test_login():
    # print("ouvrir le navigateur : ")
    print("se connecter sur google : ")
    # print("fermer le navigateur : ")

@pytest.mark.usefixtures("setup","before")
def test_creerCompte():
    #  print("ouvrir le navigateur : ")
    print("creer un compte google  : ")
    # print("fermer le navigateur : ")

@pytest.mark.usefixtures("setup","before")
def test_renitionaliser():
    #  print("ouvrir le navigateur : ")
    print("renitialiser mot de passe  : ")
    # print("fermer le navigateur : ")