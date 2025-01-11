import pygame
pygame.init()
pygame.mixer.music.load('paulada128.mp3')
pygame.mixer.music.play(2)
input()
pygame.event.wait()