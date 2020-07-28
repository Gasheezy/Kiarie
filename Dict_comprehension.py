#dict1 = {"a":1, "b":2, "c": 3, "d":4, "e":5}

#print (dict1.keys())
#print (dict1.values())
#print (dict1.items())

#double_dict1 = {k:v*2 for (k,v) in dict1.items()}

#print (double_dict1)

#--------------------key is a number divisible by 2 in a range of 0-10----------------
# -------------------and it's value is the square of the number.----------------------
numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2 == 0:
        new_dict_for[n] = n**2
print (new_dict_for)        

#--------------Use dictionary comprehension to accomplish the above------------
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print (new_dict_comp)