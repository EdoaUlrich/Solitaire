from Carte import JeuDeCarte
from enum import Enum
import sys, pygame

# -*- coding: utf-8 -*- 

class Deplacement(Enum):
    INITIAL = "Initial"
    FINAL = "Final"
    RESTE = "Reste"

class Solitaire:
    def __init__(self):
        self.Cartes = JeuDeCarte()
        self.Cartes.melanger()
        self.zone4 = [[],[],[],[]] #Liste representant l'emplacement finale de 4 Colonnes
        self.zone7 = [[],[],[],[],[],[],[]] # Liste representant l'emplacement initial de 7 colonnes

    def partage(self): # fonction permettant de repartir les cartes sur l'emplacement initial
        for num in range(6):
            for z in range(num,6):
                self.zone7[z].append(self.Cartes.cartes[-1])
                del self.Cartes.cartes[-1]
        
    def deplacer(self, place_depart, place_arrivee, pos1, pos2):
        if place_depart == Deplacement.INITIAL: # teste deplacement:
            if place_arrivee == Deplacement.FINAL: #Deplacement: INITIAL -----> FINAL
                if len(place_arrivee[pos2]) > 0: # teste si la liste n'est pas vide
                    if place_arrivee[pos2][-1].couleur == place_depart[pos1][-1].couleur: # Teste si elles ont des signes identiques
                        if place_arrivee[pos2][-1].numero == (place_depart[pos1][-1].numero+1):
                            place_arrivee[pos2].append(place_depart[pos1][-1])
                            del place_depart[pos1][-1]
                            print("Deplacement: INITIAL -----> FINAL : La liste n'etait pas vide")
                        else:
                            print("Deplacement impossible: Numero invalide")
                    else: 
                        print("Deplacement impossible: Couleur differente")
                else: #Si elle est vide
                    if(place_depart[pos1][-1].numero == 1): # Teste si le numero est l'AS
                        place_arrivee[pos2].append(place_depart[pos1][-1])
                        del place_depart[pos1][-1]
                        print("Deplacement: INITIAL -----> FINAL : La liste etait vide")
                    else: 
                        print("Deplacement Impossible: Il faut un AS")
            elif place_arrivee == Deplacement.INITIAL: # deplacement:  INITIAL --------> INITIAL
                if len(place_arrivee[pos1]) > 0: 
                    if place_depart[pos1][-1].couleur == "Carreau" or place_depart[pos1][-1].couleur == "Coeur": #teste Couleur: Rouge
                        if place_arrivee[pos2][-1].couleur == "Pique" or place_arrivee[pos2][-1].couleur == "Trefle":# Rouge -----> Noir
                            if place_depart[pos1][-1].numero < place_arrivee[pos2][-1].numero:
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                    elif place_depart[pos1][-1].couleur == "Pique" or place_depart[pos1][-1].couleur == "Trefle": # teste Couleur Noire
                        if place_arrivee[pos2][-1].couleur == "Carreau" or place_arrivee[pos2][-1].couleur == "Coeur": # Noire ------> Rouge
                            if place_depart[pos1][-1].numero == (place_arrivee[pos2][-1].numero - 1): # Teste si le numero de la carte à ajoute est inferieur au numero de la derniere carte de la destination
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                else:
                    place_arrivee[pos2].append(place_depart[pos1][-1])
                    del place_depart[pos1][-1]
                    print("Deplacement INITIAL -----> INITIAL : La case etait vide")
            else:
                print("Deplacement Impossible")
        elif place_depart == Deplacement.FINAL:
            if place_arrivee == Deplacement.INITIAL:# Deplacement FINAL --------> INITIAL
                if len(place_arrivee[pos1]) > 0: 
                    if place_depart[pos1][-1].couleur == "Carreau" or place_depart[pos1][-1].couleur == "Coeur": #teste Couleur: Rouge
                        if place_arrivee[pos2][-1].couleur == "Pique" or place_arrivee[pos2][-1].couleur == "Trefle":# Rouge -----> Noir
                            if place_depart[pos1][-1].numero < place_arrivee[pos2][-1].numero:
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                    elif place_depart[pos1][-1].couleur == "Pique" or place_depart[pos1][-1].couleur == "Trefle": # teste Couleur Noire
                        if place_arrivee[pos2][-1].couleur == "Carreau" or place_arrivee[pos2][-1].couleur == "Coeur": # Noire ------> Rouge
                            if place_depart[pos1][-1].numero == (place_arrivee[pos2][-1].numero - 1): # Teste si le numero de la carte à ajoute est inferieur au numero de la derniere carte de la destination
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                else:
                    place_arrivee[pos2].append(place_depart[pos1][-1])
                    del place_depart[pos1][-1]
                    print("Deplacement FINAL -----> INITIAL : La case etait vide")
            else:
                print("Deplacement Impossible")
        elif place_depart == Deplacement.RESTE:
            if place_arrivee == Deplacement.FINAL:#Deplacement RESTE -------> FINAL
                if len(place_arrivee[pos2]) > 0: # teste si la liste n'est pas vide
                    if place_arrivee[pos2][-1].couleur == place_depart[pos1][-1].couleur: # Teste si elles ont des signes identiques
                        if place_arrivee[pos2][-1].numero == (place_depart[pos1][-1].numero+1):
                            place_arrivee[pos2].append(place_depart[pos1][-1])
                            del place_depart[pos1][-1]
                            print("Deplacement: INITIAL -----> FINAL : La liste n'etait pas vide")
                        else:
                            print("Deplacement impossible: Numero invalide")
                    else: 
                        print("Deplacement impossible: Couleur differente")
                else: #Si elle est vide
                    if(place_depart[pos1][-1].numero == 1): # Teste si le numero est l'AS
                        place_arrivee[pos2].append(place_depart[pos1][-1])
                        del place_depart[pos1][-1]
                        print("Deplacement: INITIAL -----> FINAL : La liste etait vide")
                    else: 
                        print("Deplacement Impossible: Il faut un AS")
            elif place_arrivee == Deplacement.INITIAL: # Deplacement RESTE ------> INITIAL
                if len(place_arrivee[pos1]) > 0: 
                    if place_depart[pos1][-1].couleur == "Carreau" or place_depart[pos1][-1].couleur == "Coeur": #teste Couleur: Rouge
                        if place_arrivee[pos2][-1].couleur == "Pique" or place_arrivee[pos2][-1].couleur == "Trefle":# Rouge -----> Noir
                            if place_depart[pos1][-1].numero < place_arrivee[pos2][-1].numero:
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                    elif place_depart[pos1][-1].couleur == "Pique" or place_depart[pos1][-1].couleur == "Trefle": # teste Couleur Noire
                        if place_arrivee[pos2][-1].couleur == "Carreau" or place_arrivee[pos2][-1].couleur == "Coeur": # Noire ------> Rouge
                            if place_depart[pos1][-1].numero == (place_arrivee[pos2][-1].numero - 1): # Teste si le numero de la carte à ajoute est inferieur au numero de la derniere carte de la destination
                                place_arrivee[pos2].append(place_depart[pos1][-1])
                                del place_depart[pos1][-1]
                            else:
                                print("Deplacement impossible: Numero Invalide")
                        else:
                            print("Deplacement Impossible: Same Color")
                else:
                    place_arrivee[pos2].append(place_depart[pos1][-1])
                    del place_depart[pos1][-1]
                    print("Deplacement FINAL -----> INITIAL : La case etait vide")
            else:
                print("Deplacement Impossible")
    

    def afficher(self):
        for num in range(6):
            for z in range(len(self.zone7[num])):
                print(f"{self.zone7[num][z].couleur} {self.zone7[num][z].numero}")
            print("\n")

    def endGame(self):
        i = 0
        for num in range(3):
            if self.zone4[num][-1].numero == 13:
                i+=1
        if i == 4:
            return 1
        else:
            return 0





        



        
