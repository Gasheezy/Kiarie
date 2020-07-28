#------------functions that increment numbers in a list by 2, 5, and 10-----------
#def add2(numbers):
#    new_numbers = []
#    for n in numbers:
#        new_numbers.append(n+2)
#    return new_numbers

#print (add2([23, 28]))

#-----------------create 1 Higher Order Function---------------------------------
def hof_add (increment):
    # Create a function that loops and adds the increment
    def add_increment (numbers):
        new_numbers = []
        for i in numbers:
            new_numbers.append(i + increment)
        return new_numbers
    # We return the function as we do any other value
    return add_increment

add5 = hof_add(5)
print (add5([23, 88]))
add_10 = hof_add(10)
print (add_10([23, 88]))