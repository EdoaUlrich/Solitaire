from enum import Enum
import random
import pygame
from pygame.locals import *

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

class Etat(Enum):
    MASQUE = "Masque"
    OUVERT = "Ouvert"

class Carte:
    def __init__(self, couleur, numero, etat):
        self.couleur = couleur
        self.numero = numero
        self.etat = etat
        self.moving = False


class JeuDeCarte:
    def __init__(self): # Initialisation du jeu de 52 cartes
        self.cartes = []
        for couleur in Couleur:
            for numero in Numero:
                carte = Carte(couleur.value,numero.value, Etat.MASQUE)
                self.cartes.append(carte)
        self.melanger()

    def melanger(self): # Melanger de manière alétoire nos cartes
        random.shuffle(self.cartes)

    def print(self):
        for carte in self.cartes:
            print(carte.numero+ " " + carte.couleur)

class Img_carte:
    def __init__(self, img, rect):
        self.image = img
        self.rect = rect

class Image_cartes:
    img_carte = {
        "1 Pique" : pygame.image.load("./Images/Cartes/As Pique.png"),
        "1 Carreau" : pygame.image.load("./Images/Cartes/As Carreau.png"),
        "1 Coeur" : pygame.image.load("./Images/Cartes/As Coeur.png"),
        "1 Trefle" : pygame.image.load("./Images/Cartes/As Trefle.png"),
        "2 Pique" : pygame.image.load("./Images/Cartes/2 Pique 1.png"),
        "2 Carreau" : pygame.image.load("./Images/Cartes/2 Carreau 1.png"),
        "2 Coeur" : pygame.image.load("./Images/Cartes/2 Coeur 1.png"),
        "2 Trefle" : pygame.image.load("./Images/Cartes/2 Trefle.png"),
        "3 Pique" : pygame.image.load("./Images/Cartes/3 Pique.png"),
        "3 Carreau" : pygame.image.load("./Images/Cartes/3 Carreau.png"),
        "3 Coeur" : pygame.image.load("./Images/Cartes/3 Coeur.png"),
        "3 Trefle" : pygame.image.load("./Images/Cartes/3 Trefle.png"),
        "4 Pique" : pygame.image.load("./Images/Cartes/4 Pique.png"),
        "4 Carreau" : pygame.image.load("./Images/Cartes/4 Carreau.png"),
        "4 Coeur" : pygame.image.load("./Images/Cartes/4 Coeur.png"),
        "4 Trefle" : pygame.image.load("./Images/Cartes/4 Trefle.png"),
        "5 Pique" : pygame.image.load("./Images/Cartes/5 Pique.png"),
        "5 Carreau" : pygame.image.load("./Images/Cartes/5 Carreau.png"),
        "5 Coeur" : pygame.image.load("./Images/Cartes/5 Coeur.png"),
        "5 Trefle" : pygame.image.load("./Images/Cartes/5 Trefle.png"),
        "6 Pique" : pygame.image.load("./Images/Cartes/6 Pique.png"),
        "6 Carreau" : pygame.image.load("./Images/Cartes/6 Carreau.png"),
        "6 Coeur" : pygame.image.load("./Images/Cartes/6 Coeur.png"),
        "6 Trefle" : pygame.image.load("./Images/Cartes/6 Trefle.png"),
        "7 Pique" : pygame.image.load("./Images/Cartes/7 Pique.png"),
        "7 Carreau" : pygame.image.load("./Images/Cartes/7 Carreau.png"),
        "7 Coeur" : pygame.image.load("./Images/Cartes/7 Coeur.png"),
        "7 Trefle" : pygame.image.load("./Images/Cartes/7 Trefle.png"),
        "8 Pique" : pygame.image.load("./Images/Cartes/8 Pique.png"),
        "8 Carreau" : pygame.image.load("./Images/Cartes/8 Carreau.png"),
        "8 Coeur" : pygame.image.load("./Images/Cartes/8 Coeur.png"),
        "8 Trefle" : pygame.image.load("./Images/Cartes/8 Trefle.png"),
        "9 Pique" : pygame.image.load("./Images/Cartes/9 Pique.png"),
        "9 Carreau" : pygame.image.load("./Images/Cartes/9 Carreau.png"),
        "9 Coeur" : pygame.image.load("./Images/Cartes/9 Coeur.png"),
        "9 Trefle" : pygame.image.load("./Images/Cartes/9 Trefle.png"),
        "10 Pique" : pygame.image.load("./Images/Cartes/10 Pique.png"),
        "10 Carreau" : pygame.image.load("./Images/Cartes/10 Carreau.png"),
        "10 Coeur" : pygame.image.load("./Images/Cartes/10 Coeur.png"),
        "10 Trefle" : pygame.image.load("./Images/Cartes/10 Trefle.png"),
        "11 Pique" : pygame.image.load("./Images/Cartes/Valet Pique.png"),
        "11 Carreau" : pygame.image.load("./Images/Cartes/Valet Carreau.png"),
        "11 Coeur" : pygame.image.load("./Images/Cartes/Valet Coeur.png"),
        "11 Trefle" : pygame.image.load("./Images/Cartes/Valet Trefle.png"),
        "12 Pique" : pygame.image.load("./Images/Cartes/Reine Pique.png"),
        "12 Carreau" : pygame.image.load("./Images/Cartes/Reine Carreau.png"),
        "12 Coeur" : pygame.image.load("./Images/Cartes/Reine Coeur.png"),
        "12 Trefle" : pygame.image.load("./Images/Cartes/Reine Trefle.png"),
        "13 Pique" : pygame.image.load("./Images/Cartes/Roi Pique.png"),
        "13 Carreau" : pygame.image.load("./Images/Cartes/Roi Carreau.png"),
        "13 Coeur" : pygame.image.load("./Images/Cartes/Roi Coeur.png"),
        "13 Trefle" : pygame.image.load("./Images/Cartes/Roi Trefle.png")
        }
    rect_image = {
        "1 Pique" : None,
        "1 Carreau" : None,
        "1 Coeur" : None,
        "1 Trefle" : None,
        "2 Pique" : None,
        "2 Carreau" : None,
        "2 Coeur" : None,
        "2 Trefle" : None,
        "3 Pique" : None,
        "3 Carreau" : None,
        "3 Coeur" : None,
        "3 Trefle" : None,
        "4 Pique" : None,
        "4 Carreau" : None,
        "4 Coeur" : None,
        "4 Trefle" : None,
        "5 Pique" : None,
        "5 Carreau" : None,
        "5 Coeur" : None,
        "5 Trefle" : None,
        "6 Pique" : None,
        "6 Carreau" : None,
        "6 Coeur" : None,
        "6 Trefle" : None,
        "7 Pique" : None,
        "7 Carreau" : None,
        "7 Coeur" : None,
        "7 Trefle" : None,
        "8 Pique" : None,
        "8 Carreau" : None,
        "8 Coeur" : None,
        "8 Trefle" : None,
        "9 Pique" : None,
        "9 Carreau" : None,
        "9 Coeur" : None,
        "9 Trefle" : None,
        "10 Pique" : None,
        "10 Carreau" : None,
        "10 Coeur" : None,
        "10 Trefle" : None,
        "11 Pique" : None,
        "11 Carreau" : None,
        "11 Coeur" : None,
        "11 Trefle" : None,
        "12 Pique" : None,
        "12 Carreau" : None,
        "12 Coeur" : None,
        "12 Trefle" : None,
        "13 Pique" : None,
        "13 Carreau" : None,
        "13 Coeur" : None,
        "13 Trefle" : None,
        }
    moving_image = {
        "1 Pique" : False,
        "1 Carreau" : False,
        "1 Coeur" : False,
        "1 Trefle" : False,
        "2 Pique" : False,
        "2 Carreau" : False,
        "2 Coeur" : False,
        "2 Trefle" : False,
        "3 Pique" : False,
        "3 Carreau" : False,
        "3 Coeur" : False,
        "3 Trefle" : False,
        "4 Pique" : False,
        "4 Carreau" : False,
        "4 Coeur" : False,
        "4 Trefle" : False,
        "5 Pique" : False,
        "5 Carreau" : False,
        "5 Coeur" : False,
        "5 Trefle" : False,
        "6 Pique" : False,
        "6 Carreau" : False,
        "6 Coeur" : False,
        "6 Trefle" : False,
        "7 Pique" : False,
        "7 Carreau" : False,
        "7 Coeur" : False,
        "7 Trefle" : False,
        "8 Pique" : False,
        "8 Carreau" : False,
        "8 Coeur" : False,
        "8 Trefle" : False,
        "9 Pique" : False,
        "9 Carreau" : False,
        "9 Coeur" : False,
        "9 Trefle" : False,
        "10 Pique" : False,
        "10 Carreau" : False,
        "10 Coeur" : False,
        "10 Trefle" : False,
        "11 Pique" : False,
        "11 Carreau" : False,
        "11 Coeur" : False,
        "11 Trefle" : False,
        "12 Pique" : False,
        "12 Carreau" : False,
        "12 Coeur" : False,
        "12 Trefle" : False,
        "13 Pique" : False,
        "13 Carreau" : False,
        "13 Coeur" : False,
        "13 Trefle" : False,
        }

    def __init__(self):
        for cle, valeur in self.img_carte.items():
            self.img_carte[cle] = pygame.transform.scale(self.img_carte[cle],(145,197))
        self.init_rect()

    def init_rect(self):
        for cle, valeur in self.img_carte.items():
            self.rect_image[cle] = self.img_carte[cle].get_rect()
            self.rect_image[cle].center = 145//2, 197//2






