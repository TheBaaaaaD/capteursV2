# coding: UTF-8 
""" 
Script: test_capteur/testCapteur
Création: admin, le 09/03/2021
"""


# Imports 
import adafruit_tcs34725
import adafruit_tca9548a
import RPi.GPIO
import busio
import board
import time
# Fonctions
class tcs: #classe des capteurs
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.c = 0

    def retourValeurs(self):
        return(self.r, self.g, self.b, self.c)
# Programme principal 
def main():
    liste = [4]
# création instance
    filin = open("fichierCouleurs.txt", "w")

    i2c = busio.I2C(board.SCL, board.SDA)
    tca = adafruit_tca9548a.TCA9548A(i2c)

    sensor0 = adafruit_tcs34725.TCS34725(tca[0])
    data0 = sensor0.color_raw
    print(data0)
    # with open("fichierCouleurs.txt", "w") as filout:
        # filout.write(data0)

    sensor1 = adafruit_tcs34725.TCS34725(tca[1])
    data1 = sensor1.color_raw
    print(data1)
    # with open("fichierCouleurs.txt", "w") as filout:
        # filout.write(data1)

    sensor2 = adafruit_tcs34725.TCS34725(tca[2])
    data2 = sensor2.color_raw
    print(data2)
    # with open("fichierCouleurs.txt", "w") as filout:
        # filout.write(data2)

    sensor3 = adafruit_tcs34725.TCS34725(tca[3])
    data3 = sensor3.color_raw
    print(data3)
    # with open("fichierCouleurs.txt", "w") as filout:
        # filout.write(data3)



# 2e partie je déclare les capteurs


# empecher les interruptions
    #tcs.set_interrupt(False)

# lire valeurs RGB
    #r, g, b, c = tcs.get_raw_data()

# afficher valeurs RGB
    #print('Color: Red{0} Green{1} Blue{2} Clear{3}'.format(r, g, b, c))

#test récup multiple


# fin utilisation
    #tcs.set_interrupt(True)
    #tcs.disable()

if __name__ == '__main__':
    main()
    # Fin
