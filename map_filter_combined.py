#Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cube them
arbitrary_numbers = map(lambda num: num **3, filter (lambda num: num %3 ==0, range(1, 21)))
print(list(arbitrary_numbers))


#-------------lists comprehension---------------------------
names = ["Paul", "Collins", "Rodgers", "Mohammed"]
# Instead of: map(lambda x: 'Hi ' + x, names), we can do
greeted_names = ["Hello " + name for name in names]
print(greeted_names)