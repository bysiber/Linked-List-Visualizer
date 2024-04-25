import math
import pygame
from constants import *
from animated_list import AnimatedList

if __name__ == "__main__":
    screen = pygame.display.set_mode((WITDH, HEIGHT))
    
    #you can change these functions
    growth_rate_function=lambda x: x
    pos_modifier_function=lambda x,y,z : (0,0)

    animated_list = AnimatedList(screen, growth_rate_function=growth_rate_function, pos_modifier_function=pos_modifier_function, draw_links=True, draw_nodes=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((0,0,0))     
        x,y = pygame.mouse.get_pos()
        animated_list.move_linked_list_to_position(x,y)

        pygame.time.wait(5)
        pygame.display.update()
