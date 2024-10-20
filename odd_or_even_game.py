#Odd or even game
def OddOrEven(Group1, Group2):
    TeamAsum = 0
    TeamBsum=0
    TotalSum=0

    for i in Group1:
     TeamAsum =TeamAsum+ i  
    print("The sum of the elements in the array is:", TeamAsum)
    for j in Group2:
     TeamBsum = j  
    print("The sum of the elements in the array is:", TeamBsum)

    TotalSum=TeamAsum + TeamBsum
    print(TotalSum,"TotalSum")
    if  TotalSum % 2 == 0:
       return "Team A wins"
    else:
       return "Team B wins"
    
    
Group1 = []
n = int(input("Enter the number of elements you want to input for Group1: "))

for k in range(n):
    num = int(input(f"Enter number {k + 1}: "))
    Group1.append(num)


print("The array of numbers is:", Group1)
Group2 = []
n1 = int(input("Enter the number of elements you want to input for Group2: "))

for m in range(n1):
    num1 = int(input(f"Enter number {m + 1}: "))
    Group2.append(num1)


print("The array of numbers is:", Group2)

print(OddOrEven(Group1, Group2))