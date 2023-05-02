a=10
print(type(a))
#systeme numerique : decimal
#on peut representer le systeme numerique en plusieurs formes : decimal , binaire , hexadecimal ,et octal

#representation binaire
#on commence par 0b  ou 0B pour dire que ce nombre est dans la base binaire
somme=0b01111
total=0B1101
print(somme)
print(total)

#representation octale
#on commence par 0o  ou 0Opour dire que ce nombre est dans la base octale( de 0 a 7)
b=0o1254
print(b)
c=0O1456
print(c)

#representation hexadecimale (de 0 a 9 et de A a F)
d=0xface
print(d)
e=0Xface
print(e)

#conversion de base
#commentaire : conversion binaire
k=25
print(bin(k))
#commentaire : conversion octale
print(oct(k))
#commentaire : conversion hexadecimale
print(hex(k))