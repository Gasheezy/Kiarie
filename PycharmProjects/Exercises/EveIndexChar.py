def EveIndexChar(str):
    for i in range (0,len(str)-1, 2):
        print("index [",i,"]", str[i])

inputStr = input("Enter String ")
print("Original String is ", inputStr)

print("Printing only even index chars")
EveIndexChar(inputStr)