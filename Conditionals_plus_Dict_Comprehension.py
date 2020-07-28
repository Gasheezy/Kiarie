dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, "f":6}
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 ==0}
#dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 ==0 if v%3 ==0}

# Identify odd and even entries
dict1_tripleCond = {k:("even" if v%2 ==0 else "odd") for (k,v) in dict1.items()}
dict1_tripleCond = {k:(if v%2 ==0 "even" else "odd") for (k,v) in dict1.items()}

print (dict1_tripleCond)