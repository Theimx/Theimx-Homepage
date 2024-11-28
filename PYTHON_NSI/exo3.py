#Exo III: 
print("Exo III")

prix_base = 206000
nb_années = 15
inflations = 1 + (3/100)

for i in range (nb_années):
    print(prix_base * inflations)   
    prix_base = prix_base * inflations

#exo IV : 

def taille_chaine(_chaine):
    return int(len(str(_chaine)))

print(taille_chaine("Tesjhhjbt"))


#exo bonus I

for i in range(101):
    print(i)