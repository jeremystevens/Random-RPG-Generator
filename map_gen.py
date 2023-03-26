import random

# Map dimensions
MAP_WIDTH = 40
MAP_HEIGHT = 20

# Map symbols
TREE = 'T'
ENEMY = 'E'
CASTLE = 'C'
EMPTY = ' '

def generate_random_map():
    # Calculate the number of trees and enemies
    num_trees = int(MAP_WIDTH * MAP_HEIGHT * 0.2)  # 20% of map cells
    num_enemies = int(MAP_WIDTH * MAP_HEIGHT * 0.1)  # 10% of map cells

    # Create an empty map
    map_data = [[EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    # Place trees randomly
    for _ in range(num_trees):
        tree_x = random.randint(0, MAP_WIDTH - 1)
        tree_y = random.randint(0, MAP_HEIGHT - 1)
        while map_data[tree_y][tree_x] != EMPTY:
            tree_x = random.randint(0, MAP_WIDTH - 1)
            tree_y = random.randint(0, MAP_HEIGHT - 1)
        map_data[tree_y][tree_x] = TREE

    # Place enemies randomly
    for _ in range(num_enemies):
        enemy_x = random.randint(0, MAP_WIDTH - 1)
        enemy_y = random.randint(0, MAP_HEIGHT - 1)
        while map_data[enemy_y][enemy_x] != EMPTY:
            enemy_x = random.randint(0, MAP_WIDTH - 1)
            enemy_y = random.randint(0, MAP_HEIGHT - 1)
        map_data[enemy_y][enemy_x] = ENEMY

    # Place the castle randomly
    castle_x = random.randint(0, MAP_WIDTH - 1)
    castle_y = random.randint(0, MAP_HEIGHT - 1)
    while map_data[castle_y][castle_x] != EMPTY:
        castle_x = random.randint(0, MAP_WIDTH - 1)
        castle_y = random.randint(0, MAP_HEIGHT - 1)
    map_data[castle_y][castle_x] = CASTLE

    return map_data

def save_map_to_file(map_data, filename):
    with open(filename, 'w') as file:
        for row in map_data:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    map_data = generate_random_map()
    save_map_to_file(map_data, 'map.txt')
