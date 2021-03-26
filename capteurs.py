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
# Fonctions
def testCaractere(matriceCouleurs):
    chaineCara = ""
    for x in range(1):
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
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Orange"):
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
        if(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Orange"):
            chaineCara = chaineCara + "-"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "/"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "*"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "^"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "cos"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "sin"
        if(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Orange"):
            chaineCara = chaineCara + "tan"
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "sqrt"
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "("
        if(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + ")"

    return(chaineCara)
def testCouleurs(data):
    couleur = ""
    if (data[0] > 15000 and data[1] < 8000 and data[2] < 8000):
        print("La couleur du capteur est rouge !")
        couleur = "Rouge"
    elif (data[0] > 16000 and data[1] > 16000 and data[2] > 16000):
        print("La couleur du capteur est blanche !")
        couleur = "Blanc"
    elif (data[0] < 8000 and data[1] < 8000 and data[2] < 8000):
        print("La couleur du capteur est noir !")
        couleur = "Noir"
    elif (data[0] > 18000 and data[1] > 13000 and data[2] < 15000):
        print("La couleur du capteur est jaune !")
        couleur = "Jaune"
    elif (data[2] > data[0] and data[2] > data[1]):
        print("La couleur du capteur est bleu !")
        couleur = "Bleu"
    elif (data[0] > 15000 and data[1] < 8000 and data[2] < 8000):
        print("La couleur du capteur est orange")
        couleur = "Orange"

    return couleur
# Programme principal
def main():
    a = 0
    matriceCouleurs = [[]]
    tabCouleurs = []
    liste = []
    liste2 = []
# création instance
    filin = open("fichierCouleurs.txt", "a")

    i2c = busio.I2C(board.SCL, board.SDA)
    tca = adafruit_tca9548a.TCA9548A(i2c, 0x70)
    # erreur viens de l'adresse donner en parametres
    #tca2 = adafruit_tca9548a.TCA9548A(i2c, 0x71)

#création des capteurs en tableau avec affectation valeurs utilisable
    for x in range(0, 4):
        liste.append(adafruit_tcs34725.TCS34725(tca[x]))
        liste[x].gain = 16
        liste[x].integration_time = 200

    print("Chaque capteur possède un gain = 16 et un temps d'intégration = 200ms")
# récupération data et test de la couleurs qui lui est lié
    for x in range(0, 4):
        data = liste[x].color_raw
        dataLux = liste[x].lux
        with open("fichierCouleurs.txt", "a") as filout:
            filout.write("\n"+str(data))
        print("data0 = ", data)
        print("Luminosité0 = ", dataLux)
        tabCouleurs.append(testCouleurs(data))

# changement multiplexeur
    tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)

    for x in range(0, 4):
        liste2.append(adafruit_tcs34725.TCS34725(tca[x]))
        liste2[x].gain = 16
        liste2[x].integration_time = 200

    for x in range(0, 4):
        data2 = liste2[x].color_raw
        dataLux2 = liste2[x].lux
        with open("fichierCouleurs.txt", "a") as filout:
            filout.write("\n" + str(data2))
        print("data1 = ", data2)
        print("Luminosité1 = ", dataLux2)
        tabCouleurs.append(testCouleurs(data2))

    print(tabCouleurs)

    for x in range(4):
        for i in range(2):
            matriceCouleurs[x].append(tabCouleurs[i])

#test récup multiple

if __name__ == '__main__':
    main()
    # Fin
