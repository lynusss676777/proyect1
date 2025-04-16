#story=  another normal day, your parents punished you, you will be locked down in your house after you failed an asigment , you ended up your clases   
# school can take a lot of your energy so you just decide to take a nap
#  when you wake up you realize something in your room started a fire, find the way to scape 

import random

game_active = True
items = {
    'navaja': False,
    'hammer': False,
    'keys': False,
    'batteries': False,
    'tweezers': False,
    'towel': False,
    'fire_extinguisher': False
}
turns = 0 

def print_inventory():
    print("\nYour items:")
    for item, has_item in items.items():
        if has_item:
            print(f"- {item}")
    print(f"Turns taken: {turns}\n")


print("Welcome to Escape the Fire!")
player_name = input("Write your character's name: ").lower()
while len(player_name) < 2:
    player_name = input("Please enter a longer name: ").lower()
print(f"{player_name}, I hope you can escape!")

print("\nYou wake up in your room, smells weird then you realize it's on fire - you forgot to close your cigarette!")

while game_active:
    choice = input("\nWhat do you want to do? (leave/stay): ").lower()
    
    if choice == "leave":
        turns += 1
        print("You decided to leave the room.")
    elif choice == "stay":
        turns += 1
        print("You decided to stay in the room.")
        room_choice = input("What would you like to do?\n1. Open the closet\n2. Try to open the window\n3. Get your bag\nEnter choice (1/2/3): ")
        
        if room_choice == "1":
            print("You find a hammer in the closet!")
            items['hammer'] = True
            turns += 1
        elif room_choice == "2":
            if items['hammer']:
                print("You use the hammer to break the window! You escaped!")
                game_active = False
                continue
            else:
                print("The window won't budge. Maybe you need something to break it.")
                turns += 1
        elif room_choice == "3":
            bag_choice = input("Open bag now or later? (now/later): ").lower()
            if bag_choice == "now":
                print("You found a navaja in your bag!")
                items['navaja'] = True
                turns += 1
            else:
                print("You decide to check the bag later.")
                turns += 1
    
    if game_active:
        location = input("\nWhere to?\n1. Middle of house\n2. Front of house\nChoice (1/2): ")
        
        if location == "1":
            print("\nYou're in the middle of the house.")
            direction = input("Go right to bathroom or left to living room? (right/left): ").lower()
            
            if direction == "right":
                print("\nYou enter the bathroom.")
                turns += 1
                bathroom_choice = input("1. Get towel\n2. Open closet\n3. Get tweezers\n4. Look in mirror\nChoice (1/2/3/4): ")
                
                if bathroom_choice == "1":
                    print("You grab a towel - could be useful against smoke!")
                    items['towel'] = True
                    turns += 1
                elif bathroom_choice == "2":
                    if items['navaja']:
                        print("You unlock the closet with your navaja and find some keys!")
                        turns += 1
                        items['keys'] = True
                    else:
                        print("The closet is locked. Need something to open it.")
                        turns += 1
                elif bathroom_choice == "3":
                    print("You grab the tweezers.")
                    items['tweezers'] = True
                    turns += 1
                elif bathroom_choice == "4":
                    print("Just your scared reflection...")
                    turns += 1
            elif direction == "left":
                print("\nYou enter the living room.")
                living_choice = input("1. Check TV\n2. Look under sofa\n3. Go to front\nChoice (1/2/3): ")
                
                if living_choice == "1":
                    if items['batteries']:
                        print("You use the batteries to power the TV and see the emergency exit route!")
                    else:
                        print("TV has no power.")
                        turns += 1
                elif living_choice == "2":
                    if not items['keys']:
                        print("You find some keys under the sofa!")
                        items['keys'] = True
                        turns += 1
                elif living_choice == "3":
                    print("Moving to the front of the house...")
                    turns += 1
        
        elif location == "2":
            print("\nYou're at the front of the house.")
            turns += 1
            front_choice = input("Go to:\n1. Kitchen\n2. Garage\nChoice (1/2): ")
            
            if front_choice == "1":
                print("\nIn the kitchen.")
                kitchen_choice = input("1. Check fridge\n2. Check drawers\n3. Check stove\nChoice (1/2/3): ")
                
                if kitchen_choice == "1":
                    print("Nothing useful in the fridge.")
                    turns += 1
                elif kitchen_choice == "2":
                    if not items['batteries']:
                        print("You find some batteries!")
                        turns += 1
                        items['batteries'] = True
                elif kitchen_choice == "3":
                    if items['hammer']:
                        print("You use the hammer to break the gas line and create an escape route!")
                        game_active = False
                        continue
                    else:
                        print("The stove looks breakable with the right tool...")
                        turns += 1
            
            elif front_choice == "2":
                print("\nIn the garage.")
                turns += 1
                garage_choice = input("1. Check car\n3. Garage door\nChoice (1/2/3): ")
                
                if garage_choice == "1":
                    if items['keys']:
                        print("You use the keys to start the car and drive through the garage door! You escaped!")
                        game_active = False
                        continue
                    else:
                        print("Car needs keys.")
                        turns += 1
                
                elif garage_choice == "3":
                    if items['batteries']:
                        print("You power up the garage door with batteries and escape!")
                        game_active = False
                        continue
                    else:
                        print("Door needs power.")
        
        print_inventory()
        turns += 1
        
        if turns >= 15:
            print("\nThe fire has spread too much. Game Over!")
            game_active = False

print(f"\nGame ended in {turns} turns.")
if turns < 15:
    print("Congratulations on escaping!")
