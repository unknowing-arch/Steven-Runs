import time
i = 0
rstart = "N"
slt = .25
while rstart.lower() != "y" and rstart.lower() != "yes" and rstart != "sure":
    i = i + 2
    print("S t a r t   G a m e"[0:i])
    time.sleep(slt)
    if i == 10 and slt != 0:i = i + 2
    if i == 20 and slt != 0:
        rstart = str.lower(input("\n.-.   .-.   .-.   .-.   .-.       .-.   .-.   .  .   .-. \n`-.    |    |-|   |(     |        |..   |-|   |\/|   |-  \n`-'    '    ` '   ' '    '        `-'   ` '   '  `   `-'\n\n"))
        if rstart == "qwerty": slt = 0
        else: i = 0
print(" you wake up one day.\n in fact your brother annoyingly shulk you awake\n you will be grumpy for the rest of the day.\n you decide that you should run away\n you have a choice between a sword, a magical rock, and a magical staff\n object: [sword] [rock] [staff]")
item = "nothing"
while item.lower() != "sword" and item.lower() != "rock" and item.lower() != "staff":
    item = str.lower(input())
    if item == "sword" or item == "rock" or item == "staff": print("You chose a " + item + "!\n")
print(" You start to walk out the door\n which direction do you go?\n Do you go left or right")
direction = ("none")
while direction.lower() != "left" and direction != "right": direction = str.lower(input())
if direction == "left": print("\n\nwhile you walked " + direction + "\n then you encounter a ravinous dog\n you piss your pants\n you will now move twice as slow\n")
if item == "rock" or item == "staff" and direction == "left": print("\n\nyou bipassed the curse with your " + item + ", making your speed go back to normal. you sigh in releaf\n")
if direction == "left": time.sleep(7.5)
print(" \n\nyou come to a corner\n since your mother told you that you are not allowed to cross the street\n do you go " + direction + " or cross the street?")
while rstart != direction:
    rstart = str.lower(input(" \n\ncross or go " + direction + "?\n"))
    if rstart == "cross": print(" your mother always told you to never cross the street")
    if rstart == "cross": i = 1000
    elif rstart == "right" and direction == "left" or rstart == "left" and direction == "right": print(" You want to go back home?\n nah, you though about it some more.")
print("You decided to go " + direction + "\n you continue marching forward\n you pass by two other corners keeping on going" + direction)
if item == "sword": print(" \nYou walked by a dog barkikng,\n you defented yourself with your sword,\n you continue on ward")
else: print(" \nYou walked by a dog barkikng,\n you piss your pants, you udderly embarised\n")
time.sleep(2)
print(" on your way you see you house again?\n how would this be possible?\n you decide to go in to your mother, who has been freaking out trying to find you \n you tell her why you ran away and your brother gets in trouble and is grounded.")
if i != 1000: print("Your mother hugs you and gets you ice cream")
print("You have won the game, congratulations!\nThanks For playing!")
time.sleep(100)
