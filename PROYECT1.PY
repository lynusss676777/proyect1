#story=  another normal day, your parents punished you, you will be locked down in your house after you failed an asigment , you ended up your clases   
# school can take a lot of your energy so you just decide to take a nap
#  when you wake up you realize something in your room started a fire, find the way to scape 

import random
turns=0
room2=True
stage=1

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
     elif room_choice == "2":
        print("You move towards the window,you tried to open it and failed")
        turns += 2
    elif room_choice == "3":
        print("You reach for your bag,what do you want to do?"
        choice_room_1=("open (now/later").lower()
        if choice_room_1 == "now":
            print("You decided to leave the room. Turns:", turns)
             turns += 1
            
        elif choice_room_1 == "later":
            turns += 2
    print("You decided to stay in the room. Turns:", turns)
    else:
        print("Invalid choice!")
else:
    print("Invalid choice! Please choose 'leave' or 'stay'")