floatNum = []
n =int(input("Kindly enter the list size: "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNum.append(item)
print("User List is ", floatNum)