import time
import pygame
from pygame.locals import *

class Interface:
    def __init__(self):
        pygame.init()
        self.ecran_long,self.ecran_larg = 1100, 750
        self.fenetre = pygame.display.set_mode((self.ecran_long, self.ecran_larg), pygame.RESIZABLE)
        self.image_de_fond_menu = pygame.image.load('Images/bg2.jpg')
        self.actif = 1

        while self.actif: 
            self.image_de_fond_menu = pygame.transform.scale(self.image_de_fond_menu,(self.fenetre.get_width(),self.fenetre.get_height()))    
            self.fenetre.blit(self.image_de_fond_menu,(0,0))
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
        #btn_newgame = pygame.image.load()
        #btn_lastgame = pygame.image.load()
        btn_parametres = pygame.image.load("./Images/Cartes/2 Carreau 1.png")
        btn_parametres = pygame.transform.scale(btn_parametres,(145,197))
        #btn_quitter = pygame.image.load()
        rect = btn_parametres.get_rect()
        rect.center = 145//2, 197//2
        rect.topleft = (0,0)
        running = True
        moving = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    self.actif = 0
                elif event.type == MOUSEBUTTONDOWN:
                    if rect.collidepoint(event.pos):
                        moving = True
                elif event.type == MOUSEBUTTONUP:
                    moving = False
                elif event.type == MOUSEMOTION and moving:
                    rect.move_ip(event.rel)
            self.fenetre.blit(self.image_de_fond_menu,(0,0))
            self.fenetre.blit(btn_parametres,rect)
            pygame.display.update()

    def parametres(self):
        pass

    def nouvelle_partie(self):
        pass

    def continuer_partie(self):
        pass

    def menu_de_jeu(self):

        pass


        

       




