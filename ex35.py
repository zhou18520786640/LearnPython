from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(">")
	if	"0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man,learn to type a number:")
		
def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input(">")
	
	if	next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
	
start()
	
	if	how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
	def bear_room():
		print "There is a bear here."
		print "The bear has a lunch of honey."
		print "The fat bear is in front of another door."
		print "How are you going to move the bear?"
		bear_moved = False
					
		while True:
			next = 	raw_input(">")
			
			if	next == "Take honey":
				dead("The bear looks at you then slaps your face off.")
			elif next == "taunt bear" and not bear_moved:
				dead("")