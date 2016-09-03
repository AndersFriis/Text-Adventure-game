import random

name = input('What is your name?\n')

print ('Hello, %s. lets play' % name)



class Player:
	def __init__(self, name):
  		self.name = ""
  		self.health = 15
  		
	def attack_enemy (self, attack_enemy):
		dmg=random.randint(0,3)
		enemy.health -=dmg
		print("Player did {} damage".format(dmg))
		if enemy.health <= 0: 
			print("You killed the enemy")


class Enemy:
	def __init__(self, name):
		self.name = name
		self.health = 9

	
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
	def __init__(self, puzzle1, puzzle2, puzzle3):
		self.puzzle1 
		self.puzzle2
		self.puzzle3


       


def puzzle1():
	
	puzzle_answer = input (" What was the heighest mountain in the world before MT Everest was discovered?")
	if puzzle_answer == "mt everest":
		print ("The door opens and you step into a new room")
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


		



Start = Room
print (" You just woke up and find yourself in a dark house. All the windows are blocked and sealed. There are 3 doors in the room.")

player = Player(name)	
enemy = Enemy(name)


answer = input ("What door will you Pick? Right = R, Left = L or Straight = S?")


if Room().right == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle1()


if Room().left == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle2()

else:
	print ("You are facing an enemy")
	while player.health > 0 or enemy.health > 0:
		player.attack_enemy(enemy)		
		enemy.attack_player(player)


			
		






		









			
	


		













   














