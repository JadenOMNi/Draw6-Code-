import pygame
import os
import sys


# Define a desired aspect ratio
ASPECT_RATIO = 11 / 7

WIN_SIZE = (1100, 700)
WIN = pygame.display.set_mode(WIN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Please Work")

GREEN = (0, 128, 0)

# Load images

image = pygame.image.load(os.path.join('images', 'casino_chips', 'chip_1_w85h85.png'))
image = pygame.transform.scale(image, (100, 100))  # adjust size of image

run = True

clock = pygame.time.Clock()

# Calculate the new height of the window based on the desired aspect ratio and the current width
def calculate_new_height(width):
    new_height = int(width / ASPECT_RATIO)
    return new_height

# Calculate the new width of the window based on the desired aspect ratio and the current height
def calculate_new_width(height):
    new_width = int(height * ASPECT_RATIO)
    return new_width

def draw_window():
    global WIN
    # Resize the window if needed
    window_width, window_height = WIN.get_size()
    new_width = calculate_new_width(window_height)
    new_height = calculate_new_height(window_width)
    if window_width != new_width or window_height != new_height:
        WIN = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    # Fill the window with green
    WIN.fill(GREEN)

    # Get the dimensions of the window
    window_width, window_height = WIN.get_size()

    # Calculate the position for the bottom right corner of the image
    image_width, image_height = image.get_size()
    image_x = window_width - image_width
    image_y = window_height - image_height

    # Blit the image to the screen
    WIN.blit(image, (image_x, image_y))

def main():
    global run

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        pygame.display.update()

        clock.tick(60)  # Limit frame rate

    pygame.quit()

if __name__ == "__main__":
    main()