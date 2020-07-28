def reverseCheck(number):
    print("Original number ", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum*10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False
print("Is this number the same when reversed? \n", reverseCheck(0))