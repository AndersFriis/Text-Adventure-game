import random

name = input('What is your name?\n')

print ('Hello, %s. lets play' % name)



class Player:
	def __init__(self, name):
  		self.name = ""
  		self.health = 10
  		
	def attack_enemy (self, attack_enemy):
		dmg=random.randint(1,3)
		enemy.health -=dmg
		print("Player did {} damage".format(dmg))
		if enemy.health <= 0: 
			print("You killed the enemy, and moving on to the next room")


class Enemy:
	def __init__(self, name):
		self.name = name
		self.health = 1

	
	def attack_player(self, player):
		dmg=random.randint(0,3)
		player.health -=dmg
		print("enemy did {} damage".format(dmg))
		if player.health <= 0:
			print ("You Died, GameOver")    





class Room:
	def __init__(self):
		self.doors = 3
		self.right = "R"
		self.left = "L"
		self. straight = "S"




class Puzzle:
    def __init__(self, puzzle1, puzzle2, puzzle3, puzzle4, puzzle5):
        self.puzzle1
        self.puzzle2
        self.puzzle3
        self.puzzle4
        self.puzzle5
        self.puzzle6
        self.puzzle7 
        
        

def puzzle1():
	
	puzzle_answer = input (" What was the heighest mountain in the world before MT Everest was discovered?")
	if puzzle_answer == "mt everest":
		print ("The door opens and you step into a new room, Hint: Mt ")
	else: 
		print ("The answer is not correct, try again")

		puzzle1()
## Note to self, do not put anythin else under else statement with puzzle1()
def puzzle2():
	
	puzzle_answer = input (" What has a head and a tail, but no body?")
	if puzzle_answer == "A coin":
			print ("The door opens and you step into a new room")
	else: 
		print ("The answer is not correct, try again")

		puzzle2()


def puzzle3():
    
    puzzle_answer = input (" What is the National flower of Holland")
    if puzzle_answer == "tulip":
        print ("The door opens and you step into a new room")
    else: 
        print ("The answer is not correct, try again")

        puzzle3()		


def puzzle4():
    
    puzzle_answer = input (" What is the biggest city in the U.S, New York, L.A or Dallas?")
    if puzzle_answer == "New York":
        print ("The door opens and you step into a new room")
    else: 
        print ("The answer is not correct, try again")

        puzzle4()               


def puzzle5():
    
    puzzle_answer = input ("What ship sank on its maiden voyage in 1912, Titanic, Bismark or Quuen Elizabeth")
    if puzzle_answer == "Titanic":
        print ("The door opens and you step into a new room")
    else: 
        print ("The answer is not correct, try again")

        puzzle5()

def puzzle6():
    
    puzzle_answer = input ("What year did WW1 start, 1912, 1915, 1917")
    if puzzle_answer == "1912":
        print ("You are now in the final room and must answer 3 questions correct to win the game")
    else: 
        print ("The answer is not correct, try again")

        puzzle6()

def puzzle7():
    
    puzzle_answer = input ("American involvement in the Korean war took place in what decade, 1950's, 1960's 1970's")
    if puzzle_answer == "1950's":
        print ("You are now in the final room and must answer 3 questions correct to win the game")
    else: 
        print ("The answer is not correct, try again")

        puzzle7()

def puzzle8():
    
    puzzle_answer = input ("The Hundred Years War was fought between what two countries, France & England or Belgium & France?")
    if puzzle_answer == "France & England":
        print ("You are now in the final room and must answer 3 questions correct to win the game")
    else: 
        print ("The answer is not correct, try again")

        puzzle8()

def puzzle9():
    
    puzzle_answer = input ("What the Capital of Germany, Bonn, Berlin or Munich?")
    if puzzle_answer == "Berlin":
        print ("That is correct, 2 questions more to win")
    else: 
        print ("The answer is not correct, you lost the game")

        puzzle9()

def puzzle10():
    
    puzzle_answer = input ("What is the largest ocean in the world, Pacific, Atlantic or the Indian?")
    if puzzle_answer == "Pacific":
        print ("That is correct, 1 questions more to win")
    else: 
        print ("The answer is not correct, you lost the game")

        puzzle10()

def puzzle11():
    
    puzzle_answer = input ("What elephant is bigger, African or Indian?")
    if puzzle_answer == "African":
        print ("CONGRATS YOU WON THE GAME")
    else: 
        print ("The answer is not correct, you lost the game")

        puzzle11()




## Room number 1 (Start Room) __________________________________________________________________

player = Player(name)   
enemy = Enemy(name)

Start = Room
print ("This is an Educational Game. There are 3 doors in each room. The game will consist of puzzle and enemy fights.")


answer = input ("What door will you Pick? Right = R, Left = L or Straight = S?")


if Room().right == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle1()


if Room().left == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle2()

else:
    
    print ("You are facing an enemy, if you answer the question correct you will hit the enemy, or else he will hit you")
    
    puzzle_answer = input ("What ship sank on its maiden voyage in 1912, Titanic, Bismark or Quuen Elizabeth")
if  puzzle_answer == "Titanic": 
    print ("You hit the Enemy")
    player.attack_enemy(enemy) 
else: 
    puzzle_answer == "Bismark, Queen Elizabeth"
    print (" The enemy hit you")
    enemy.attack_player(player)

## Room number 2(New Room)_______________________________________________





New = Room
print (" You are now in a new room")

answer = input ("What door will you Pick? Right = R, Left = L or Straight = S?")

if Room().right == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle3()


if Room().left == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle4()


else:
    
    print ("You are facing an enemy, if you answer the question correct you will hit the enemy, or else he will hit you")
    
    puzzle_answer = input ("What is the biggest city in the U.S, New York, L.A or Dallas?")
if  puzzle_answer == "New York": 
    print ("You hit the Enemy")
    player.attack_enemy(enemy) 
else: 
    puzzle_answer == "L.A, Dallas"
    print (" The enemy hit you")
    enemy.attack_player(player)


## Room number 3 (New Room) _________________________________________

New = Room
print (" You are now in a new room")

answer = input ("What door will you Pick? Right = R, Left = L or Straight = S?")

if Room().right == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle6()


if Room().left == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle7()

if Room().straight == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle8()

## Final Room__________________________________

New = Room
print("The Final Room") 
















			
		






		









			
	


		













   














