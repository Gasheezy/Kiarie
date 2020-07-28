mutable_collection = ["Tim", 10, [4,5]]
immutable_collection = ("Tim", 10, [4,5])

# Reading from data types are essentially the same:
print (mutable_collection[1])
print (immutable_collection[2])

# Let's change the 2nd value from 10 to 15
mutable_collection[1] = 15
print (mutable_collection[1])

# This fails with the tuple
#immutable_collection[1] = 15

#---------------where a Tuple may appear to be a mutable object------------------
immutable_collection[2].append(6)
print (immutable_collection)