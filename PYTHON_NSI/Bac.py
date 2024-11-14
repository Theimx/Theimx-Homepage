

def moyenne_Bac(note1,note2,note3,note4,note5,note6,note7,coef1,coef2,coef3,coef4,coef5,coef6,coef7):

    moyenneG = 0
    coefG = 0 
    moyenneG = moyenneG + note1 * coef1
    coefG += coef1
    moyenneG = moyenneG + note2 * coef2 
    coefG += coef2 
    moyenneG = moyenneG + note3 * coef3 
    coefG += coef3 
    moyenneG = moyenneG + note4 * coef4 
    coefG += coef4 
    moyenneG = moyenneG + note5 * coef5 
    coefG += coef5 
    moyenneG = moyenneG + note6 * coef6 
    coefG += coef6
    moyenneG = moyenneG + note7 * coef7
    coefG += coef7

    Bac = moyenneG /coefG

    return Bac



Bac =  moyenne_Bac(10,10,10,10,10,10,10,10,10,10,10,10,10,10)

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
elif Bac >= 18:
    print("Felicitation")
else : 
    print("erreur")