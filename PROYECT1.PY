#story=  another normal day, your parents punished you, you will be locked down in your house after you failed an asigment , you ended up your clases   
# school can take a lot of your energy so you just decide to take a nap
#  when you wake up you realize something in your room started a fire, find the way to scape 

import random
Game1=True
Game2=True
Game3=True
batteries=1
keys=1
tweezers=1
hammer=1
navaja=1
turns=0
room2=True
stage=1
leave=("you didn't find something else, you decide to leave the room")
print("welcome to this game")
player_name=input("write your character's name:").lower()
while len(player_name) >= 0:
  if len(player_name) > 1:
    print(player_name+". I hope you can scape!!")
    break
    
if len(player_name) == 1:
    player_name_choice =( player_name+"try another name!!")
print("you wake up in your room, smeels weird then you realize its on fire you forgot to close your cigarrete\n")

choice = input("What do you want to do? (leave/stay): ").lower()
if choice == "leave":
    turns+= 1
    print("You decided to leave the room. Turns:", turns)
elif choice == "stay":
    turns += 1
    print("You decided to stay in the room. Turns:", turns)
    room_choice = input("What would you like to do?\n1. Open the closet\n2. Try to open the window\n3. Get your bag\nEnter your choice (1/2/3): ")
    
    if room_choice == "1":
        print("You approach the closet,you find a hammer")
        hammer=True
        turns += 1
        print(leave)
    elif room_choice == "2":
        print("You move towards the window,you tried to open it and failed\n")
        turns += 2
        print(leave)
    elif room_choice == "3":
        print("You reach for your bag,what do you want to do?\n")
        choice_room_1=input("open (now/later)").lower()
        if choice_room_1 == "now":
            navaja=True
            turns += 1
            print("You decided to open the bag and found a navaja . Turns:", turns)
            print(leave)
        elif choice_room_1 == "later":
            navaja= False
            turns += 2
            print("You decided to leave the room withouth looking the bag. Turns:", turns)
    else:
        print("Invalid choice!")
else:
    print("Invalid choice! Please choose 'leave' or 'stay'")
leave_room=input("What would you like to do?\n1.Go to the middle of your house\n2. Go to the front of your house\nEnter your choice (1/2):")
if leave_room== "1":
    print("You go to the middle of the house\n")
    turns += 1
    print("at your right there is a bathroom, at your left there is a door towards the living room\n")
    choice_sect_1=input("where do you want to go?(right/left)").lower()
     
    if choice_sect_1 == "right":
     print("You get into the bathroom\n")
     bathroom_choice = input("What would you like to do?\n1. Get a towel\n2. Open the closet\n3. Get mother's tweezers\n4. Look in the mirror\nEnter your choice (1/2/3/4): ")
        
     if bathroom_choice == "1":
            print("You grab a towel\n")
            turns += 3
            print(leave)
     elif bathroom_choice=="2":
         if navaja==True:  
                print("You use the navaja to unlock the closet\n")
                print("You find some medicine inside\n")
                turns += 1
                print(leave)
         else:
                print("The closet is locked. You need something to open it\n")
                turns += 1
                print(leave)
     elif bathroom_choice=="3":
            print("You found your mother's tweezers\n")
            turns += 1
            print(leave)
     elif bathroom_choice == "4":
            print("You see your reflection in the mirror\n")
            turns += 3
            print(leave)
     else:
            print("Invalid choice!")
    
    elif choice_sect_1 == "left":
        print("You enter the living room\n")
        living_choice = input("What would you like to do?\n1. Check the TV\n2. Look under the sofa\n3. Go to the front\nEnter your choice (1/2/3): ")
        if living_choice == "1":
            print("The TV is not working due to the fire\n")
            turns += random ;{0,5}
            print(leave)
        elif living_choice == "2":
            print("You find some keys under the sofa\n")
            turns += 1
            print(leave)
        elif living_choice == "3":
            print("You move towards the front\n")
            turns += 1
            print(leave)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice! Please choose 'right' or 'left'") 

elif leave_room == "2":
        print("You move towards the front of the house\n")
        turns += 4
front_choice = input("Where would you like to go?\n1. Kitchen\n2. Garage\nEnter your choice (1/2): ")
if front_choice == "1":
        print("You enter the kitchen")
        kitchen_choice = input("What would you like to do?\n1. Check the fridge\n2. Look in the drawers\n3. Check the stove\nEnter your choice (1/2/3): ")
        if kitchen_choice == "1":
            print("You find some water bottles in the fridge")
            turns -= 1
        elif kitchen_choice == "2":
            print("You find some batteries in the drawer")
            turns += 1
        elif kitchen_choice == "3":
            print("The stove won't help you with anything! Better be far from it")
            turns += 1
        else:
            print("Invalid choice!")
    
elif front_choice == "2":
        print("You enter the garage\n")
        garage_choice = input("What would you like to do?\n1. Check the car\n2. Look at the tool bench\n3. Try the garage door\nEnter your choice (1/2/3): ")
        if garage_choice == "1":
            print("The car won't start without keys")
            turns += 1
        elif garage_choice == "2":
            print("You find a fire extinguisher!")
            turns += 1
        elif garage_choice == "3":
            print("The electrical garage door won't open without power")
            turns += 1 
        else:
            print("Invalid choice!")
else:
        print("Invalid choice! Please choose 1 or 2")

        
