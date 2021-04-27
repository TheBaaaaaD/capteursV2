# coding: UTF-8
"""
Script: test_capteur/testCapteur
Création: admin, le 09/03/2021
"""


# Imports
import adafruit_tcs34725
import adafruit_tca9548a
import RPi.GPIO as GPIO
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
        chaineCara = chaineCara + "math.pow("
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
    tour = 0
    phrase = ""
    tabCouleurs = []
    liste = []
    liste2 = []
    dataL = 0
# création instan
    pinBTN1 = 21
    pinBTN2 = 23
    pinLED = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinBTN1, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 1 Capter + Envoie donnée
    GPIO.setup(pinBTN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 2 Exo
    GPIO.setup(pinLED, GPIO.OUT)#manip led

    while True:#programme continue
        while True:# attente
            GPIO.output(pinLED, False)#led eteinte
            i2c = busio.I2C(board.SCL, board.SDA)
            tca = adafruit_tca9548a.TCA9548A(i2c)
            # erreur viens de l'adresse donner en parametres
            #tca2 = adafruit_tca9548a.TCA9548A(i2c, 0x71)

            #création des capteurs en tableau avec affectation valeurs utilisable
            if(tour == 0):#si c'est le premier tour on déclarre
                for x in range(0, 2):
                    liste.append(adafruit_tcs34725.TCS34725(tca[x]))
                    liste[x].gain = 16
                    liste[x].integration_time = 200
                tour += 1 # tour = nb capteurs penser à changer

            dataL = liste[0].lux
            print(dataL)
            if(dataL < 5):
                GPIO.output(pinLED, not GPIO.input(pinLED))  # changement d'état (allumer normalement)

            etat1 = GPIO.input(pinBTN1)#récupération état du bouton envoie data
            etat2 = GPIO.input(pinBTN2)#récupération état du bouton exo
            if(etat1 == 0 and etat2 == 1):#permet de ne pas activer les 2 boutons en même temps
                # fonctionnement du programme de récupération des couleurs (charactère)
                # récupération data et test de la couleurs qui lui est lié
                for x in range(0, 2):
                    time.sleep(0.5)#laisser le temps de se mettre à la lumière
                    data = liste[x].color_raw
                    print(data)
                    tabCouleurs.append(testCouleurs(data))

                # changement multiplexeur
                tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)

                if(tour == 1):#deuxième remplissage (tour = nb capteur avant !)
                    for x in range(0, 4):
                        liste2.append(adafruit_tcs34725.TCS34725(tca[x]))
                        liste2[x].gain = 16
                        liste2[x].integration_time = 200
                    tour += 1

                for x in range(0, 4):
                    data1 = liste2[x].color_raw
                    print("data1 = ", data1)
                    tabCouleurs.append(testCouleurs(data1))
                    print(tabCouleurs)

                # remplissage matrice couleurs

                matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 4, 2)]
                # on fait la range avec le pas que l'on souhaite
                print(matriceCouleurs)
                phrase += testCaractere(matriceCouleurs)
                print(phrase)
                break

            elif(etat2 == 0 and etat1 == 1):
                print("demande exo")
            else:
                print("attente")

            time.sleep(0.5)
            tabCouleurs = [] #remise à zero du tableau


    print("end")


#test récup multiple

if __name__ == '__main__':
    main()
    # Fin
