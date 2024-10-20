#HANGMAN_GAME

FilmName =  "titanic"
FilmLetterCount = int(input("how many letters for the film"))
GuessedList=[]
Chances=8
for i in range (FilmLetterCount):
    GuessedList.append('_')
print(GuessedList)

while Chances>0:
  
    Letter = input("Enter guessed Letter")
    if Letter in FilmName:
        print(f'player has choose the Letter {Letter}')
        for i in range (len(FilmName)):
            if FilmName[i]==Letter:
                GuessedList[i]= Letter     
        print(GuessedList)

    else:
        Chances = Chances-1
        print(f'you lose,{Chances} more Chances left')
    if '_' not in GuessedList:
       print('Success. FilmName is', GuessedList)
       exit()
     
print('failed to guess the film name. The FilmName is ',FilmName)    
