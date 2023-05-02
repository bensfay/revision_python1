# retrouvez les mots reservés de python(keywords)
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
a=25
# on ultise pas les keywords comme identifiant
# comme as=25 (  as c'est keyword python)

#123somme=25
#les identifiants ne doivent pas commencer par un nombre
somme123=25
#somme$=25
#un identifiant ne doit pas contenir un caractere special
somme=25

_somme=25
#les identifiants peuvent commencer par un underscore

def maFonction():
    pass