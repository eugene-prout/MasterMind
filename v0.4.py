import random

difficulty = {1: [4, 5, 6], 2: [7, 8],
              3: [9, 10, 11], 4: [12, 13],
              5: [14, 15]
              }
#Keys are the various word lengths for each difficulty (1-5).

acceptedWord = []
#Start a blank list, used in getWords()

def getWords():
    while True:
        try:
            level = int(input("What difficulty would you like? (1,2,3,4,5) "))
            break
        except (ValueError, KeyError):
            print("That is not a number")
    #Take a numerical input from the user, attempt to parse it, if it fails, carry on the loop.
    
    num = random.choice(difficulty[level])
    #num (used to store word lengths) is a random choice from the available lengths for the selected difficulty.
    
    with open('enable1.txt', 'r') as file:
        #Open the file containing word-bank
        for x in map(str.strip, file.readlines()):
            #loop over the stripped down words
            if len(x) == num:
                acceptedWord.append(x)
                #If length of word is equal to random choice from suitable lengths, add it to a list.
    indexValue = random.randint(0, len(acceptedWord)-1)
    #Random index from total number of items in list.
    return acceptedWord[indexValue]
    #Returns random index'ed value from suitable length words.


print(getWords())
