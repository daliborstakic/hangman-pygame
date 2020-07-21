import pygame

WIDTH = 1000
HEIGHT = 600

# Setting up the screen
surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Colors
WHITE = (255, 255, 255)


def main():
    run = True

    while run:
        surf.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


main()
