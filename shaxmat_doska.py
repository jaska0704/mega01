import pygame
pygame.init()

width, height = 480, 480
screen = pygame.display.set_mode((width, height))

# Qora va oq rangni e'lon qilish
white = (255, 255, 255)
black = (0, 0, 0)

# Kvadrating eni
square_size = 60

# Doska yuzi
board = []
for row in range(10):
    row_list = []
    for column in range(10):
        color = white if (row + column) % 2 == 0 else black
        rect = pygame.Rect(column * square_size, row * square_size, square_size, square_size)
        pygame.draw.rect(screen, color, rect)
        row_list.append(rect)
    board.append(row_list)

pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()