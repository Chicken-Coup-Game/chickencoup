import random

# Define the rare chicken types and their traits
chicken_types = {
    "Embercluckers": "Resistant to heat and fire, warm eggs",
    "Crystalwings": "Iridescent, transparent feathers, enchanting eggs",
    "Skywhisper Roosters": "Winged chickens, good omen for fair weather",
    "Moonstone Chickens": "Shimmering feathers, eggs with lunar magic",
    "Dune Striders": "Adapted to desert, salty eggs",
    "Stormfeather Hens": "Predict storms, electrical feathers",
    "Shadowcluckers": "Nocturnal, temporary invisibility eggs",
    "Sunflare Roosters": "Golden feathers, bring sunny weather",
    "Frostplume Fowls": "Ice-cold feathers, frosty eggs",
    "Aurora Chickens": "Radiate colorful lights, eggs with aurora magic",
    "Lavacluckers": "Magma-resistant, lava-heated eggs",
    "Junglejumpers": "Vividly colored feathers, eggs with jungle vibes",
    "Mystic Roosters": "Feathers with magical properties, enchanting eggs",
    "Icy Talons": "Sharp talons, ice-infused eggs",
    "Phoenix Flyers": "Flaming feathers, reborn from ashes",
    "Rainbow Plumes": "Multicolored feathers, bring rainbows",
    "Thunder Beaks": "Loud calls, create thunderstorms",
    "Diamond Crests": "Feathers like diamonds, lay gemstone eggs",
    "Cursed Chickens": "Brings bad luck, hatch cursed eggs",
    "Golden Feathers": "Feathers made of pure gold, valuable eggs",
    "Glitterwings": "Glow in the dark, lay glowing eggs",
}

# Define additional achievements
achievements = {
    "Beginner Birdwatcher": "Find your first rare chicken",
    "Seasoned Birdwatcher": "Find 5 rare chickens",
    "Egg Hunter": "Collect 10 unique eggs",
    "Expert Aviculturist": "Find and collect all rare chickens and their eggs",
    "Isle Explorer": "Visit every location on the Isle of Cverkil",
    "Master of Fate": "Complete all available quests",
}

# Splash text options
splash_texts = [
    "Welcome to the Isle of Cverkil Chicken Hunt!",
    "Find the rare chickens and become a legendary chicken hunter!",
    "Hunt the elusive chickens and discover their unique traits.",
    "Explore the mystical Isle of Cverkil in search of rare poultry.",
    "The Isle of Cverkil awaits your chicken-hunting skills!",
    "Can you uncover the secrets of the rare chickens of Cverkil?",
    "Become the ultimate chicken hunter on this mystical island!",
    "Dare to venture into the Isle of Cverkil and hunt for unique fowl.",
    "The chickens are calling. Can you resist their clucks?",
    "Rumor has it that a legendary chicken roams these lands.",
    "The Isle of Cverkil is waiting for your poultry pursuit!",
    "Discover the wonders of rare poultry in your chicken-hunting adventure.",
    "Bawk, bawk! You're in for an egg-citing journey.",
    "Don't count your chickens before they hatch, but do count your achievements!",
    "Adventure and cluck-tastic discoveries await on the Isle of Cverkil.",
    "Welcome, aspiring chicken whisperer, to the chicken hunter's paradise.",
    "Eggs-traordinary secrets are hidden in the feathers of rare chickens.",
    "The sky is the limit, especially when it's filled with flying chickens!",
]

# Define the size of the map
map_size = 30  # Increase the map size

# Create a list of chicken locations on the Isle of Cverkil
chicken_locations = []

# Generate random chicken locations
def generate_chicken_locations():
    return [(random.choice(list(chicken_types.keys())), (random.randint(1, map_size), random.randint(1, map_size))) for _ in range(20)]  # Increase the number of chickens

# Define player's starting position
player_position = (15, 15)  # Adjust the starting position for the larger map

# Initialize an empty chicken inventory
chicken_inventory = []

# Initialize player's achievements
player_achievements = set()

# Define NPC characters with side quests
def create_npc(name, description, quest, locations):
    return {
        "name": name,
        "description": description,
        "quest": quest,
        "location": random.choice(locations)
    }

npc_locations = [(8, 8), (10, 10), (5, 20)]  # Example locations for NPCs
npcs = [
    create_npc(
        "Farmer John",
        "A friendly farmer who has lost his prized chicken.",
        {
            "name": "Lost Chicken",
            "description": "Find Farmer John's lost chicken and return it to him.",
            "objectives": [
                "Find the lost chicken in the forest (A6).",
                "Return the chicken to Farmer John.",
            ],
            "reward": "Gold coins",
        },
        npc_locations
    ),
    create_npc(
        "Hermit Hilda",
        "A mysterious hermit who seeks an unusual egg for an ancient ritual.",
        {
            "name": "Hermit's Ritual",
            "description": "Find a rare egg for Hermit Hilda's ancient ritual.",
            "objectives": [
                "Locate the Cave of Mysteries (D12).",
                "Retrieve the unique egg from the cave.",
                "Return the egg to Hermit Hilda.",
            ],
            "reward": "Mystical Knowledge",
        },
        npc_locations
    ),
    # Add more NPCs with quests and locations here...
]

# Define islands with their features
islands = {
    "Island of Cverkil": {
        "map_size": 30,  # Define the map size for Island of Cverkil
        "player_position": (15, 15),
        "chicken_locations": [],
        "active_quests": [],
        "dock_location": (7, 7),  # Define a dock location for Island of Cverkil
    },
    "Island of Enderclaw": {
        "map_size": 40,
        "player_position": (20, 20),
        "chicken_locations": [],
        "active_quests": [],
    },
    # Add more islands with their features here...
}

# Function to handle NPC interactions and quests
def handle_npc_interaction(player_position):
    for npc in npcs:
        if npc["location"] == player_position:
            print(f"You have encountered {npc['name']}. {npc['description']}")
            print(f"{npc['name']} offers you a quest: {npc['quest']['name']}")

            # Prompt the player to accept or decline the quest
            accept_quest = input("Accept the quest? (Y/N): ").upper()

            if accept_quest == "Y":
                islands[current_island]["active_quests"].append(npc["quest"])
                print(f"Quest '{npc['quest']['name']}' added to your quest log.")
            else:
                print(f"You declined {npc['name']}'s quest.")

# Function to handle quest menu
def quest_menu():
    while True:
        print("\nQuest Menu:")
        for idx, quest in enumerate(islands[current_island]["active_quests"]):
            print(f"{idx + 1}. {quest['name']} - {quest['description']}")

        print("0. Back to the game")
        choice = input("Select a quest (0 to return): ")
        if choice == "0":
            break
        try:
            quest_index = int(choice) - 1
            if 0 <= quest_index < len(islands[current_island]["active_quests"]):
                print(f"Quest: {islands[current_island]['active_quests'][quest_index]['name']}")
                print(f"Description: {islands[current_island]['active_quests'][quest_index]['description']}")
                print(f"Objectives:")
                for obj in islands[current_island]['active_quests'][quest_index]['objectives']:
                    print(f"  - {obj}")
                print(f"Reward: {islands[current_island]['active_quests'][quest_index]['reward']}")
            else:
                print("Invalid quest number.")
        except ValueError:
            print("Invalid input. Please enter a quest number.")

# Function to display the map
def display_map(player_position, chicken_locations, npcs):
    for row in range(islands[current_island]["map_size"], 0, -1):
        for col in range(1, islands[current_island]["map_size"] + 1):
            if (col, row) == player_position:
                print("P", end=" ")  # Player's position
            elif (col, row) in [location for _, location in chicken_locations]:
                print("C", end=" ")  # Chicken's position
            elif (col, row) in [npc["location"] for npc in npcs]:
                print("N", end=" ")  # NPC's position
            else:
                print(".", end=" ")  # Empty space
        print()  # Move to the next row

# Game loop
current_island = "Island of Cverkil"  # Set the initial island

while True:
    # Randomly select a splash text
    splash_text = random.choice(splash_texts)

    # Display the welcome screen with the map
    print(splash_text)
    print("Can you find all the rare chickens on the island?")
    print(f"Press 'E' to enter the game on {current_island} or 'Q' to quit.")

    # Generate initial chicken locations for the current island
    islands[current_island]["chicken_locations"] = generate_chicken_locations()

    while True:
        display_map(islands[current_island]["player_position"], islands[current_island]["chicken_locations"], npcs)

        user_choice = input("Your choice: ").upper()

        if user_choice != "E":
            print("You have chosen to exit the game. Goodbye!")
            break
        else:
            # Game loop for the current island
            while True:
                print(f"You are at position {islands[current_island]['player_position']}.")
                action = input("Do you want to move (N/S/E/W), check inventory (I), check achievements (A), check quests (Q), or quit (X)? ").upper()

                if action == "X":
                    print("You have quit the game.")
                    break
                elif action in ("N", "S", "E", "W"):
                    if action == "N":
                        islands[current_island]["player_position"] = (
                            islands[current_island]["player_position"][0], islands[current_island]["player_position"][1] + 1)
                    elif action == "S":
                        islands[current_island]["player_position"] = (
                            islands[current_island]["player_position"][0], islands[current_island]["player_position"][1] - 1)
                    elif action == "E":
                        islands[current_island]["player_position"] = (
                            islands[current_island]["player_position"][0] + 1, islands[current_island]["player_position"][1])
                    elif action == "W":
                        islands[current_island]["player_position"] = (
                            islands[current_island]["player_position"][0] - 1, islands[current_island]["player_position"][1])

                    for chicken_type, location in islands[current_island]["chicken_locations"]:
                        if location == islands[current_island]["player_position"]:
                            print(f"You found a {chicken_type} chicken! ({chicken_types[chicken_type]})")
                            islands[current_island]["chicken_locations"].remove((chicken_type, location))
                            chicken_inventory.append(chicken_type)

                            # Check and update achievements
                            if "Beginner Birdwatcher" not in player_achievements and len(chicken_inventory) >= 1:
                                player_achievements.add("Beginner Birdwatcher")
                                print("Achievement Unlocked: Beginner Birdwatcher")

                            if "Seasoned Birdwatcher" not in player_achievements and len(chicken_inventory) >= 5:
                                player_achievements.add("Seasoned Birdwatcher")
                                print("Achievement Unlocked: Seasoned Birdwatcher")

                            if "Egg Hunter" not in player_achievements and len(chicken_inventory) >= 10:
                                player_achievements.add("Egg Hunter")
                                print("Achievement Unlocked: Egg Hunter")

                            if "Expert Aviculturist" not in player_achievements and len(chicken_inventory) == len(chicken_types):
                                player_achievements.add("Expert Aviculturist")
                                print("Achievement Unlocked: Expert Aviculturist")

                if action == "I":
                    print("Inventory:")
                    for chicken in chicken_inventory:
                        print(chicken)

                if action == "A":
                    print("Achievements:")
                    for achievement in player_achievements:
                        print(achievement)

                if action == "Q":
                    quest_menu()  # Call the quest menu function

                # Handle NPC interactions and quests for the current island
                handle_npc_interaction(islands[current_island]["player_position"])

                if not islands[current_island]["chicken_locations"]:
                    print(f"Congratulations! You've found all the rare chickens on the {current_island}.")
                    islands[current_island]["chicken_locations"] = generate_chicken_locations()

                # Check for map transition logic (e.g., move to another island)
                def player_reaches_edge_of_map():
                    x, y = islands[current_island]["player_position"]
                    map_size = islands[current_island]["map_size"]

                    return x <= 0 or y <= 0 or x > map_size or y > map_size
