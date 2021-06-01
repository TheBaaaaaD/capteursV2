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
    for x in range(0, 3):
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
            chaineCara = chaineCara + "×"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Noir"):
            chaineCara = chaineCara + "□"
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "cos("
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Bleu"):
            chaineCara = chaineCara + "sin("
        elif(matriceCouleurs[x][0] == "Noir" and matriceCouleurs[x][1] == "Marron"):
            chaineCara = chaineCara + "tan("
        elif(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Rouge"):
            chaineCara = chaineCara + "√("
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
def resultatPoses(pinBTN1, pinBTN2, pinLED, i2c, listeCapteurs):#pour recuperer le résultat 2e tour
    calculPose = ""
    dataL = 0
    tabCouleurs = []
#attente
    while(True):
        GPIO.setup(pinBTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # bouton poussoir 1 Capter + Envoie donnée
        GPIO.setup(pinLED,GPIO.OUT)
        # création des capteurs en tableau avec affectation valeurs utilisable

        etat1 = GPIO.input(pinBTN1)  # récupération état du bouton envoie data
        etat2 = GPIO.input(pinBTN2)  # récupération état du bouton exo
        if (etat1 == 0 and etat2 == 1):  # permet de ne pas activer les 2 boutons en même temps
            if (dataL < 5):
                GPIO.output(pinLED, not GPIO.input(pinLED))  # changement d'état (allumer normalement)

            # fonctionnement du programme de récupération des couleurs (charactère)
            tabCouleurs = lecture_capteurs(listeCapteurs, tabCouleurs, i2c)

            # remplissage matrice couleurs
            matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 6, 2)]
            # on fait la range avec le pas que l'on souhaite
            print(matriceCouleurs)
            calculPose += testCaractere(matriceCouleurs)

            return (calculPose)
        else:
            print("attente resultat")
            time.sleep(0.5)
def insert_calcul(nom, prenom, calculDonne, calculPose, resultatAbsolu, niveau):
#connection bdd
    conn = sqlite3.connect('Sessions.db')
    curs = conn.cursor()
# insertion
# execution commande
    curs.execute("Insert into eleve (nom, prenom, calculDonne, calculPose, resultatAbsolu, niveau) Values(?, ?, ?, ?, ?, ?)",
                 (nom, prenom, calculDonne, calculPose, resultatAbsolu, niveau))
    conn.commit()
    curs.close()
    conn.close()
def insert_resultat(nom, prenom, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau):
#connection bdd
    conn = sqlite3.connect('Sessions.db')
    curs = conn.cursor()
# insertion
# execution commande
    curs.execute("Insert into eleve (nom, prenom, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau) Values(?, ?, ?, ?, ?, ?, ?)",
                 (nom, prenom, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau))
    conn.commit()
    curs.close()
    conn.close()
def definition_capteurs(i2c, listeCapteurs):
# premiere fournée de capteurs
    for x in range(0, 6):
        if(x < 2):#0 et 1 affecter au tca 2
            tca = adafruit_tca9548a.TCA9548A(i2c, 0x70)
            listeCapteurs.append(adafruit_tcs34725.TCS34725(tca[x]))
            listeCapteurs[x].gain = 16
            listeCapteurs[x].integration_time = 200
        else:# les autres sont affecter avec le deuxième multiplexeur
            tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)
            listeCapteurs.append(adafruit_tcs34725.TCS34725(tca[x-2]))
            listeCapteurs[x].gain = 16
            listeCapteurs[x].integration_time = 200

    return listeCapteurs
def lecture_capteurs(listeCapteurs, tabCouleurs, i2c):
    for x in range(0, 6):
        if(x < 2):
            tca = adafruit_tca9548a.TCA9548A(i2c)
            tabCouleurs.append(testCouleurs(listeCapteurs[x].color_raw))
        else:
            tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)
            tabCouleurs.append(testCouleurs(listeCapteurs[x].color_raw))

    return tabCouleurs

# Programme principal
def main():
# data BDD
    nom = "Pablo"
    prenom = "Emilio"
    calculDonne = "0+0"
    calculPose = ""
    resultatAbsolu = "0"
    resultatPose = ""
    niveau = 0

#variable fonctionnement programme
    juste = 0
    tabCouleurs = []
    listeCapteurs = []
    dataL = 0
    attente = 0

# création instances GPIO
    pinBTN1 = 21#recup data led
    pinBTN2 = 23#demande exo
    pinBTN3 = 17#oui (true)
    pinBTN4 = 27#non (false)
    pinBTN5 = 18#ré-entendre dernière data
    pinLED = 16#manip led

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinBTN1, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 1 Capter + Envoie donnée
    GPIO.setup(pinBTN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton poussoir 2 Exo
    GPIO.setup(pinLED, GPIO.OUT)#manip led
    GPIO.setup(pinBTN3, GPIO.IN, pull_up_down = GPIO.PUD_UP)#Bouton True
    GPIO.setup(pinBTN4, GPIO.IN, pull_up_down = GPIO.PUD_UP)#bouton False
    GPIO.setup(pinBTN5, GPIO.IN, pull_up_down = GPIO.PUD_UP)#Bouton de fin de programme

    while True:#programme continue
        while True:# attente
            GPIO.output(pinLED, False)#led eteinte
            i2c = busio.I2C(board.SCL, board.SDA)
# declaration capteurs
            listeCapteurs = definition_capteurs(i2c, listeCapteurs)

#Récupération etat bouton pour savoir ce qu'on fait
            etat1 = GPIO.input(pinBTN1)#récupération état du bouton envoie data
            etat2 = GPIO.input(pinBTN2)#récupération état du bouton exo
            etat3 = GPIO.input(pinBTN3)#stop programme hors exo sinon retry
            etat4 = GPIO.input(pinBTN4)#stop programme hors exo sino retry
            etat5 = GPIO.input(pinBTN5)#identification

# Identification
            if(etat5 == 0 and etat1 == 1 and etat2 == 1 and etat3 == 1 and etat4 == 1):
                dataL = listeCapteurs[0].lux
                if(dataL < 5):
                    GPIO.output(pinLED, not GPIO.input(pinLED))
# récup couleurs pour identification
                tabCouleurs = lecture_capteurs(listeCapteurs, tabCouleurs, i2c)


# remise à zéro du tabCouleurs
            tabCouleurs = []

#Fonctionnement normal (récup data)
            if(etat1 == 0 and etat2 == 1 and etat3 == 1 and etat4 == 1 and etat5 == 1):#permet de ne pas activer les 2 boutons en même temps
                dataL = listeCapteurs[0].lux
                if (dataL < 5):
                    GPIO.output(pinLED, not GPIO.input(pinLED))  # changement d'état (allumer normalement)

                # fonctionnement du programme de récupération des couleurs (charactère)
                # récupération data et test de la couleurs qui lui est lié
                time.sleep(0.5)
                tabCouleurs = lecture_capteurs(listeCapteurs, tabCouleurs, i2c)

                GPIO.output(pinLED, not GPIO.input(pinLED))# extinction des leds pour poser le résultat ou reposer le calcul
# remplissage matrice couleurs
                matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 6, 2)]
# remise à zéro du tabCouleurs
                print(tabCouleurs)
# remise à zéro du calculPose
                calculPose = ""
                tabCouleurs = []
# remplissage calcul posé
                calculPose += testCaractere(matriceCouleurs)
# calcul
                print(calculPose)

# si le resultat de ce qu'on a poser vaut le calculDonne et qu'on a pas eu juste avant
                if(calculPose == calculDonne):
                    juste += 1 #si un calcul est juste on peut pas revenir ici
                    print("Calcul poser juste")
                    print("Pose le resultat maintenant !")
# envoie du calcul à la fin
                    insert_calcul(nom, prenom, calculDonne, calculPose, resultatAbsolu, niveau)

                    # dire résultat

                    resultatPose = resultatPoses(pinBTN1, pinBTN2, pinLED, i2c, listeCapteurs)#resultat pose par l'éléeve

                    if(resultatPose == resultatAbsolu):#resultat donne par l'eleve est juste
                        print("Bien jouer ! Tu as juste !")
                        print(resultatPose)
# envoie du resultat posé
                        insert_resultat(nom, prenom, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau)
                        break
                    else:
                        print("Faux, veux tu reposer le resultat ?")
# envoie du resultat posé
                        insert_resultat(nom, prenom, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau)
                        print(resultatPose)
# boucle d'attente
                        while(True):
                            etat3 = GPIO.input(pinBTN3)
                            etat4 = GPIO.input(pinBTN4)
# Si btn 3 ou 4 appuyer on sort de la boucle d'attente
                            if(etat3 == 0 or etat4 == 0):
                                time.sleep(1)
                                break
# si btn3 recommence poser resultat
                        if (etat3 == 0 and etat4 == 1):  # si appuyer sur btn3 = oui
                            print("Tu recommence")
                            print("retry")
                            break  # on remonte juste avec l'exercice en cours
# si btn4 abandon exo
                        elif (etat4 == 0 and etat3 == 1):  # si appuyer sur BTN4 = non
                            print("Tu abandonnes")
                            print("echec !")
                            break  # fin exercice et en redemander un (peut etre demander avant de remonter)
                else:
                    print("calcul mal poser")
# stockage calcul
                    insert_calcul(nom, prenom, calculDonne, calculPose, resultatAbsolu, niveau)
                    print("Veux tu recommencer l'exercice ?")#bouton Oui et Non
# attente de réponse donc boucle
                    while(True):
                        etat3 = GPIO.input(pinBTN3)
                        etat4 = GPIO.input(pinBTN4)
# si appuyer sur btn3 = oui
                        if(etat3 == 0 and etat4 == 1):
                            print("retry")
                            time.sleep(0.5)
                            break#on remonte juste avec l'exercice en cours (sort du while true)
# si appuyer sur BTN4 = non
                        elif(etat4 == 0 and etat3 == 1):
                            print("echec !")
                            time.sleep(0.5)
                            break#fin exercice et en redemander un (peut etre demander avant de remonter)(sort du while true)
                        time.sleep(0.3)
# sort de l'exercice
                break
# si btn2 demande exo bdd
            elif(etat2 == 0 and etat1 == 1 and etat1 == 3 and etat1 == 4 and etat1 == 5):
                print("demande exo")
                break
# si btn3 on arrete le programme
            elif(etat3 == 0 and etat4 == 1 and etat1 == 1 and etat2 == 1 and etat5 == 1):
                exit()
                break
            else:
                print("attente")

            time.sleep(0.5)
            tabCouleurs = [] #remise à zero du tableau
            juste = 0 #remise à zéro

if __name__ == '__main__':
    main()
    # Fin
