from sys import argv
#imports argv from sys so we can use argv as a list to store info

script, filename = argv
#the arguments/var? that are going to be stored in argv

txt = open(filename)
#creaes a var txt that will open a filename

print "Here's your file %r:" % filename
#prints this line with the name of the file
print txt.read()
#reads and prints the file 

print "Type the filename again:"
#prints type the filename again
file_again = raw_input("> ")
#creates a variable file_again that will store the input of the prompt


txt_again = open(file_again)
#creates a variable that will store the text again once it's open

print txt_again.read()
#prints teh file again 
close(txt)
close(txt_again)
