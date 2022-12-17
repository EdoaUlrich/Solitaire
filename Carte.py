from enum import Enum
import random

class Couleur(Enum):
    PIQUE = "Pique"
    CARREAU = "Carreau"
    COEUR = "Coeur"
    TREFLE = "Trefle"

class Numero(Enum):
    AS = 1
    DEUX = 2
    TROIS = 3
    QUATRE = 4
    CINQ = 5
    SIX = 6
    SEPT = 7
    HUIT = 8
    NEUF = 9
    DIX = 10
    VALET = 11
    DAME = 12
    ROI = 13

class Carte:
    def __init__(self, couleur, numero):
        self.couleur = couleur
        self.numero = numero

class JeuDeCarte:
    def __init__(self): # Initialisation du jeu de 52 cartes
        self.cartes = []
        for couleur in Couleur:
            for numero in Numero:
                carte = Carte(couleur.value,numero.value)
                self.cartes.append(carte)

    def melanger(self): # Melanger de manière alétoire nos cartes
        random.shuffle(self.cartes)

    def print(self):
        for carte in self.cartes:
            print(carte.numero+ " " + carte.couleur)






