import pygame

WIDTH = 1000
HEIGHT = 600

# Setting up the screen
surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Images
hangman_images = []
for i in range(7):
    hangman_images.append(pygame.image.load("images\hangman{}.png".format(str(i))))

# Colors
WHITE = (255, 255, 255)


def render(hangman_status):
    surf.fill(WHITE)
    surf.blit(hangman_images[hangman_status], (70, (HEIGHT - hangman_images[hangman_status].get_height()) / 2 - 80))
    pygame.display.update()


def main():
    # Hangman variables
    hangman_status = 0

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        render(hangman_status)

    pygame.quit()


main()
