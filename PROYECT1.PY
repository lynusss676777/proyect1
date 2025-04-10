#story=  another normal day, your parents punished you, you will be locked down in your house after you failed an asigment , you ended up your clases   
# school can take a lot of your energy so you just decide to take a nap
#  when you wake up you realize something in your room started a fire, find the way to scape 

import random
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
print("you wake up in your room, smeels weird then you realize its on fire you forgot to close your cigarrete")

choice = input("What do you want to do? (leave/stay): ").lower()
if choice == "leave":
    turns = 1
    print("You decided to leave the room. Turns:", turns)
elif choice == "stay":
    turns += 1
    print("You decided to stay in the room. Turns:", turns)
    room_choice = input("What would you like to do?\n1. Open the closet\n2. Try to open the window\n3. Get your bag\nEnter your choice (1/2/3): ")
    
    if room_choice == "1":
        print("You approach the closet,you find a hammer")
        turns += 1
        print(leave)
    elif room_choice == "2":
        print("You move towards the window,you tried to open it and failed")
        turns += 2
        print(leave)
    elif room_choice == "3":
        print("You reach for your bag,what do you want to do?")
        choice_room_1=input("open (now/later)").lower()
        if choice_room_1 == "now":
            turns += 1
            print("You decided to open the bag and found a navaja . Turns:", turns)
            print(leave)
        elif choice_room_1 == "later":
            turns += 2
            print("You decided to leave the room withouth looking the bag. Turns:", turns)
    else:
        print("Invalid choice!")
else:
    print("Invalid choice! Please choose 'leave' or 'stay'")
leave_room=input("What would you like to do?\n1.Go to the middle of your house\n2. Go to the front of your house\nEnter your choice (1/2):")
     
if leave_room== "right":
     print("You get into the bathroom")
     bathroom_choice = input("What would you like to do?\n1. Get a towel\n2. Open the closet\n3. Get mother's tweezers\n4. Look in the mirror\nEnter your choice (1/2/3/4): ")
        
     if bathroom_choice == "1":
            print("You grab a towel")
            turns += 1
     elif bathroom_choice=="2":
         if "navaja" in player_name:  
                print("You use the navaja to unlock the closet")
                print("You find some medicine inside")
                turns += 1
         else:
                print("The closet is locked. You need something to open it")
                turns += 1
     elif bathroom_choice=="3":
            print("You found your mother's tweezers")
            turns += 1
     elif bathroom_choice == "4":
            print("You see your reflection in the mirror")
            turns += 1
     else:
            print("Invalid choice!")
    
elif leave_room == "left":
        print("You enter the living room")
        living_choice = input("What would you like to do?\n1. Check the TV\n2. Look under the sofa\n3. Go to the kitchen\nEnter your choice (1/2/3): ")








        
elif room_choice == "2":
        print("You move towards the front of the house")
        turns += 4

 else:
        print("Invalid choice!")