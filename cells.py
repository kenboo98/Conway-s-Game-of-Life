from pygame import Color, Surface, draw

ALIVE = 1
DEAD = 0

class Cells:

    def __init__(self, initial_state):

        self.state = initial_state
        self.width = len(initial_state[0])
        self.height = len(initial_state)
        
    def draw(self, screen):
        #self.drawGrid(screen)
        self.drawLiveCells(screen)

    def drawGrid(self, screen):
        
        cell_width = screen.get_width()/self.width
        for i in range(self.width):
            draw.line(screen, (255,255,255), (i*cell_width, 0),(i*cell_width, screen.get_height()))
        
        cell_height = screen.get_height()/self.height
        for i in range(self.height):
            draw.line(screen, (255,255,255), (0,i*cell_height),(screen.get_width(),i*cell_height))
    
    def drawLiveCells(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.state[j][i]:
                    cell_width = screen.get_width()/self.width
                    cell_height = screen.get_height()/self.height
                    draw.rect(screen, (0,0,0),(i*cell_width, j*cell_height, cell_width, cell_height))
    
    def handleClick(self, pos, screen_width, screen_height):
        x = int(pos[0]/(screen_width/self.width))
        y = int(pos[1]/(screen_height/self.height))
        self.state[y][x] = DEAD if self.state[y][x] else ALIVE
    def clear(self):
        self.state = [[0 for j in range(32)] for i in range(32)]
    def update(self):
        for j in range(self.height):
            for i in range(self.width):
                self.state[j][i] = self.checkCell(i, j)

    def checkCell(self, x, y):
        left = top = -1
        right = bottom = 1
        n_alive_cells = 0

        if x == 0:
            left = 0
        if x == self.width-1:
            right = 0
        if y == 0:
            top = -1
        if y == self.height-1:
            bottom = 0

        for i in range(left, right+1):
            for j in range(top, bottom+1):
                if not (i==0 and j==0):
                    n_alive_cells += self.state[y+j][x+i]

        
        if self.state[y][x]:
            if n_alive_cells < 2:
                return 0
            elif n_alive_cells <= 3:
                return 1
            else:
                return 0
            
        if n_alive_cells == 3:
            return 1
        
        return 0
                
                     
