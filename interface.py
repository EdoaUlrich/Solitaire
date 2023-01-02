import time
from Solitaire import Solitaire
from Carte import Image_cartes, Img_carte, Etat
import pygame
from pygame.locals import *

from Carte import Couleur

class Interface:
    def __init__(self):
        pygame.init()
        self.solitaire = Solitaire()
        self.ecran_long,self.ecran_larg = 1500, 750
        self.images_cartes = Image_cartes()
        self.fenetre = pygame.display.set_mode((self.ecran_long, self.ecran_larg), pygame.RESIZABLE)
        self.image_de_fond_menu = pygame.image.load('Images/bg2.jpg')
        self.actif = 1
        self.zone4 = [0,0,0,0] #Liste representant l'emplacement finale de 4 Colonnes
        self.zone7 = [0,0,0,0,0,0,0] # Liste representant l'emplacement initial de 7 colonnes
        self.zone4_image = [[],[],[],[]] #Liste representant l'emplacement finale de 4 Colonnes
        self.zone7_image = [[],[],[],[],[],[],[]] # Liste representant l'emplacement initial de 7 colonnes
        self.zoneReste = [0,0,0]
        self.zoneReste_image = [[],[],[]]
        self.zonePioche = pygame.image.load('Images/Cartes/images.png')
        self.zonePioche = pygame.transform.scale(self.zonePioche,(145,197))
        while self.actif: 
            self.menu()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.actif = 0
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.actif = 1
            pygame.display.update()
        pygame.quit()

    def menu(self):
        btn_parametres = pygame.image.load("./Images/Cartes/2 Carreau 1.png")
        btn_parametres = pygame.transform.scale(btn_parametres,(145,197))
        rect = btn_parametres.get_rect()
        rect.center = 145//2, 197//2
        rect.topleft = (0,0)
        rectPioche = self.zonePioche.get_rect()
        rectPioche.center = 145//2, 197//2
        rectPioche.topleft = (100.5,50)
        running = True
        moving = False
        while running:
            
            self.image_de_fond_menu = pygame.transform.scale(self.image_de_fond_menu,(self.fenetre.get_width(),self.fenetre.get_height()))    
            self.fenetre.blit(self.image_de_fond_menu,(0,0))
            self.fenetre.blit(self.zonePioche,rectPioche)
            for i in range(len(self.zone4)): #initialisation des emplacements de la zone carte FINALE
                self.zone4[i] = pygame.image.load('Images/Cartes/zone.png')
                self.zone4[i] = pygame.transform.scale(self.zone4[i],(145,187))
            for i in range(len(self.zone7)): #initialisation des emplacements de la zone carte 7
                self.zone7[i] = pygame.image.load('Images/Cartes/zone.png')
                self.zone7[i] = pygame.transform.scale(self.zone7[i],(145,187))
            for i in range(len(self.zone4)): #Afficage des emplacements de la zone FINALE
                if i == 0:
                    self.fenetre.blit(self.zone4[i],(self.ecran_long-100.5-145*(i+1),50))
                else:
                    self.fenetre.blit(self.zone4[i],(self.ecran_long-100.5-145*(i+1)-45*i,50))
            for i in range(len(self.zone7)): #Afficage des emplacements de la zone 7
                if( i == 0):
                    self.fenetre.blit(self.zone7[i],(100.5+145*i,297))
                else:
                    self.fenetre.blit(self.zone7[i],(100.5+145*i+45*i,297))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    self.actif = 0
                elif event.type == MOUSEBUTTONDOWN: # Teste si le bouton de la souris est appuyé
                    for z in range(len(self.images_cartes.rect_image)): #Parcours de toutes les images des cartes affichés.
                        #if self.images_cartes.rect_image[z].collidepoint(event.pos):  #Teste si le click est effectué sur une carte 
                        self.test_click_souris(z) #teste si le click de la souris se fait sur une carte

                    if rect.collidepoint(event.pos):
                        moving = True
                    elif rectPioche.collidepoint(event.pos):
                        moving = True
                elif event.type == MOUSEBUTTONUP:
                    moving = False
                    for cle, valeur in self.images_cartes.moving_image.items():
                        self.images_cartes.moving_image[cle] = False
                elif event.type == MOUSEMOTION and moving:
                    rect.move_ip(event.rel)
            #self.fenetre.blit(btn_parametres,rect) 
            self.afficher_carte()
             # mis à jour de l'ecran

    def afficher_carte(self):
        for i in range(4):
            if len(self.solitaire.zone4[i])>0:
                for j in range(len(self.solitaire.zone4[i])):
                    numero = str(self.solitaire.zone4[i][j].numero)
                    couleur = self.solitaire.zone4[i][j].couleur
                    etat = self.solitaire.zone4[i][j].etat
                    image_carte = Img_carte(self.images_cartes.img_carte[numero + " " + couleur],self.images_cartes.rect_image[numero + " " + couleur])
                    self.zone4_image[i].append(image_carte)
        for i in range(7):
            if len(self.solitaire.zone7[i])>0:
                for j in range(len(self.solitaire.zone7[i])):
                    numero = str(self.solitaire.zone7[i][j].numero)
                    couleur = self.solitaire.zone7[i][j].couleur
                    etat = self.solitaire.zone7[i][j].etat
                    if etat == Etat.MASQUE:
                        image = pygame.image.load('Images/Cartes/images.png')
                        image = pygame.transform.scale(image,(145,197))
                    elif etat == Etat.OUVERT:
                        image = self.images_cartes.img_carte[numero + " " + couleur]
                    image_carte = Img_carte(image, self.images_cartes.rect_image[numero + " " + couleur])
                    self.zone7_image[i].append(image_carte)
        for i in range(4):
            if len(self.solitaire.zone4[i])>0:
                for j in range(len(self.solitaire.zone4[i])):
                    if i == 0:
                        self.zone4_image[i][j].rect.topleft = (self.ecran_long-100.5-145*(i+1),50)
                    else:
                        self.zone4_image[i][j].rect.topleft = (self.ecran_long-100.5-145*(i+1)-45*i,50)
                    self.fenetre.blit(self.zone4_image[i][j].image,self.zone4_image[i][j].rect)
        for i in range(7):
            if len(self.solitaire.zone7[i])>0:
                for j in range(len(self.solitaire.zone7[i])):
                    if i == 0:
                        self.zone7_image[i][j].rect.topleft = (100.5+145*i,297)
                    else:
                        self.zone7_image[i][j].rect.topleft = (100.5+145*i+45*i,297+50*j)
                    self.fenetre.blit(self.zone7_image[i][j].image,self.zone7_image[i][j].rect)           
        pygame.display.update()
    def parametres(self):
        pass

    def nouvelle_partie(self):
        pass

    def continuer_partie(self):
        pass

    def menu_de_jeu(self):
        pass

    def test_click_souris(self, z): #permet de tester tous les évènements possibles lors de l'appuie du bouton droit de la souris
        index = list(self.images_cartes.img_carte.keys())
        for i in range(7):
            for j in range(len(self.solitaire.zone7[i])):
                mot = str(self.solitaire.zone7[i][j].numero) + " " + self.solitaire.zone7[i][j].couleur
                if index[z] == mot:
                    if self.solitaire.zone7[i][j].etat == Etat.OUVERT:
                        if self.solitaire.zone7[i][j] == self.solitaire.zone7[i][-1]:
                            self.images_cartes.moving_image[mot] = True
                        else:
                            pos = self.solitaire.zone7[i].index(self.solitaire.zone7[i][j])
                            for m in range(j, len(self.solitaire.zone7[i])-1):
                                mot1 = str(self.solitaire.zone7[i][m].numero) + " " + self.solitaire.zone7[i][m].couleur
                                mot2 = str(self.solitaire.zone7[i][m+1].numero) + " " + self.solitaire.zone7[i][m+1].couleur
                                if self.solitaire.zone7[i][m].numero == self.solitaire.zone7[i][m+1].numero+1:
                                    if self.solitaire.zone7[i][m].couleur == Couleur.PIQUE or self.solitaire.zone7[i][m].couleur == Couleur.TREFLE:
                                        if self.solitaire.zone7[i][m+1].couleur == Couleur.PIQUE or self.solitaire.zone7[i][m+1].couleur == Couleur.TREFLE:
                                            self.images_cartes.moving_image[mot1] = True
                                            self.images_cartes.moving_image[mot2] = True
                                    elif self.solitaire.zone7[i][m].couleur == Couleur.COEUR or self.solitaire.zone7[i][m].couleur == Couleur.CARREAU:
                                        if self.solitaire.zone7[i][m+1].couleur == Couleur.COEUR or self.solitaire.zone7[i][m+1].couleur == Couleur.CARREAU:
                                            self.images_cartes.moving_image[mot1] = True
                                            self.images_cartes.moving_image[mot2] = True
        for i in range(4):
            if len(self.solitaire.zone4[i])>0:
                mot = str(self.solitaire.zone4[i][-1].numero) + " " + self.solitaire.zone4[i][-1].couleur
                if index[z] == mot:
                    self.solitaire.zone4[i][-1].moving = True   

    def deplacer_image_carte(self):
        pass

                               




        

       




