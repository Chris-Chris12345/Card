import pygame
import time

WIDTH = 800
HEIGHT = 500

pygame.init()

display_screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Card")

img = pygame.image.load("birthday_image1")
img1 = pygame.transform.scale(img,(WIDTH,HEIGHT))

while 1:
    font = pygame.font.SysFont("Arial",60)
    text1 = font.render("Happy Birthday",True,(0,0,0))
    display_screen.blit((255,255,255))
    display_screen.blit(img1,(0,0))
    display_screen.blit(text1,(400,250))
    pygame.display.update()

    time.sleep(2)
    
    