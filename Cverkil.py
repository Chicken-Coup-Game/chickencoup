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
    "Dare to venture into the Isle of Cverkil and hunt for unique fowl.","The chickens are calling. Can you resist their clucks?",
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
npcs = [
    {
        "name": "Farmer John",
        "description": "A friendly farmer who has lost his prized chicken.",
        "location": (8, 8),
        "quest": {
            "name": "Lost Chicken",
            "description": "Find Farmer John's lost chicken and return it to him.",
            "objectives": [
                "Find the lost chicken in the forest (A6).",
                "Return the chicken to Farmer John.",
            ],
            "reward": "Gold coins",
        }
    },
    # Define other NPCs and their quests here...
]

# Function to handle NPC interactions and quests
def handle_npc_interaction(player_position):
    for npc in npcs:
        if npc["location"] == player_position:
            print(f"You have encountered {npc['name']}. {npc['description']}")
            print(f"{npc['name']} offers you a quest: {npc['quest']['name']}")

            # Prompt the player to accept or decline the quest
            accept_quest = input("Accept the quest? (Y/N): ").upper()

            if accept_quest == "Y":
                active_quests.append(npc["quest"])
                print(f"Quest '{npc['quest']['name']}' added to your quest log.")
            else:
                print(f"You declined {npc['name']}'s quest.")

# Function to handle quest menu
def quest_menu():
    while True:
        print("\nQuest Menu:")
        for idx, quest in enumerate(active_quests):
            print(f"{idx + 1}. {quest['name']} - {quest['description']}")

        print("0. Back to the game")
        choice = input("Select a quest (0 to return): ")
        if choice == "0":
            break
        try:
            quest_index = int(choice) - 1
            if 0 <= quest_index < len(active_quests):
                print(f"Quest: {active_quests[quest_index]['name']}")
                print(f"Description: {active_quests[quest_index]['description']}")
                print(f"Objectives:")
                for obj in active_quests[quest_index]['objectives']:
                    print(f"  - {obj}")
                print(f"Reward: {active_quests[quest_index]['reward']}")
            else:
                print("Invalid quest number.")
        except ValueError:
            print("Invalid input. Please enter a quest number.")

# Game loop
active_quests = []  # Initialize active quests
while True:
    # Randomly select a splash text
    splash_text = random.choice(splash_texts)

    # Display the welcome screen with the map
    print(splash_text)
    print("Can you find all the rare chickens on the island?")
    print("Press 'E' to enter the game or 'Q' to quit.")

    # Generate initial chicken locations
    chicken_locations = generate_chicken_locations()

    while True:
        # Display the map
        for row in range(map_size, 0, -1):
            for col in range(1, map_size + 1):
                if (col, row) == player_position:
                    print("P", end=" ")  # Player's position
                elif (col, row) in [location for _, location in chicken_locations]:
                    print("C", end=" ")  # Chicken's position
                for npc in npcs:
                    if (col, row) == npc["location"]:
                        print("N", end=" ")  # NPC's position
                else:
                    print(".", end=" ")  # Empty space
            print()  # Move to the next row

        user_choice = input("Your choice: ").upper()

        if user_choice != "E":
            print("You have chosen to exit the game. Goodbye!")
            break
        else:
            # Game loop
            while True:
                print(f"You are at position {player_position}.")
                action = input("Do you want to move (N/S/E/W), check inventory (I), check achievements (A), check quests (Q), or quit (X)? ").upper()

                if action == "X":
                    print("You have quit the game.")
                    break
                elif action in ("N", "S", "E", "W"):
                    if action == "N":
                        player_position = (player_position[0], player_position[1] + 1)
                    elif action == "S":
                        player_position = (player_position[0], player_position[1] - 1)
                    elif action == "E":
                        player_position = (player_position[0] + 1, player_position[1])
                    elif action == "W":
                        player_position = (player_position[0] - 1, player_position[1])

                    for chicken_type, location in chicken_locations:
                        if location == player_position:
                            print(f"You found a {chicken_type} chicken! ({chicken_types[chicken_type]})")
                            chicken_locations.remove((chicken_type, location))
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

                if not chicken_locations:
                    print("Congratulations! You've found all the rare chickens on the Isle of Cverkil.")
                    chicken_locations = generate_chicken_locations()

                # Handle NPC interactions and quests
                handle_npc_interaction(player_position)
