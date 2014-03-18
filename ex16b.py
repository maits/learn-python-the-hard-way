#a script that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
