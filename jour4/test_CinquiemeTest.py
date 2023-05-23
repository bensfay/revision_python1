"""
pour tester une seule methode ( login) dans une suite de test , on execute dans le terminal:
pytest test_CinquiemeTest.py -s -v -k login

pour tester toutes les methodes dans une suite de test sans la methode (login) , on execute dans le terminal:
pytest test_CinquiemeTest.py -s -v -k "not login"



"""
import pytest





# les fonctions a tetser sont : test_login , test_creerCompte
def test_login():
    # print("ouvrir le navigateur : ")
    print("se connecter sur google : ")
    # print("fermer le navigateur : ")

def test_creerCompte():
    #  print("ouvrir le navigateur : ")
    print("creer un compte google  : ")
    # print("fermer le navigateur : ")

def test_renitionaliser():
    #  print("ouvrir le navigateur : ")
    print("renitialiser mot de passe  : ")
    # print("fermer le navigateur : ")