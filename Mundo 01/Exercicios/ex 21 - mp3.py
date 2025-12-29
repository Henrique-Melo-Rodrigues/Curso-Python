import pygame as pg

pg.init() #para iniciar o uso do pygame
pg.mixer.music.load('ex 21.mp3') #usar sempre o nome do arquivo em aspas
pg.mixer.music.play() #para dar play a musica
input() #responsável por corrigir o código!
pg.event.wait() #para finalizar a música


