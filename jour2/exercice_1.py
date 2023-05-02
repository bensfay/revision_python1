#ecrire un programme qui trouve le plus grand nombre en utilisant un prompt
nombre1=int(input("donnez le premier nombre"))
nombre2=int(input("donnez le deuxieme nombre"))

if (nombre1>nombre2):
    max=nombre1
    print("le max est :"+str(max))
elif (nombre2>nombre1):
    max=nombre2
    print("le max est :" + str(max))
else :
    print("les deux nombre sont egaux ")

