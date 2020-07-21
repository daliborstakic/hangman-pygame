import pygame

pygame.init()

# Screen parameters
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
BLACK = (0, 0, 0)

# Fonts
LETTER_FONT = pygame.font.SysFont('arial', 30)

# Circle parameters
RADIUS = 25
GAP = 15

# Clock
clock = pygame.time.Clock()
FPS = 60


def render_screen(hangman_status, letters):
    surf.fill(WHITE)
    surf.blit(hangman_images[hangman_status], (70, (HEIGHT - hangman_images[hangman_status].get_height()) // 2 - 80))

    for letter in letters:
        x, y, char, visible = letter
        if visible:
            pygame.draw.circle(surf, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(char, 1, BLACK)
            surf.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    pygame.display.update()


def initialize_letters():
    # Calculating the coordinates of the circles
    start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    start_y = 450

    # Letter list
    letters = []
    A = 65

    for i in range(26):
        x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = start_y + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

    return letters


def main():
    # Game variables
    hangman_status = 0
    letters = initialize_letters()

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        render_screen(hangman_status, letters)

    pygame.quit()


main()
