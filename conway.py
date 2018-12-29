# PyGame template.
 
# Import standard modules.
import sys, random
from cells import Cells

# Import non-standard modules.
import pygame
from pygame.locals import *

FPS = 60.0

class Game:

  def __init__(self):
        # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    self.fpsClock = pygame.time.Clock()
    # Set up the window.
    width, height = 640, 640
    self.screen = pygame.display.set_mode((width, height))

    initial_state = [[bool(random.getrandbits(1)) for j in range(32)] for i in range(32)]
    self.cells = Cells(initial_state)

    # Main game loop.
  def update(self, dt):
    for event in pygame.event.get():
      # We need to handle these events. Initially the only one you'll want to care
      # about is the QUIT event, because if you don't handle it, your game will crash
      # whenever someone tries to exit.
      if event.type == QUIT:
        pygame.quit() # Opposite of pygame.init
        sys.exit() # Not including this line crashes the script on Windows. Possibly
        # on other operating systems too, but I don't know for sure.
      # Handle other events as you wish.

  def draw(self, screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0)) # Fill the screen with black.
    self.cells.draw(screen)
    # Redraw screen here.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()

  def run(self):
    dt = 1/FPS # dt is the time since last frame.
    while True: # Loop forever!
        self.update(dt) # You can update/draw here, I've just moved the code for neatness.
        self.draw(self.screen)
        dt = self.fpsClock.tick(FPS)

if __name__ == "__main__":
    Game().run()