# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = list(map(lambda x: (float(5)/9) * (x-32), fahrenheit.values()))

celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print (celsius_dict)

#-------------------solve the same problem using dictionary comprehension---------------
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print (celsius)
