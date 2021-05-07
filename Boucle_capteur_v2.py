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
import sqlite3
# Fonctions
def testCaractere(matriceCouleurs):
    chaineCara = ""
    for x in range(0, 2):
        if(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "0"
        elif(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "1"
        elif(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "2"
        elif(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "3"
        elif(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "4"
        elif(matriceCouleurs[x][0] == "Rouge" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "5"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "6"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "7"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "8"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "9"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "+"
        elif(matriceCouleurs[x][0] == "Blanc" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "-"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "/"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "*"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "**"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "math.cos("
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "math.sin("
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "math.tan("
        elif(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "math.sqrt("
        elif(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Blanc"):
            chaineCara = chaineCara + "("
        elif(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + ")"
        elif(matriceCouleurs[x][0] == "Vert" and matriceCouleurs[x][1] == "Vert"):
            chaineCara = chaineCara + ""


    return(chaineCara)
def testCouleurs(data):
    couleur = ""
    if (data[0] > data[1]*2.5 and data[0] > data[2]*2.5):
        print("La couleur du capteur est rouge !")
        couleur = "Rouge"
    elif (data[0] > 10000 and data[1] < data[0] * 1.1 and data[1] > data[0] * 0.9 and data[2] < data[0] * 1.1 and data[2] > data[0] * 0.9):
        print("La couleur du capteur est blanche !")
        couleur = "Blanc"
    elif (data[0] < 5000 and data[1] < data[0] * 1.5 and data[1] > data[0] * 0.5 and data[2] < data[0] * 1.5 and data[2] > data[0] * 0.5):
        print("La couleur du capteur est noir !")
        couleur = "Noir"
    elif (data[0] > data[2] and data[1] > data[2] and data[2] > 5000 and data[2] < 10000):
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
    elif (data[0] > data[1]*2 and data[0] > data[2]*2 and data[0] < 5000 and data[1] < 5000 and data[2] < 5000):
        print("La couleur du capteur est marron")
        couleur = "Marron"


    return couleur
def verif(liste, liste2, pinBTN1, pinBTN2, pinLED):#pour recuperer le résultat 2e tour
    calculPose = ""
    tabCouleurs = []
    i2c = busio.I2C(board.SCL, board.SDA)
#attente
    while(True):
        tca = adafruit_tca9548a.TCA9548A(i2c)
        GPIO.setup(pinBTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # bouton poussoir 1 Capter + Envoie donnée
        GPIO.setup(pinLED,GPIO.OUT)
        # création des capteurs en tableau avec affectation valeurs utilisable

        dataL = liste[0].lux
        print(dataL)
        if (dataL < 5):
            GPIO.output(pinLED, not GPIO.input(pinLED))  # changement d'état (allumer normalement)

        etat1 = GPIO.input(pinBTN1)  # récupération état du bouton envoie data
        etat2 = GPIO.input(pinBTN2)  # récupération état du bouton exo
        if (etat1 == 0 and etat2 == 1):  # permet de ne pas activer les 2 boutons en même temps
            # fonctionnement du programme de récupération des couleurs (charactère)
            # récupération data et test de la couleurs qui lui est lié
            for x in range(0, 2):
                time.sleep(0.5)  # laisser le temps de se mettre à la lumière
                data = liste[x].color_raw  # récup valeurs capteur multiplexeur 1
                print(data)
                tabCouleurs.append(testCouleurs(data))

            # changement multiplexeur
            tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)

            for x in range(0, 4):
                data1 = liste2[x].color_raw  # récup valeurs capteur multiplexeur 2
                print("data1 = ", data1)
                tabCouleurs.append(testCouleurs(data1))

            # remplissage matrice couleurs

            matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 6, 2)]
            # on fait la range avec le pas que l'on souhaite
            print(matriceCouleurs)
            calculPose += testCaractere(matriceCouleurs)

            return (calculPose)
        else:
            print("attente resultat")
            time.sleep(0.5)
def insert(prenom, nom, calculDonne, calculPose, resultat):
#connection bdd
    conn = sqlite3.connect('testbdd.db')
    curs = conn.cursor()
# insertion
# execution commande
    curs.execute("Insert into eleve (Prenom, Nom, CalculDonne, CalculPose, Resultat) Values(?,?,?,?,?)", (prenom, nom, calculDonne, calculPose, resultat))
    conn.commit()
    curs.close()
    conn.close()

# Programme principal
def main():
#test bdd
    nom = "Pablo"
    prenom = "Emilio"
    calculDonne = "12/6"
    calculPosee = "12/6"

    resultat = ""
    resultatDonne = "2"
    resultatEnvoie = ""
    tour = 0
    juste = 0
    calculPose = ""
    tabCouleurs = []
    liste = []
    liste2 = []
    dataL = 0
    attente = 0
# création instances
    pinBTN1 = 21#recup data led
    pinBTN2 = 23#demande exo
    pinBTN3 = 17#oui (true)
    pinBTN4 = 27#non (false)
    pinLED = 16#manip led
    etat3 = 0
    etat4 = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinBTN1, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 1 Capter + Envoie donnée
    GPIO.setup(pinBTN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 2 Exo
    GPIO.setup(pinLED, GPIO.OUT)#manip led
    GPIO.setup(pinBTN3, GPIO.IN, pull_up_down = GPIO.PUD_UP)#Bouton True
    GPIO.setup(pinBTN4, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton False

    while True:#programme continue
        while True:# attente
            GPIO.output(pinLED, False)#led eteinte
            i2c = busio.I2C(board.SCL, board.SDA)
            tca = adafruit_tca9548a.TCA9548A(i2c)

            #création des capteurs en tableau avec affectation valeurs utilisable
            if(tour == 0):#si c'est le premier tour on déclarre
                for x in range(0, 2):
                    liste.append(adafruit_tcs34725.TCS34725(tca[x]))
                    liste[x].gain = 16
                    liste[x].integration_time = 200
                tour += 1 # tour = nb capteurs penser à changer

            dataL = liste[0].lux
            if(dataL < 5):
                GPIO.output(pinLED, not GPIO.input(pinLED))  # changement d'état (allumer normalement)

            etat1 = GPIO.input(pinBTN1)#récupération état du bouton envoie data
            etat2 = GPIO.input(pinBTN2)#récupération état du bouton exo
            etat3 = GPIO.input(pinBTN3)
            etat4 = GPIO.input(pinBTN4)
            if(etat1 == 0 and etat2 == 1):#permet de ne pas activer les 2 boutons en même temps
                # fonctionnement du programme de récupération des couleurs (charactère)
                # récupération data et test de la couleurs qui lui est lié
                for x in range(0, 2):
                    time.sleep(0.5)#laisser le temps de se mettre à la lumière
                    data = liste[x].color_raw #récup valeurs capteur multiplexeur 1
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
                    data1 = liste2[x].color_raw #récup valeurs capteur multiplexeur 2
                    print("data1 = ", data1)
                    tabCouleurs.append(testCouleurs(data1))

                # remplissage matrice couleurs

                matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 6, 2)]
                # on fait la range avec le pas que l'on souhaite
                print(matriceCouleurs)
                calculPose += testCaractere(matriceCouleurs)
#calcul
                print(tabCouleurs)
                resultat = eval(calculPose)

                if(resultat == eval(calculDonne) and juste == 0):
                    juste += 1 #si un calcul est juste on peut pas revenir ici
                    print("Pose le resultat maintenant !")
                    resultatEnvoie = verif(liste, liste2, pinBTN1, pinBTN2, pinLED)#resultat pose par l'éléeve
                    if(resultatEnvoie == resultatDonne):#resultat donne par l'eleve est juste
                        print("Bien jouer ! Tu as juste !")
                        print(eval(resultatEnvoie))
                        print(eval(calculPosee))
# envoie du calcul à la fin
                        insert(prenom, nom, calculDonne, calculPose, resultatEnvoie)
                        break
                    else:
                        print("Faux, veux tu reposer le resultat ?")
                        insert(prenom, nom, calculDonne, calculPose, resultatEnvoie)
                        print(resultatEnvoie)
                        print(calculPosee)
                        while(True):
                            etat3 = GPIO.input(pinBTN3)
                            etat4 = GPIO.input(pinBTN4)
                            if(etat3 == 0 or etat4 == 0):
                                break
                        if (etat3 == 0 and etat4 == 1):  # si appuyer sur btn3 = oui
                            print("Tu recommence")
                            print("retry")
                            break  # on remonte juste avec l'exercice en cours
                        if (etat4 == 0 and etat3 == 1):  # si appuyer sur BTN4 = non
                            print("Tu abandonnes")
                            print("echec !")
                            break  # fin exercice et en redemander un (peut etre demander avant de remonter)
                else:
                    print("calcul mal poser")
                    print("Veux tu recommencer l'exercice ?")#bouton Oui et Non
                    etat3 = input(GPIO.input(pinBTN3))
                    etat4 = input(GPIO.input(pinBTN4))
                    if(etat3 == 0 and etat4 == 1):#si appuyer sur btn3 = oui
                        print("retry")
                        break#on remonte juste avec l'exercice en cours
                    if(etat4 == 0 and etat3 == 1):#si appuyer sur BTN4 = non
                        print("echec !")
                        break#fin exercice et en redemander un (peut etre demander avant de remonter)
                break

            elif(etat2 == 0 and etat1 == 1):
                print("demande exo")
                break
            elif(etat3 == 0 and etat4 == 1 and etat1 == 1 and etat2 == 1):
                exit()
                break
            else:
                print("attente")

            time.sleep(0.5)
            tabCouleurs = [] #remise à zero du tableau
            juste = 0


    print("end")


#test récup multiple

if __name__ == '__main__':
    main()
    # Fin
