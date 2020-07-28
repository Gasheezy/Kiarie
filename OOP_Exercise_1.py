#Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. 
#In other words, the Dog class does not inherit from the Pets class. 
#Then assign three dog instances to an instance of the Pets class. 
#Start with the following code below. Your output should look like this:
#I have 3 dogs. 
#Tom is 6. 
#Fletcher is 7. 
#Larry is 9. 
#And they're all mammals, of course.

#Parent Class
class Pets:

    dogs = []

    def __init__ (self, dogs):
        self.dogs = dogs

#Parent class
class Dog:

    #Class Attribute
    species = "mammal"

    #Initializer / Instance attributes
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    #Instance Method
    def description (self):
        return self.name, self.age
    
    #Instance Method
    def speak (self, sound):
        return "%s says %s" % (self.name, sound)
    
    #Instance Method
    def eat (self):
        self.is_hungry = False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

#Child class (inherits from dog class)
class Bulldog (Dog):
    def run (self, speed):
        return "%s runs %s" %(self.name, speed)

# Child class (inherits from Dog class)
class Chiwawa(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

#Create Instances of Dogs
my_dogs = [
    Bulldog ("Tom", 6),
    RussellTerrier ("Fletcher", 7),
    Chiwawa ("Kimo", 9)
]

#Instanciate the pets class
my_pets = Pets (my_dogs)

#Output
print ("I have {} dogs.".format (len(my_pets.dogs)))
for dog in my_pets.dogs:
    print ("{} is {}.".format(dog.name, dog.age))

print ("And they are all {}s, of course.".format(dog.species))