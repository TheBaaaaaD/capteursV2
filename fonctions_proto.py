# coding: UTF-8 
""" 
Script: test_capteur/fonctions_proto
Création: admin, le 11/06/2021
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
from random import *

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
        elif(matriceCouleurs[x][0] == "Jaune" and matriceCouleurs[x][1] == "Jaune"):
            chaineCara = chaineCara + "π"
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
    elif (data[2] > data[0] and data[2] > data[1]):
        print("La couleur du capteur est bleu !")
        couleur = "Bleu"
    elif (data[0] > data[1]*2 and data[0] > data[2]*2 and data[0] < 5000 and data[1] < 5000 and data[2] < 5000):
        print("La couleur du capteur est marron")
        couleur = "Marron"
    elif (data[1] > data[0] and data[1] > data[2]):
        print("La couleur du capteur est vert")
        couleur = "Vert"

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
def insert_calcul(id, calculDonne, calculPose, resultatAbsolu, niveau):
#connection bdd
    conn = sqlite3.connect('Sessions.db')
    curs = conn.cursor()
# insertion
# execution commande
    curs.execute("Insert into eleve (id, calculDonne, calculPose, resultatAbsolu, niveau) Values(?, ?, ?, ?, ?)",
                 (id, calculDonne, calculPose, resultatAbsolu, niveau))
    conn.commit()
    curs.close()
    conn.close()
def insert_resultat(id, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau):
#connection bdd
    conn = sqlite3.connect('Sessions.db')
    curs = conn.cursor()
# insertion
# execution commande
    curs.execute("Insert into eleve (id, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau) Values(?, ?, ?, ?, ?, ?)",
                 (id, calculDonne, calculPose, resultatAbsolu, resultatPose, niveau))
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
            print(listeCapteurs[x].color_raw)
        else:
            tca = adafruit_tca9548a.TCA9548A(i2c, 0x71)
            tabCouleurs.append(testCouleurs(listeCapteurs[x].color_raw))
            print(listeCapteurs[x].color_raw)

    return tabCouleurs
# fonction pemettant de récuperer les calculs
def recuperer_exercices(niveau, case):

    cnx = sqlite3.connect('Sessions.db' )
    cursor = cnx.cursor()
    recup_exo = "SELECT  calculDonne FROM exercices Where  niveau = ? "
    data = (niveau)
    cursor.execute(recup_exo, data)#execution d'une requête SQL a l'aide de la methode execute()
    result = cursor.fetchall()
    taille = len(result)
    case = randint(0, taille - 1)
    return result[case], case
# fonction pemettant de récuperer les calculs
def recuperer_resultat(niveau, case):
    cnx = sqlite3.connect('Sessions.db') #creation d'un objet-connection a l'aide de la methode connect()
    cursor = cnx.cursor() #creation d'un objet-interface a l'aide de la methode connect()
    recup_result = "SELECT resultatAbsolu FROM exercices Where  niveau = ?  "
    data = (niveau)
    cursor.execute(recup_result, data)
    result = cursor.fetchall()
    return result[case]
def identification(matriceCouleurs):
    # récupération couleurs
    couleurs = matriceCouleurs[0][0]
    couleurs += " "
    couleurs += matriceCouleurs[0][1]

    cnx = sqlite3.connect('Sessions.db')  # creation d'un objet-connection a l'aide de la methode connect()
    cursor = cnx.cursor()  # creation d'un objet-interface a l'aide de la methode connect()
    recup_result = "SELECT niveau, id FROM identification Where couleurs LIKE '"+couleurs+"'"
    cursor.execute(recup_result)
    result = cursor.fetchone()
    return result

def enonceCalculDonne(phrase, calculDonne):
    phrase = "Le calcul que vous devez poser est"
    call(["espeak", "-vfr+13", phrase + calculDonne])

def enonceCalculPose(phrase, calculDonne):
    phrase = "Le calcul que vous avez posé est"
    call(["espeak", "-vfr+13", phrase + calculDonne])

def lireCalcul(calculPose, resultatDonne):  # On lit le calcul posé par l'élève
    if (calculPose == True):
        call(["espeak", "-vfr+13", "Le calcul posé est juste"])
        time.sleep(0.5)
        call(["espeak", "-vfr+13", "Passons au résultat"])
        time.sleep(0.5)
        call(["espeak", "-vfr+13", "Le resultat est" + resultatDonne])
    else:
        call(["espeak", "-vfr+13", "Le calcul posé est incorrect"])
        time.sleep(0.5)
        call(["espeak", "-vfr+13", "Voulez-vous réessayer ?"])
        time.sleep(0.5)

def LireResultat(resultatPose):  # On lit le résultat du calcul
    if (resultatPose == True):
        call(["espeak", "-vfr+13", "-s80", "Le resultat proposé est juste"])
        time.sleep(0.5)
    else:
        call(["espeak", "-vfr+13", "Le résultat proposé est incorrect"])
        time.sleep(0.5)
        call(["espeak", "-vfr+13", "Voulez-vous réessayer ?"])
        time.sleep(0.5)
# Programme principal 
def main():
    pass


if __name__ == '__main__':
    main()
    # Fin
