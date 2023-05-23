"""
comment regrouper les tests
les deux premiers : tests de regression ( @pytest.mark.regression) c"est ca son marqueur
les 3 suivants : tests de charge (@pytest.mark.charge)
le dernier : on va pas realiser ce test on va le skiper (@pytest.mark.skip)

tres important :

faut enregistrer les marqueur s dans un fichier " pytest.ini"
avant l'execution  , voir la demarche en bas




dans le terminal :

pour tester toutes les fonctions qui ont un marqueur : charge
 pytest test_SiziemeTest.py -s -v -m charge

 pour tester toutes les methodes sauf les methodes qui ont un marqueur : charge
  pytest test_SiziemeTest.py -s -v -m "not charge"



"""
import pytest





# les fonctions a tetser sont : test_login , test_creerCompte

#@pytest.mark.regression  : permet de creer un marqueur et nommer le test comme de regrression
#le probleme c est que pytest ne connait pas ces marqueurs : regression , charge
# ce qu'on doit faire , on doit creer un fichier "pytest.ini" dans dans notre dossier "jour4" pour
# enregistrer ces marqueurs (regression et charge ) dans "pytest.ini
# comme ca si on execute on aura pas de probleme parceque les markeurs sont enregistrées (ces marqueurs c est nous qui les a créés )
#faut respecter le gabarit pour enregistrer les marqueurs dans pytest.ini
@pytest.mark.regression
def test_login():
    # print("ouvrir le navigateur : ")
    print("se connecter sur google : ")
    # print("fermer le navigateur : ")

#@pytest.mark.regression  : permet de creer un marqueur et nommer le test comme de regrression
@pytest.mark.regression
def test_creerCompte():
    #  print("ouvrir le navigateur : ")
    print("creer un compte google  : ")
    # print("fermer le navigateur : ")

#@pytest.mark.charge  : permet de creer un marqueur et nommer le test comme de charge
@pytest.mark.charge
def test_renitionaliser():
    #  print("ouvrir le navigateur : ")
    print("renitialiser mot de passe  : ")
    # print("fermer le navigateur : ")

#@pytest.mark.regression  : permet de creer un marqueur et nommer le test comme de charge
@pytest.mark.charge
def test_quatre():
    # print("ouvrir le navigateur : ")
    print("quatrieme test : ")
    # print("fermer le navigateur : ")

#@pytest.mark.regression  : permet de creer un marqueur et nommer le test comme de charge
@pytest.mark.charge
def test_cinq():
    #  print("ouvrir le navigateur : ")
    print("cinquieme test : ")
    # print("fermer le navigateur : ")

#@pytest.mark.skip  : permet de creer un marqueur et permet de sauter ce teste cad ne pas le realiser
@pytest.mark.skip
def test_six():
    #  print("ouvrir le navigateur : ")
    print("sixieme test  : ")
    # print("fermer le navigateur : ")