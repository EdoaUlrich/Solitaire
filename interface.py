import time
import pygame
from pygame.locals import *

class Interface:
    def __init__(self):
        pygame.init()
        self.ecran_long,self.ecran_larg = 463, 600
        self.fenetre = pygame.display.set_mode((self.ecran_long, self.ecran_larg))
        self.image_de_fond = pygame.image.load('Images/bg2.jpg')
        self.image_de_fond = pygame.transform.scale(self.image_de_fond,(self.ecran_long,self.ecran_larg))
        actif = 1

        while actif: 
            self.fenetre.blit(self.image_de_fond,(0,0))
            self.menu()
            for event in pygame.event.get():
                if event.type == QUIT:
                    actif = 0
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        actif = 1
            pygame.display.update()
        pygame.quit()

    def menu(self):
        #btn_newgame = pygame.image.load()
        #btn_lastgame = pygame.image.load()
        btn_parametres = pygame.image.load('Images/settings.jpg').convert_alpha()
        #btn_quitter = pygame.image.load()
        rect = btn_parametres.get_rect()
        rect.bottomright = (100,100)
        self.fenetre.blit(btn_parametres, (rect.x, rect.y))

    def parametres(self):
        pass

    def nouvelle_partie(self):
        pass

    def continuer_partie(self):
        pass


        

       




