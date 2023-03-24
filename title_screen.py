import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
TEXT_COLOR = (255, 255, 255)
TITLE_SIZE = 48
MENU_SIZE = 32

# Create the screen and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Title Screen")

# Load the font, background image, and background music
title_font = pygame.font.Font(pygame.font.get_default_font(), TITLE_SIZE)
menu_font = pygame.font.Font(pygame.font.get_default_font(), MENU_SIZE)
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

def draw_text(text, font, y_pos):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, y_pos)
    screen.blit(text_surface, text_rect)

def title_screen():
    pygame.mixer.music.play()
    
    clock = pygame.time.Clock()
    
    title_y = HEIGHT // 4
    menu_start_y = HEIGHT // 2
    menu_spacing = MENU_SIZE + 10
    
    menu_items = ["Start Game", "Options"]

    while True:
        screen.blit(background_image, (0, 0))
        
        # Draw title
        draw_text("RPG Title", title_font, title_y)

        # Draw menu items
        for index, item in enumerate(menu_items):
            draw_text(item, menu_font, menu_start_y + index * menu_spacing)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    title_screen()
