#find the index of peak element

ListOfElements = [12, 45, 7, 23, 1, 89, 341]
MaxValue = ListOfElements[0]
MaxIndex = 0
for i in range(1, len(ListOfElements)):
    if ListOfElements[i] > MaxValue:
        MaxValue = ListOfElements[i]
        MaxIndex = i
print("peak element index",MaxIndex)