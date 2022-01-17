import pygame
import random

WIDTH = 400
HEIGHT = 400
FPS = 60

# ========================================== COLOUR DEFINITIONS =======================================================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ========================================== END OF - COLOUR DEFINITIONS ==============================================

# ======================================== INITIALIZE PYGAME AND CREATE WINDOW ========================================
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Title")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# ======================================== END OF - INITIALIZE PYGAME AND CREATE ======================================

# ===================================================== GAME LOOP =====================================================
done = False
while not done:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            done = True
    # --------------------------------------------------- UPDATE --------------------------------------------------
    all_sprites.update()

    # --------------------------------------------------- DRAW ----------------------------------------------------
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # ---------------------------------------------- REFRESH THE SCREEN -------------------------------------------
    pygame.display.flip()
pygame.quit()