def sumNum (num):
    previousNum = 0
    for i in range (num):
        sum = previousNum + i
        print("Current number is ", i, "Previous number is ", previousNum, "Sum is ", sum)
        previousNum = i

print("Printing current and previous number in a given range (10)")
sumNum(10)