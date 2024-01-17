# Import libraries including set of english words
from time import monotonic
import numpy as np 
import pandas as pd 

# Begin the timer 
start = monotonic()

# Create a set of all english words
lowerset = pd.read_table('words_alpha.txt', header=None, delimiter=None)[0].to_list()

# Create a list containing all five letter words from the set
uniques0 = []
for word in lowerset:
    if type(word) == str:
        if len(word) == 5:
            uniques0.append(word)


# Define words in the english alphabet which will be used to detect words with repeated letters
letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z'}

# Detect words with repeated letters and remove them
repeats = []
for word in uniques0:
    for letter in letters:
        if word.count(letter) > 1:
            repeats.append(word)

for word in set(repeats):
    uniques0.remove(word)

# Main program
unique_word_sets = []

word_x = 0      # Creates a counter which keeps track of the index of the current word
for word in uniques0:       
    uniques1 = []
    for following_word in range(word_x + 1, len(uniques0)):     # Loops over the words in the list following the current word
        unique_letters = True                                       # Detects if the current word shares any letter with the following word
        for letter in uniques0[following_word]:
            if letter in word:
                unique_letters = False
        if unique_letters:      # Apppends unique words as a list to procede the the nex tinstance of this function
            uniques1.append(uniques0[following_word])
    
    # The following three paragraphs are recursive off the previous
    word2_x = 0
    for word2 in uniques1:
        uniques2 = []
        for following_word in range(word2_x + 1, len(uniques1)):
            unique_letters = True
            for letter in uniques1[following_word]:
                if letter in word2:
                    unique_letters = False
            if unique_letters:
                uniques2.append(uniques1[following_word])
        

        word3_x = 0
        for word3 in uniques2:
            uniques3 = []
            for following_word in range(word3_x + 1, len(uniques2)):
                unique_letters = True
                for letter in uniques2[following_word]:
                    if letter in word3:
                        unique_letters = False
                if unique_letters:
                    uniques3.append(uniques2[following_word])


            word4_x = 0
            for word4 in uniques3:
                uniques4 = []
                for following_word in range(word4_x + 1, len(uniques3)):
                    unique_letters = True
                    for letter in uniques3[following_word]:
                        if letter in word4:
                            unique_letters = False
                    if unique_letters:
                        uniques4.append(uniques3[following_word])

                for word5 in uniques4:
                    unique_word_sets.append((word, word2, word3, word4, word5))

                word4_x += 1
            word3_x += 1
        word2_x += 1
    word_x += 1           
    print(f'{word_x}/{len(uniques0)} words completed')

print(unique_word_sets)
print('\nThis code ran in ' + str(round(monotonic() - start, 3)) + ' seconds')