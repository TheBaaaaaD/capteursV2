# coding: UTF-8 
""" 
Script: test_capteur/testCapteur
Création: admin, le 09/03/2021
"""


# Imports
import adafruit_tcs34725
import adafruit_tca9548a
#import RPi.GPIO
import busio
import board
import time
import math
# Fonctions
def testCaractere(matriceCouleurs):
    chaineCara = ""
    for x in range(0, 2):
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "0"
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "1"
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "2"
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "3"
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "4"
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "5"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "6"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "7"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "8"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "9"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "+"
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "-"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "/"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "*"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "^"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "math"
            print(chaineCara)
            chaineCara = chaineCara + "."
            print(chaineCara)
            chaineCara = chaineCara + "cos"
            print(chaineCara)
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "math.sin("
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "math.tan("
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "math.sqrt("
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "("
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + ")"


    return(chaineCara)
def testCouleurs(data):
    couleur = ""
    if (data[0] > 15500 and data[1] < 8000 and data[2] < 8000):
        print("La couleur du capteur est rouge !")
        couleur = "Rouge"
    elif (data[0] > 16000 and data[1] > 16000 and data[2] > 16000):
        print("La couleur du capteur est blanche !")
        couleur = "Blanc"
    elif (data[0] < 5000 and data[1] < 5000 and data[2] < 5000):
        print("La couleur du capteur est noir !")
        couleur = "Noir"
    elif (data[0] > data[2] and data[1] > data[2]):
        print("La couleur du capteur est Jaune !")
        couleur = "Jaune"
    #elif (data[0] > 18000 and data[1] > 13000 and data[2] < 15000):
        #print("La couleur du capteur est jaune !")
        #couleur = "Jaune"
    elif (data[2] > data[0] and data[2] > data[1]):
        print("La couleur du capteur est bleu !")
        couleur = "Bleu"
    #elif (data[0] > 12500 and data[1] < 9200 and data[2] < 8000):
        #print("La couleur du capteur est orange")
        #couleur = "Orange"
    elif (data[0] > 5500 and data[1] < 5000 and data[2] < 5000):
        print("La couleur du capteur est marron")
        couleur = "Marron"

    return couleur

def testCaractereTest2(tabCouleurs2):
    chaineCara = ""

    if(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Rouge"):
        chaineCara = chaineCara + "0"
    elif(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Blanc"):
        chaineCara = chaineCara + "1"
    elif(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Noir"):
        chaineCara = chaineCara + "2"
    elif(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Jaune"):
        chaineCara = chaineCara + "3"
    elif(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Bleu"):
        chaineCara = chaineCara + "4"
    elif(tabCouleurs2[0] == "Rouge" and tabCouleurs2[1] == "Marron"):
        chaineCara = chaineCara + "5"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Rouge"):
        chaineCara = chaineCara + "6"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Blanc"):
        chaineCara = chaineCara + "7"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Noir"):
        chaineCara = chaineCara + "8"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Jaune"):
        chaineCara = chaineCara + "9"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Bleu"):
        chaineCara = chaineCara + "+"
    elif(tabCouleurs2[0] == "Blanc" and tabCouleurs2[1] == "Marron"):
        chaineCara = chaineCara + "-"
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Rouge"):
        chaineCara = chaineCara + "/"
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Blanc"):
        chaineCara = chaineCara + "*"
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Noir"):
        chaineCara = chaineCara + "^"
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Jaune"):
        chaineCara = chaineCara + "math.cos("
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Bleu"):
        chaineCara = chaineCara + "math.sin("
    elif(tabCouleurs2[0] == "Noir" and tabCouleurs2[1] == "Marron"):
        chaineCara = chaineCara + "math.tan"
    elif(tabCouleurs2[0] == "Jaune" and tabCouleurs2[1] == "Rouge"):
        chaineCara = chaineCara + "math.sqrt("
    elif(tabCouleurs2[0] == "Jaune" and tabCouleurs2[1] == "Blanc"):
        chaineCara = chaineCara + "("
    elif(tabCouleurs2[0] == "Jaune" and tabCouleurs2[1] == "Noir"):
        chaineCara = chaineCara + ")"

    return(chaineCara)
# Programme principal
def main():
    phraseTest = ""
    phrase = ""
    matriceCouleurs = [[]]
    matriceCouleursTest = [["Noir", "Bleu"], ["Rouge", "Marron"], ["Noir", "Noir"], ["Rouge", "Noir"], ["Jaune", "Noir"]]
    tabCouleurs = []
    liste = []
    liste2 = []
# création instance
    filin = open("fichierCouleurs.txt", "a")

    i2c = busio.I2C(board.SCL, board.SDA)
    tca = adafruit_tca9548a.TCA9548A(i2c)
    # erreur viens de l'adresse donner en parametres
    #tca2 = adafruit_tca9548a.TCA9548A(i2c, 0x71)

#création des capteurs en tableau avec affectation valeurs utilisable
    for x in range(0, 2):
        liste.append(adafruit_tcs34725.TCS34725(tca[x]))
        liste[x].gain = 16
        liste[x].integration_time = 200

    print("Chaque capteur possède un gain = 16 et un temps d'intégration = 200ms")
# récupération data et test de la couleurs qui lui est lié
    for x in range(0, 2):
        data = liste[x].color_raw
        dataLux = liste[x].lux
        print("data0 = ", data)
        print("Luminosité0 = ", dataLux)
        tabCouleurs.append(testCouleurs(data))
        with open("fichierCouleurs.txt", "a") as filout:
            filout.write("\n"+str(data)+tabCouleurs[x])

# changement multiplexeur
    tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)

    for x in range(0, 2):
        liste2.append(adafruit_tcs34725.TCS34725(tca[x]))
        liste2[x].gain = 16
        liste2[x].integration_time = 200

    for x in range(0, 2):
        data1 = liste2[x].color_raw
        dataLux1 = liste2[x].lux
        print("data1 = ", data1)
        print("Luminosité1 = ", dataLux1)
        tabCouleurs.append(testCouleurs(data1))
        with open("fichierCouleurs.txt", "a") as filout:
            filout.write("\n" + str(data1) + tabCouleurs[x])

    print(tabCouleurs)
#remplissage matrice couleurs
    matriceCouleurs = [tabCouleurs[i:i+2] for i in range(0, 4, 2)]
# on fait la range avec le pas que l'on souhaite
    print(matriceCouleurs)

    phrase += testCaractere(matriceCouleurs)
    print(phrase)

    for x in range(5):
        tabCouleurs2 = matriceCouleursTest[x]
        phraseTest += testCaractereTest2(tabCouleurs2)

    tabCouleurs2 = matriceCouleursTest[0]
    print(eval(phraseTest))

#test récup multiple

if __name__ == '__main__':
    main()
    # Fin
