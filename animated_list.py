"""
This is a Python script that animates a linked list using Pygame.
It defines the AnimatedList class, which inherits from the LinkedList class.
The class contains methods for creating nodes, updating node positions for animation purposes,
and shifting/moving the entire linked list.
"""

from linked_list import LinkedList
from constants import *
import pygame

class AnimatedList(LinkedList):
    def __init__(self, screen, num_nodes=150, growth_rate_function=lambda x: x, pos_modifier_function=lambda x,y,z : (x,y,z), draw_links=True, draw_nodes=True):
        super().__init__()
        self.screen = screen
        self.growth_rate_function = growth_rate_function
        self.pos_modifier_function = pos_modifier_function
        self.draw_links = draw_links
        self.draw_nodes = draw_nodes
        self.alpha = 0
        self.speed = 0
        self.counter = 0
        self.create_nodes(num_nodes)
    
    def create_nodes(self, num_nodes):
        for i in range(num_nodes):
            cords = [WITDH/2 ,(HEIGHT/2)+i]
            self.add_node(cords)

    def _animation_update(self, node, node_size_increase=0):
        """
        This is a recursive function that updates the positions of the nodes in the linked list for animation purposes.
        It starts from the last node and updates the position of each node to match the position of the previous node.
        Finally, it draws the nodes and links on the screen using Pygame.
        """
        if node != None:
            #calculating the radius of the node based on the growth rate function and the node size increase
            node_size_increase += GROWTH_RATE
            radius = self.growth_rate_function(NODE_SIZE+node_size_increase)
            #calling the function again for the next node
            self._animation_update(node.next, node_size_increase)

            #drawing node as a circle
            if self.draw_nodes:
                pygame.draw.circle(self.screen, NODE_COLOR, (node.data[0], node.data[1]), radius, NODE_FILL)
            
            if node.prev != None:
                #updating node's position to match the prev node's position
                x_offset, y_offset = self.pos_modifier_function(node.data[0],node.data[1],node_size_increase)
                node.data[0] = node.prev.data[0] - x_offset
                node.data[1] = node.prev.data[1] - y_offset
                #drawing link between the node and the prev node
                if self.draw_links:
                    pygame.draw.aaline(self.screen, NODE_LINK_COLOR, (node.data[0], node.data[1]), (node.prev.data[0], node.prev.data[1]))

    def animation_update(self):
        """
        This function updates the positions of the nodes in the linked list for animation purposes by calling the _animation_update function.
        """
        self.counter = 0
        self._animation_update(self.head)
    
    def shift_linked_list(self, delta_x, delta_y):
        """
        This function shifts the linked list by adding delta_x to the x-coordinate and delta_y to the y-coordinate
        of the head node's data. It then updates the positions of the nodes for animation purposes.
        """
        self.head.data[0] += delta_x
        self.head.data[1] += delta_y
        self.animation_update()
    

    def move_linked_list_to_position(self, x, y):
        """
        This function moves the linked list to the specified position (x, y) by setting the head node's x-coordinate
        to x and the y-coordinate to y. It then updates the positions of the nodes for animation purposes.
        """
        self.head.data[0] = x
        self.head.data[1] = y
        self.animation_update()
