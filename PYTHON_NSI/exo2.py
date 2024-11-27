enceinte = 0
age = int(input("entrez votre age: "))

sexe_femme = input("si vous êtes une femme entrez : oui : ")
if sexe_femme == "oui":
    sexe_femme = True

if sexe_femme == True:
    enceinte = input("si vous êtes enceinte écrivez : oui: ")
if enceinte == "oui":
    enceinte = True


if age <= 17.99 : 
    print("non trop petit")

if sexe_femme == True and enceinte == True:
    print("non pas bon pour le bébé")
if age >= 18 and enceinte != "oui" :
    print("oui c'est bon")
    