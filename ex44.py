class Parent(object):
	
	def override(self):
		print "PARENT override()"

#override explicitly
#overrides parent

	def implicit(self):
		print "PARENT implicit()"

#defines an implicit function for parent
#implicit inheritance

	def altered(self):
		print "PARENT altered()"

#alters parent
#alter before or after

class Child(Parent):

#class CHILD inherts from parent
	
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
#dad is an instance of parent 
son = Child()
#son is an instance of child

#this part calls the functions 
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
