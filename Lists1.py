#new_range = [i*i for i in range(5) if i%2 ==0]

#x = [i for i in range (10)]
#print (x)

#--------------Lists by Loop--------------
#squares = []

#for x in range(10):
#    squares.append(x**2)

#print (squares)

#-------------list comprehensions-------------------------
#squares = [x**2 for x in range(10)]
#print (squares)

#-------------Multiplying parts of a list-----------------
#list1 = [3,4,5]
#multiplied = [j*3 for j in list1]

#print (multiplied)

#------------Show the first letter of each word------------
#listOfWords = ["this", "is", "a", "list", "of", "words"]
#items = [word[0] for word in listOfWords]
#print (items)

#------------Print numbers/text only from a string---------
#string = "Hello 12345 World"
#numbers = [x for x in string if x.isdigit()]
#print (numbers)

#------------list comprehension in functions-------
def double(x):
    return x*2
    [double(x) for x in range(10)]
print double(x)


