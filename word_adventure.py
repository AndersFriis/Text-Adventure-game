name = input('What is your name?\n')
print ('Get ready to play, %s.' % name)

class Character:
	def __init__(self, name, health):
  		self.name = ""
  		self.health = health


class Room:
	def __init__(self):
		self.doors = 3
		self.right = "right"
		self.left = "left"
		self. straight = "straight"

class Puzzle:
	def __init__(self, puzzle1, puzzle2, puzzle3):
		self.puzzle1 
		self.puzzle2
		self.puzzle3


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self. enemy
 
    def is_alive(self):
        return self.health > 0



def puzzle1():
	
	puzzle_answer = input (" What was the heighest mountain in the world before MT Everest was discovered?")
	if puzzle_answer == "mt everest":
		print ("The door opens and you step into a new room")
	else: 
		print ("The answer is not correct, try again")

		puzzle1()
## Note to self, do not put anythin else under else statement with puzzle1()
def puzzle2():
	
	puzzle_answer = input (" Cry Baby that plays for Real Madrid?")
	if puzzle_answer == "Ronaldo":
			print ("The door opens and you step into a new room")
	else: 
		print ("The answer is not correct, try again")

		puzzle2()


		



Start = Room
print (" You just woke up and find yourself in a dark house. All the windows are blocked and sealed. There are 3 doors in the room.")




answer = input ("What door will you Pick? Right, Left or Straight?")


if Room().right == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle1()


if Room().left == answer:
    print ("You try to open the door, but the door slams in your face. A voice appears and says: I will open this door if you answer this question correctly")
    puzzle2()

else:
	print ("You are facing a ghost enemy")

def enemy ()

	enemy = 





   














