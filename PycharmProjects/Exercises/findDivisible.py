def findDivisible(numList):
    print("Given list is ", numList)
    print("Numbers divisible by 5 in the list are:")

    for num in numList:
        if (num%5 == 0):
            print(num)

numList = [10, 55, 89, 79, 70]
findDivisible(numList)