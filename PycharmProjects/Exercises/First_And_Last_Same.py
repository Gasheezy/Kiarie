def isFirst_and_Last (numbers):
    print("The given list is ", numbers)
    first_element = numbers[0]
    last_element = numbers[-1]

    if (first_element == last_element):
        return True
    else:
        return False

numList = [10,20,30,40,50,10]
print("The result is ", isFirst_and_Last(numList))