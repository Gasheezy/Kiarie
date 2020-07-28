def mergeList(list1, list2):
    print("First List", list1)
    print("Second List", list2)
    list3 = []

    for num in list1:
        if (num %2 != 0):
            list3.append(num)
    for num in list2:
        if (num %2 != 0):
            list3.append(num)

    return list3

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
print("result List is", mergeList(list1, list2))