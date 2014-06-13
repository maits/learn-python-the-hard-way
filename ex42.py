## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal 
class Dog(Animal):

    def __init__(self, name):
        ##has-a init
        self.name = name

##Cat is-a animal 
class Cat(Animal):

    def __init__(self, name):
        ## has-a init
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## has-a init
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## has-a init, super
        super(Employee, self).__init__(name)
        ## Employee has-a salary of some kind
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet is-a satan (?)
mary.pet = satan

## Frank is-a employee that takes parameters Frank, 120000
frank = Employee("Frank", 120000)

## Frain has-a pet is-a rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
