class dog:
    
    # Class Attribute
    species  = "mammal"

    # Initializer / Instance Attributes
    def __init__ (self, name, age):
        self.name = name
        self.age = age

#Instantiate the Dog object
phillo = dog("Phillo", 5)
mikey = dog("Mikey", 6)
doug = dog("Doug", 4)

# Access the instance attributes
print ("{} is {} and {} is {}".format (phillo.name, phillo.age, mikey.name, mikey.age))

# Is Phillo a mammal?
if phillo.species == "mammal":
    print ("{0} is a {1}!".format (phillo.name, phillo.species))

#determine the oldest dog
def get_biggest_number (*args):
    return max(args)
print ("The oldest dog is {} years old.".format (get_biggest_number(phillo.age, mikey.age, doug.age)))
