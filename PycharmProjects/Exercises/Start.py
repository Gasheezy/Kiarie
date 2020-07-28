def mult_or_sum (x, y):
    product  = x*y
    sum = x+y

    if x*y > 1000:
        return product
    else:
        return sum

x = int(input("Enter first number "))
y = int(input("Enter second number "))

result = mult_or_sum(x,y)
print("The result is ", result)