# coding: UTF-8
"""
Script: test_capteur/testCapteur
Création: admin, le 09/03/2021
"""


# Imports
from fonctions_proto import *
# Fonctions
# Programme principal
def main():
# data BDD
    id = 0
    calculDonne = ""
    calculPose = ""
    resultatAbsolu = ""
    resultatPose = ""
    niveau = ""
    identif = []

#variable fonctionnement programme
    donne = False # si false exo donnée par le système
    juste = 0
    case = 0
    coupe = 0
    tabRecup = []
    tabCouleurs = []
    listeCapteurs = []
    dataL = 0
    attente = 0
    taille = 0

# création instances GPIO
    pinBTN1 = 21#recup data led
    pinBTN2 = 24#demande exo
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

    i2c = busio.I2C(board.SCL, board.SDA)
# declaration capteurs
    listeCapteurs = definition_capteurs(i2c, listeCapteurs)

    while True:#programme continue
        while True:# attente
            GPIO.output(pinLED, False)#led eteinte

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
# découpage tableau
                matriceCouleurs = [tabCouleurs[i:i + 2] for i in range(0, 6, 2)]
                identif = identification(matriceCouleurs)
                niveau = identif[0]
                id = identif[1]
                print("id est "+str(id))
                print(type(id))
                print(niveau)

# remise à zéro du tabCouleurs
            tabCouleurs = []

# Fonctionnement normal (récup data)
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
                calculPose = testCaractere(matriceCouleurs)

                print("calcul donné = ")
                print(calculDonne)
# calcul
                print(calculPose)

# si le resultat de ce qu'on a poser vaut le calculDonne et qu'on a pas eu juste avant
                if(calculPose == calculDonne or donne == True):
                    print("Calcul poser juste")
                    print("Pose le resultat maintenant !")
# envoie du calcul à la fin
                    insert_calcul(id, str(calculDonne), str(calculPose), str(resultatAbsolu), str(niveau))
                    # dire résultat

                    resultatPose = resultatPoses(pinBTN1, pinBTN2, pinLED, i2c, listeCapteurs)#resultat pose par l'éléeve

                    if(resultatPose == resultatAbsolu):#resultat donne par l'eleve est juste
                        print("Bien jouer ! Tu as juste !")
                        print(resultatPose)
# envoie du resultat posé
                        insert_resultat(id, str(calculDonne), str(calculPose), str(resultatAbsolu), str(resultatPose), str(niveau))
                        break
                    else:
                        print("Faux, veux tu reposer le resultat ?")
# envoie du resultat posé
                        insert_resultat(id, str(calculDonne), str(calculPose), str(resultatAbsolu), str(resultatPose), str(niveau))
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
                    insert_calcul(id, str(calculDonne), str(calculPose), str(resultatAbsolu), str(niveau))
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
            elif(etat2 == 0 and etat1 == 1):
                print("demande exo")
                time.sleep(2)
                tabRecup = recuperer_exercices(niveau, case)
                case = tabRecup[1]  # dernière case
                calculDonne = str(tabRecup[0])
                resultatAbsolu = recuperer_resultat(niveau, case)
                print(resultatAbsolu)
                break
# si btn3 on arrete le programme
            elif(etat3 == 0 and etat4 == 1 and etat1 == 1 and etat2 == 1 and etat5 == 1):
                exit()
                break
            elif(etat4 == 0 and etat3 == 1):
                donne = True
            else:
                print("attente")

            time.sleep(0.5)
            tabCouleurs = [] #remise à zero du tableau
            juste = 0 #remise à zéro

if __name__ == '__main__':
    main()
    # Fin
