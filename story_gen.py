import random
import time
import uuid
import json
import os
# Seed the random number generator
random.seed(time.time())

# Story elements
settings = ["a mysterious forest", "a haunted castle", "a bustling city", "a forgotten dungeon", "a hidden village"]
heroes = ["a brave knight", "a cunning rogue", "a wise mage", "a skilled archer", "a powerful warrior"]
allies = ["a loyal squire", "an enigmatic thief", "an ancient guardian", "a gifted healer", "an inspiring bard"]
villains = ["an evil sorcerer", "a ruthless warlord", "a fearsome dragon", "a vengeful ghost", "a horde of undead"]
quests = ["recover a lost artifact", "rescue a kidnapped noble", "defeat a powerful enemy", "solve a mysterious riddle", "uncover a dark secret"]
complications = ["a hidden curse", "a brewing war", "an unexpected betrayal", "an ancient prophecy", "a powerful artifact"]
game_titles = ["Mystery of the Lost Realm", "Rise of the Enchanted", "The Forgotten Prophecy", "Shadow of the Ancient War", "Legacy of the Fallen Kingdom"]
# Add RPG keywords for game title generation
#title_adjectives = ["Eternal", "Forgotten", "Mystical", "Enchanted", "Shadowy"]
#title_nouns = ["Kingdom", "Realm", "Prophecy", "Legacy", "Quest"]
#title_descriptors = ["of Darkness", "of Light", "of the Ancients", "of the Lost", "of Destiny"]
title_adjectives = [
    "Eternal", "Forgotten", "Mystical", "Enchanted", "Shadowy",
    "Ancient", "Mysterious", "Hidden", "Cursed", "Lost",
    "Fabled", "Legendary", "Sacred", "Mythic", "Epic",
    "Dark", "Whispering", "Haunted", "Twisted", "Vengeful",
    "Wandering", "Glorious", "Radiant", "Majestic", "Cryptic",
    "Shrouded", "Infinite", "Divine", "Tainted", "Hallowed",
    "Unyielding", "Enigmatic", "Forbidden", "Runebound", "Benevolent",
    "Hunted", "Reclusive", "Shattered", "Windswept", "Ethereal",
    "Ravaged", "Burning", "Frozen", "Arcane", "Unseen",
    "Exalted", "Forsaken", "Infernal", "Celestial", "Temporal"
]

title_nouns = [
    "Kingdom", "Realm", "Prophecy", "Legacy", "Quest",
    "Land", "Empire", "Chronicle", "Rune", "Fortress",
    "Forest", "Mountain", "Island", "Desert", "Oasis",
    "Cavern", "Dungeon", "Labyrinth", "Sanctuary", "Tomb",
    "Tower", "Keep", "Citadel", "Castle", "Palace",
    "Fountain", "Shrine", "Catacomb", "Temple", "Monolith",
    "Bastion", "Stronghold", "City", "Village", "Garrison",
    "Tundra", "Swamp", "Cove", "Throne", "Harbor",
    "Grove", "Chamber", "Mausoleum", "Archive", "Haven",
    "Vault", "Expanse", "Barrow", "Glade", "World"
]

title_descriptors = [
    "of Darkness", "of Light", "of the Ancients", "of the Lost", "of Destiny",
    "of Shadows", "of Time", "of Eternity", "of Dreams", "of Chaos",
    "of Elements", "of Fire", "of Ice", "of Earth", "of Wind",
    "of Power", "of Hope", "of Despair", "of the Fallen", "of Redemption",
    "of Betrayal", "of Secrets", "of Illusions", "of Nightmares", "of the Abyss",
    "of the Void", "of the Stars", "of the Moon", "of the Sun", "of the Heavens",
    "of Courage", "of Wisdom", "of the Forgotten", "of the Vanished", "of the Hidden",
    "of the Fates", "of the Sages", "of the Seekers", "of the Wanderers", "of the Protectors",
    "of the Destroyers", "of the Creators", "of the Maelstrom", "of the Depths", "of the Heights",
    "of the Vanguard", "of the Reckoning", "of the Rebellion", "of the Covenant",  "of the Storm", "of the Silent", "of the Infinite", "of the Damned", "of the Blessed",
    "of the Broken", "of the Risen", "of the Exiled", "of the Sorrow", "of the Triumph",
    "of the Enigma", "of the Miracle", "of the Nexus", "of the Conquerors", "of the Defenders",
    "of the Veil", "of the Nexus", "of the Unknown", "of the Rapture", "of the Resurgence",
    "of the Ascended", "of the Convergence", "of the Sundered", "of the Outcasts", "of the Forsworn",
    "of the Awakened", "of the Drowned", "of the Embers", "of the Mist", "of the Pioneers"
]
def generate_rpg_storyline():
    setting = random.choice(settings)
    hero = random.choice(heroes)
    ally = random.choice(allies)
    villain = random.choice(villains)
    quest = random.choice(quests)
    complication = random.choice(complications)
    title_adjective = random.choice(title_adjectives)
    title_noun = random.choice(title_nouns)
    title_descriptor = random.choice(title_descriptors)
    story = (f"In {setting}, {hero} embarks on a perilous journey to {quest}. "
             f"Joined by {ally}, they face numerous challenges and adversaries. "
             f"But beware, for {villain} will do anything to thwart the hero's plans. "
             f"Furthermore, {complication} threatens to change the course of their adventure.")
    title = f"{title_adjective} {title_noun} of {title_descriptor}"
    story_id = str(uuid.uuid4())
    
    return {'storyline': story, 'title': title}

def randomTitle():
      #game_title = random.choice(game_titles)
       # Generate a random game title using RPG keywords
      game_title = f"{random.choice(title_adjectives)} {random.choice(title_nouns)} {random.choice(title_descriptors)}"
      return game_title
    
def save_story_data(story_data, file_name="story_data.json"):
    with open(file_name, "w") as f:
        json.dump(story_data, f)

def load_story_data(file_name="story_data.json"):
    with open(file_name, "r") as f:
        story_data = json.load(f)
    return story_data

# Generate and print a random RPG storyline
file_path = 'story_data.json'

# if a story_data.json file already exist then don't generate a new title
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        storyline = json.load(file)
else:
    storyline = generate_rpg_storyline()
    with open(file_path, 'w') as file:
        json.dump(storyline, file)

#storyline = generate_rpg_storyline()
save_story_data(storyline)

