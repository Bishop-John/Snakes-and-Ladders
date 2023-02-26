import random, time

p1Name = input("What is player 1's name... ")
p2Name = input("What is player 2's name... ")#

p1Score = 0
p2Score = 0#

snakes  = [9,13,21,47,53,66,68,75,83,92,95,99]
ladders = [3,8,25,30,33,41,50,55,62,74,90]

while p1Score < 100 and p2Score < 100:#
    dice = random.randrange(1,6)
    p1Score = p1Score + dice
    print (p1Name, "rolled a number", dice, "and is now on", p1Score)
    if p1Score in snakes:
        movement = random.randrange(1,6)
        p1Score = p1Score - movement
        print ("You have landed on a snake. Move back", movement)
    if p1Score in ladders:
        movement = random.randrange(1,6)
        p1Score = p1Score + movement
        print ("You have landed on a ladder. Move forward", movement)        

    dice = random.randrange(1,6)
    p2Score = p2Score + dice
    print (p2Name, "rolled a number", dice, "and is now on", p2Score)
    if p2Score in snakes:
        movement = random.randrange(1,6)
        p2Score = p2Score - movement
        print ("You have landed on a snake. Move back", movement)
    if p2Score in ladders:
        movement = random.randrange(1,6)
        p1Score = p1Score + movement
        print ("You have landed on a ladder. Move forward", movement)     


    
    print("-----------------------------------------")
    time.sleep(2)
    
print ("End of game")
