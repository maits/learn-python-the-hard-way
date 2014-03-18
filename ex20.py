from sys import argv
#it imports a list from argv

script, input_file = argv
#there's two attributes to argv

def print_all(f):
	print f.read()
#defines a function: print all, which reads f

def rewind(f):
	f.seek(0)
#defines another function, rewind f

def print_a_line(line_count, f):
	print line_count, f.readline()
#defines a function - print a line, it counts the line and then reads them

current_file = open(input_file)
#defines current file as something tht opens the input file
print "First let's print the whole file:\n"


print_all(current_file)
#prints the file
print "Now let's rewind, kind of like a tape."

rewind(current_file)
#rewinds current file
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
#prints a line from the current file
current_line = current_line + 1
print_a_line(current_line, current_file)
#prints the line following the previous one

current_line = current_line + 1
print_a_line(current_line, current_file)
#idem

#What is f in the print_all and other functions?
#The f is a variable just like you had in other functions in Exercise 18, 
#except this time it's a file. A file in Python is kind of like an old tape drive 
#on a mainframe, or maybe a DVD player. It has a "read head," and you can "seek" 
#this read head around the file to positions, then work with it there. Each time 
#you do f.seek(0) you're moving to the start of the file. Each time you do f.readline() 
#you're reading a line from the file, and moving the read head to right after the \n that 
#ends that file. This will be explained more as you go on
