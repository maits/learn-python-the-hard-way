x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #there's a string within a string

print x
print y

print "I said: %r." % x #here's a string within a string 
print "I also said: '%s' . " % y #here's a string within a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #here's a string within a string 

w = "This is the left side of..."
e = "a string with a right side."

print w + e

