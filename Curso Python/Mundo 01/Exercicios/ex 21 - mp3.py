import pygame
pygame.init() #para iniciar o uso do pygame
pygame.mixer.music.load('ex021.mp3')
#usar sempre o nome do arquivo em aspas
pygame.mixer.music.play() #para dar play a musica
input() #responsável por corrigir o código!
pygame.event.wait() #para finalizar a música


