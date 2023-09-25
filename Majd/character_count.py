from typing import List
def character_count(word: str) -> str:
    
    word = sorted(word.lower())
    count = 1 
    output = ""

    for indx in range(len(word)):
        if indx != len(word)-1 and word[indx] == word[indx+1]:
            count += 1
        else:
            output += word[indx] + str(count)
            count = 1

    return output