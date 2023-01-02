
from Carte import JeuDeCarte
from interface import Interface
from Solitaire import Solitaire
import sys, pygame, ctypes
from pygame.locals import *


if __name__=="__main__":
    Interface()


""" A FAIRE LA PROCHAINE FOIS:
   -servir du dictionnaire moving_image dans la classe Image_cartes pour gerer les deplacement des cartes
   -gerer l'affichage des cartes en reserves ( a piocher) et modifier la focntion test_click_souris dans 
   le fichier Interface.py en ajoutant un test pour un click sur l'image des cartes en reserves.
"""
