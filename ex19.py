def cheese_and_crackers(cheese_count, boxes_of_crackers):
#defines the function cheese_and_crackers and passes 2 arguments
	print "You have %d cheeses!" % cheese_count
#prints how many cheeses you have
	print "You have %d boxes of crackers!" % boxes_of_crackers
#prints how many boxes of crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
#the \n adds a space btw the print statements

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#assings numbers to te functions - 20 cheese count and 30 boxes

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#creates two vars, amount of cheese and amout of crackers, and asignes values to them

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#changes the argument in the fuction cheese and crackers to amount of cheese and amount of crackers

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#adds up amounts inside the function and prints them

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
#combines the functions with the amounts

