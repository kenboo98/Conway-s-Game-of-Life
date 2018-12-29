from pygame import Color, Surface, draw

ALIVE = True
DEAD = False

class Cells:

    def __init__(self, initial_state):

        self.state = initial_state
        self.width = len(initial_state[0])
        self.height = len(initial_state)
        
    def draw(self, screen):
        self.drawGrid(screen)
        
    def drawGrid(self, screen):
        
        cell_width = screen.get_width()/self.width
        for i in range(self.width):
            draw.line(screen, (255,255,255), (i*cell_width, 0),(i*cell_width, screen.get_height()))
        
        cell_height = screen.get_height()/self.height
        for i in range(self.height):
            draw.line(screen, (255,255,255), (0,i*cell_height),(screen.get_width(),i*cell_height))
    
    