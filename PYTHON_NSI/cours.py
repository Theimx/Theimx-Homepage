
#Exo I : 
def moyenne_Bac(_note1,_note2,_note3,_note4,_note5,_note6,_note7,_coef1,_coef2,_coef3,_coef4,_coef5,_coef6,_coef7):

    _moyenneG = 0
    _coefG = 0 
    _moyenneG = _moyenneG + _note1 * _coef1
    _coefG += _coef1
    _moyenneG = _moyenneG + _note2 * _coef2 
    _coefG += coef2 
    _moyenneG = _moyenneG + _note3 * _coef3 
    _coefG += coef3 
    _moyenneG = _moyenneG + _note4 * _coef4 
    _coefG += _coef4 
    _moyenneG = _moyenneG + _note5 * _coef5 
    _coefG += _coef5 
    _moyenneG = _moyenneG + _note6 * _coef6 
    _coefG += _coef6
    _moyenneG = _moyenneG + _note7 * _coef7
    _coefG += _coef7

    Bac = _moyenneG /_coefG

    return Bac

def moyenne_math2(note1,note2,note3,note4,note5):
    _math = (((note1+note2+note3) / 3) + ((note4+note4+note5+note5)) / 4) /2

    return _math

def TVA(prix,tva):
    _newPrice = float(prix) * (1 +tva/100)

    return _newPrice

print(moyenne_math2(20,20,20,0,0))
print(TVA(10,20))
Bac = 22


if Bac <= 7.99:
    print("Refusé")
elif Bac >= 8 and Bac <= 9.99 : 
    print("Ratrapage")
elif Bac >= 10 and Bac <= 11.99:
    print("Bac sans mention")
elif Bac >= 12 and Bac <= 13.99:
    print("Mention Assez bien")
elif Bac >= 14 and Bac <= 15.99:
    print("Bien ")
elif Bac >= 16 and Bac <= 17.99:
    print("Très bien")
elif Bac >= 18 and Bac <= 21:
    print("Felicitation")

else : 
    print("non")

#Exo II : 

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
    
#Exo III: 
