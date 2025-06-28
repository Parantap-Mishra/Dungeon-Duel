import random

# Define the player's starting inventory
inventory = {
    'weapons': [('Small Dagger', (1, 3))],
    'armor': [('Leather Armor', 5)],
    'potions': [],
    'coins': 100
}

# Define the shop items
shop = {
    'armor': {
        'Leather Armor': {'defense': 5, 'price': 50},
        'Iron Armor': {'defense': 10, 'price': 100},
        'Diamond Armor': {'defense': 20, 'price': 200},
        'Netherite Armor': {'defense': 30, 'price': 300}
    },
    'weapons': {
        'Dagger': {'damage': (1, 3), 'price': 50},
        'Long Sword': {'damage': (3, 7), 'price': 100},
        'Axe': {'damage': (5, 10), 'price': 150}
    },
    'potions': {
        'Health Boost': {'effect': 'heal', 'value': 20, 'price': 30},
        'Attack Boost': {'effect': 'boost', 'value': 5, 'price': 30}
    }
}

# Define the monsters for each level
monsters = [
    {'name': 'Goblin', 'hitpoints': 50, 'damage': (1, 5)},
    {'name': 'Orc', 'hitpoints': 75, 'damage': (3, 7)},
    {'name': 'Troll', 'hitpoints': 100, 'damage': (5, 10)},
    {'name': 'Giant', 'hitpoints': 150, 'damage': (7, 12)},
    {'name': 'Dragon', 'hitpoints': 200, 'damage': (10, 15)}
]

# Function to display the inventory
def show_inventory():
    print("\nInventory:")
    for category, items in inventory.items():
        if category != 'coins':
            print(f"{category.capitalize()}:")
            for item in items:
                print(f"  - {item[0]}")
        else:
            print(f"Coins: {items}")

# Function to handle shopping
def shop_menu():
    print("\nWelcome to the shop!")
    while True:
        print("\nShop Categories:")
        print("1. Armor")
        print("2. Weapons")
        print("3. Potions")
        print("4. Exit Shop")
        choice = input("Choose a category: ")
        if choice == '1':
            buy_item('armor')
        elif choice == '2':
            buy_item('weapons')
        elif choice == '3':
            buy_item('potions')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to buy items from the shop
def buy_item(category):
    while True:
        print(f"\nAvailable {category.capitalize()}:")
        for item, details in shop[category].items():
            print(f"{item}: {details['price']} coins")
        print("Type 'back' to return to the shop menu.")
        choice = input("Enter the name of the item you want to buy: ")
        if choice.lower() == 'back':
            break
        if choice in shop[category]:
            if inventory['coins'] >= shop[category][choice]['price']:
                inventory['coins'] -= shop[category][choice]['price']
                if category == 'armor':
                    inventory['armor'].append((choice, shop[category][choice]['defense']))
                elif category == 'weapons':
                    inventory['weapons'].append((choice, shop[category][choice]['damage']))
                elif category == 'potions':
                    inventory['potions'].append((choice, shop[category][choice]['effect'], shop[category][choice]['value']))
                print(f"You bought {choice}!")
            else:
                print("You don't have enough coins.")
        else:
            print("Invalid item.")

# Function to handle combat
def combat(monster):
    player_hp = 100
    monster_hp = monster['hitpoints']
    print(f"\nA wild {monster['name']} appears!")
    while player_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {player_hp}")
        print(f"{monster['name']}'s HP: {monster_hp}")
        
        # Player's turn
        while True:
            action = input("Choose your action (attack/use potion): ").lower()
            if action == 'attack':
                attack_choice = input("Choose your attack (high/medium/low): ").lower()
                if attack_choice in ['high', 'medium', 'low']:
                    break
                else:
                    print("Invalid choice. Please choose high, medium, or low.")
            elif action == 'use potion':
                if inventory['potions']:
                    use_potion()
                    break
                else:
                    print("You have no potions to use.")
            else:
                print("Invalid action. Please choose attack or use potion.")
        
        if action == 'attack':
            monster_defense = random.choice(['high', 'medium', 'low'])
            if attack_choice == monster_defense:
                print(f"The {monster['name']} defended your attack!")
            else:
                monster_hp = attack(monster_hp)
        
        if monster_hp <= 0:
            print(f"You defeated the {monster['name']}!")
            break
        
        # Monster's turn to attack
        defense_choice = input("Choose your defense (high/medium/low): ").lower()
        while defense_choice not in ['high', 'medium', 'low']:
            print("Invalid choice. Please choose high, medium, or low.")
            defense_choice = input("Choose your defense (high/medium/low): ").lower()
        
        monster_attack = random.choice(['high', 'medium', 'low'])
        if defense_choice == monster_attack:
            print("You successfully defended the attack!")
        else:
            player_hp = defend(monster, player_hp)
        
        if player_hp <= 0:
            print("You have been defeated.")
            break

# Function to handle player attack
def attack(monster_hp):
    weapon = inventory['weapons'][0]
    damage = random.randint(weapon[1][0], weapon[1][1])
    monster_hp -= damage
    print(f"You attacked with your {weapon[0]} and dealt {damage} damage!")
    return monster_hp

# Function to handle player defense
def defend(monster, player_hp):
    damage = random.randint(monster['damage'][0], monster['damage'][1])
    player_hp -= damage
    print(f"The {monster['name']} attacked and dealt {damage} damage!")
    return player_hp

# Function to use a potion
def use_potion():
    global player_hp
    print("\nAvailable Potions:")
    for i, potion in enumerate(inventory['potions']):
        print(f"{i + 1}. {potion[0]}")
    choice = input("Choose a potion to use: ")
    if choice.isdigit() and 1 <= int(choice) <= len(inventory['potions']):
        potion = inventory['potions'].pop(int(choice) - 1)
        if potion[1] == 'heal':
            player_hp += potion[2]
            print(f"You used a {potion[0]} and healed {potion[2]} HP!")
        elif potion[1] == 'boost':
            print(f"You used a {potion[0]} and boosted your attack by {potion[2]}!")
    else:
        print("Invalid choice. No potion used.")

# Main menu
def main_menu():
    current_level = 0
    while True:
        print("\nMain Menu:")
        print("1. Show Inventory")
        print("2. Shop")
        print("3. Enter Arena")
        print("4. Exit Game")
        choice = input("Choose an option: ")
        if choice == '1':
            show_inventory()
        elif choice == '2':
            shop_menu()
        elif choice == '3':
            current_level = enter_arena(current_level)
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to enter the arena
def enter_arena(current_level):
    while current_level < len(monsters):
        combat(monsters[current_level])
        if current_level < len(monsters) - 1:
            print("\nWhat would you like to do next?")
            current_level+=1
            print("1. Continue to next level")
            print("2. Return to main menu")
            choice = input("Choose an option: ")
            while choice not in ['1', '2']:
                print("Invalid choice. Please choose 1 or 2.")
                choice = input("Choose an option: ")
            if choice == '2':
                break
    return current_level

# Start the game
main_menu()