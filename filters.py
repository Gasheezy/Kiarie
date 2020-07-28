numbers = [15, 83, 69, 70]

div_by_5 = filter(lambda num: num%5 == 0, numbers)
print(list(div_by_5))

#-----------Another way could be: ----------------------
#div_by_5 = [num for num in numbers if num %5 == 0]
#print(div_by_5)