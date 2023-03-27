import pygame
import sys
import os
from opening_screen import main as opening_scene
from story_gen import randomTitle
import json
from story_gen import *

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 800, 600
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 32
TITLE_SIZE = 48

file_path = "story_data.json"

if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        story_data = json.load(f)
        game_title = story_data["title"]
else:
    story_data = generate_rpg_story_data()
    with open(file_path, "w") as f:
        json.dump(story_data, f)
    game_title = story_data["title"]

bg_image_path = os.path.join("background.jpg")
bg_image = pygame.image.load(bg_image_path)
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Create the screen and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(game_title)

# Load the font, background image, and background music
font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
title_font = pygame.font.Font(pygame.font.get_default_font(), TITLE_SIZE)
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)

# Check if a story file already exists.
def load_story_data():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            story_data = json.load(f)
    else:
        story_data = generate_rpg_story_data()
        with open(file_path, "w") as f:
            json.dump(story_data, f)

    return story_data

def draw_text(text, x_pos, y_pos):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x_pos, y_pos)
    screen.blit(text_surface, text_rect)

def title_screen(story_data):
    clock = pygame.time.Clock()

    menu_options = ["Start Game", "Options", "Exit"]
    selected_option = 0
    
    #title_text = story_data["title"]
    title_text = story_data["title"] if story_data["title"] else "Untitled RPG"

    while True:
        screen.blit(bg_image, (0, 0))

        draw_text(title_text, WIDTH // 2, HEIGHT // 4)  # Display the game title

        for index, option in enumerate(menu_options):
            if index == selected_option:
                draw_text(f"> {option} <", WIDTH // 2, HEIGHT // 2 + index * (FONT_SIZE + 5))
            else:
                draw_text(option, WIDTH // 2, HEIGHT // 2 + index * (FONT_SIZE + 5))
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        print("Starting game...")
                        # TODO: Add game start functionality
                    elif selected_option == 1:  # Options
                        while True:
                            screen.blit(bg_image, (0, 0))
                            draw_text("Options", WIDTH // 2, HEIGHT // 4)

                            option_list = ["Generate New Story", "Back"]

                            for i, option in enumerate(option_list):
                                if i == selected_option:
                                    draw_text(
                                        f"> {option} <",
                                        WIDTH // 2,
                                        HEIGHT // 2 + i * (FONT_SIZE + 5),
                                    )
                                else:
                                    draw_text(
                                        option,
                                        WIDTH // 2,
                                        HEIGHT // 2 + i * (FONT_SIZE + 5),
                                    )

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP:
                                        selected_option = (selected_option - 1) % len(
                                            option_list
                                        )
                                    elif event.key == pygame.K_DOWN:
                                        selected_option = (selected_option + 1) % len(
                                            option_list
                                        )
                                    elif event.key == pygame.K_RETURN:
                                        if selected_option == 0:
                                            os.remove(file_path)
                                            story_data = generate_rpg_story_data()
                                            with open(file_path, 'w') as file:
                                                json.dump(story_data, file)
                                                opening_scene(story_data)
                                        else:
                                            pass  
                                    elif selected_option == 1:
                                        back_menu = title_screen()
                                        if back_to_menu:
                                            break

                            pygame.display.flip()
                            clock.tick(60)

                    elif selected_option == 2:  # Exit
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            story_data = json.load(file)
    else:
        story_data = generate_rpg_story_data()
        with open(file_path, 'w') as file:
            json.dump(story_data, file)
    story_data = load_story_data()
    print(story_data)
    opening_finished = opening_scene(story_data)
    if opening_finished:
        title_screen(story_data)
