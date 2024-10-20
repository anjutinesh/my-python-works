#Find the length of last word
Sentence = "anju surendran"
Count = 0  
Length = len(Sentence)  
while Length > 0:
        Length =Length - 1 
            
        if Sentence[Length] != ' ':
            Count =Count+ 1  
        else:
            if Count > 0:
                break

print(f"Length of the last word: {Count}") 