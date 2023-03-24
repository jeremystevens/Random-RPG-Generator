import pygame
import sys
import textwrap
from pygame.locals import *
import os
from story_gen import generate_rpg_storyline
# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 24

# Create the screen and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Opening Screen")

# Load the font, background image, and background music
font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# if a story_data.json file exist then we shouldn't generate a new title
def load_story_data():
    file_path = 'story_data.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            story_data = json.load(file)
    else:
        story_data = generate_rpg_story_data()
        with open(file_path, 'w') as file:
            json.dump(story_data, file)

    return story_data

def draw_text(text_lines, y_pos):
    for index, line in enumerate(text_lines):
        text_surface = font.render(line, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, y_pos + index * (FONT_SIZE + 5))
        screen.blit(text_surface, text_rect)

def main(story_data):
    clock = pygame.time.Clock()
    scroll_speed = 1
    text_y = HEIGHT
    if story_data is None:
        file_path = 'story_data.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                story_data = json.load(file)
        else:
            story_data = generate_rpg_story_data()
            with open(file_path, 'w') as file:
                json.dump(story_data, file)

    story = story_data['storyline']
    wrapped_story = textwrap.wrap(story, width=50)  # Adjust the width as needed
    while True:
        screen.blit(background_image, (0, 0))

        draw_text(wrapped_story, text_y)

        text_y -= scroll_speed

        # Check if the text has scrolled off the screen
        if text_y + len(wrapped_story) * (FONT_SIZE + 5) < 0:
            pygame.mixer.music.fadeout(2000)  # Fade out music over 2 seconds (2000 ms)
            return True # Fade out music over 2 seconds (2000 ms)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    story_data = load_story_data()
    print("#### " + story_data)
    main(story_data)
