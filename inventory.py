# Period: 1
# Date created: 10/1/21
# Date last modified:
# Name: Dalton Low
# Description: Rpg inventory

# Creates a list of character choices
characters = ["Wizard", "Knight", "Adventurer"]

# Creates a list of characters weapons
inventories = {"Wizard": 
                {"Magic wand":
                  {"description": "Uses magic to cast spells on enemies"}},
            "Knight":
                {"Sword":
                  {"description": "A metal weapon used for close range combat"},
                "Shield":
                  {"description": "Used to block or parry enemie attacks"}},
            "Adventurer":
                {"Map":
                  {"description": "A map of the dungeon"},
            "Dagger":
                  {"description": "A small blade with very minimal damage"}}}

# Prints out a list of possible character choices
for person in characters:
    print(f"Would you like to be a {person}")

# Creates a variable to keep track of the character choice
char_choice = input("")

# Creates a invalid input statement
# Code addapted from stack Over flow
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while char_choice.lower() not in ("wizard", "knight", "adventurer"):
    print(f"Please enter a valid input")
    char_choice = input("")

# Creates a situation if character is the knight
if char_choice.lower() == "wizard":
    del inventories["Knight"]
    del inventories["Adventurer"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])

# Creates a situtaion if character is the knight
if char_choice.lower() == "knight":
    del inventories["Wizard"]
    del inventories["Adventurer"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])

# Creates a situation if the character is a adventurer
if char_choice.lower() == "adventurer":
    del inventories["Wizard"]
    del inventories["Knight"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])
                char_choice = "adventurer"


# Creates a list of places the player can go
locations = ["Treasure room", "Hallways", "Combat room", "Rest room"]

# Creates a dictionary of places in the game
loc_text = {"Treasure room":
              {"text": "You see a small chest open it and see whats inside"},
            "Hallways":
              {"text": "You enter the hallway and move forward through the dungeon"},
            "Combat room":
              {"text": "An enemy jumps out and attacks you"},
            "Rest room":
              {"text": " You enter a room where you can rest a and heal"},
            "Dragon room":
              {"text": " You approach the room where the dragon lives, prepare for the final battle"}}

# Asks the player where they would like to start
print("Where would you like to go")
for location in locations:
    print(f"The {location}")
play_location = input("")

# Adds the final boss room back
locations.append("Dragon room")

# Prints text if player is in treasure room
if play_location.lower == "treasure room":
    loc_text = loc_text["Treasure room"]["text"]
    print(f"{loc_text}")

# Prints text if player is in the hallway
if play_location.lower == "hallways":
    loc_text = loc_text["Hallways"]["text"]
    print(f"{loc_text}")

# Prints text if player is in treasure room
if play_location.lower() == "combat room":
    loc_text = loc_text["Combat room"]["text"]
    print(f"{loc_text}")

# Prints text if player is in treasure room
if play_location.lower() == "rest room":
    loc_text = loc_text["Rest room"]["text"]
    print(f"{loc_text}")
