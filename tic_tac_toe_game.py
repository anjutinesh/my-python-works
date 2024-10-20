#Tictactoe Game

sheet = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def PrintPattern():
    row1 = (sheet[0] +' | '+ sheet[1] +' | ' + sheet[2])
    row2 = (sheet[3] +' | '+ sheet[4] +' | ' + sheet[5])
    row3 = (sheet[6] +' | '+ sheet[7] +' | ' + sheet[8])

 
    print(row1)
    print('---------')
    print(row2)
    print('----------')
    print(row3)


def InsertOption(option):
    if option == 'X':
        number = 1
    elif option == 'O':
        number = 2

    print("player",number,"can enter")

    choice = int(input("Enter your option (0-8)"))
    if sheet[choice] == ' ':
        sheet[choice] = option
    else:
        
        print("it is already filled")

def CheckResult(option):
    if (sheet[0] == option and sheet[1] == option and sheet[2] == option) or (sheet[3] == option and sheet[4] == option and sheet[5] == option) or (sheet[6] == option and sheet[7] == option and sheet[8] == option) or (sheet[0] == option and sheet[3] == option and sheet[6] == option) or (sheet[1] == option and sheet[4] == option and sheet[7] == option) or (sheet[2] == option and sheet[5] == option and sheet[8] == option) or (sheet[0] == option and sheet[4] == option and sheet[8] == option) or (sheet[2] == option and sheet[4] == option and sheet[6] == option):
        return True
    else:
        return False

while True:
    PrintPattern()
    InsertOption('X')
    PrintPattern()
    if CheckResult('X'):
        print("Player 1 wins")
        break
    InsertOption('O')
    if CheckResult('O'):
        PrintPattern()
        print("Player 2 wins")
        break