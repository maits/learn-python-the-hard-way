def office():
	print "Could've been worse!"
	print "YOU WIN!"
	exit()

def towing_co():
	print "Justin arrives to the towing company."
	print "The guy who has his car says he needs to pay $2,000 to retrieve his car."
	print "Justin doesn't like this, and thinks the guy is scamming him. They get into a heated argument."
	print "What should he do? Should he pay the $2,000?"

	next = raw_input(">")
	
	if next == "pay $2,000" or "pay" or "pay the $2,000" or "pay fine":
		fired("Justin pays the fine and gets his car. He arrives to the office 2 hours late.")
		
		
	elif next == "don't pay":
		print "The argument between him and the guy escalates to the point they get into a fist fight."
		print "Someone calls the police and Justin gets arrested."
		print "Maite has to bail him. He gets fired the next day."
		print "YOU LOSE!"
		exit(0)

	else:
			print "I got no idea what that means."

def bathroom():
	print "Justin takes a shower but he took too long now."
	print "After he shaved and got dressed, he ran to his car but.. Oh no!"
	print "He realizes his car has been towed because of the strict parking restrictions in Ggtown."	
	print "What should he do? Should he take a cab to work, a bus, or go find his car?"

	next = raw_input(">")

	if "take a cab" in next:
		print "He arrives to the office an hour late."
		office()
	elif "bus" in next:
		fired("Bus takes too long. Justin is not used to taking buses and ends up taking the wrong bus. He ends up in Waldorf, MD. He gets fired the next day.")
	elif "find his car" in next:
		towing_co()
	else:
		fired("I don't know what that means.")
		exit(0)

def car():
	print "He puts on deodorant and perfume and jumps into his car."
	print "He makes it to the office 15 minutes late. His coworkers make fun of him because he stinks."
	office()


def fired(why):
	print why, "YOU LOSE!"
	exit(0)

def start():
	print "Justin wakes up, but oh no, he's going to be late for work!"
	print "He doesn't have enough time to shower. If he does, he'll be late."
	print "What should he do?"

	next = raw_input(">")

	if next == "take shower":
		bathroom()
	elif next == "don't shower":
		car()
	else:
		fired("Justin decides to go back to sleep. Gets fired the next day.")
		exit(0)

start()
