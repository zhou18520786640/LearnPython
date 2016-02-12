#coding:utf-8

from sys import exit

# 金房间
def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input(">")
	if	"0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man,learn to type a number:") # 会退出脚本
	if	how_much < 50:
		print "Nice, you're not greddy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
	
# 熊的房间
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch if honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input(">")
		
		if	next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the doo. You can go through it now."
			bear_moved = Ture
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

# 妖怪的房间
def cthulhu_room(): # 邪恶的妖怪
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
	
# 死
def dead(why):
	print why, "Good job!"
	exit(0)

# 开始
def start():
	print "You are in a dark room."
	print "There is a door to your right and left"
	print "Which one do you take?"
	
	next = raw_input(">")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
	
start()
		
		
	
