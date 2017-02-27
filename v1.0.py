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
    with open('wordbank.txt', 'r') as file:
        #Open the file containing word-bank
        for x in map(str.upper, map(str.strip, file.readlines())):
            #loop over the stripped down words
            if len(x) == num:
                acceptedWord.append(x)
                 #If length of word is equal to random choice from suitable lengths, add it to a list.
    
    #Random index from total number of items in list.
    answers  = random.sample(acceptedWord, num)
    #picks a selection of the available words. Amount of words = word length.
    trueWord = answers[random.randint(0, len(answers)-1)]
    #trueWord = answer. Random item of the shortlisted avaliable words
    print('\n'.join(answers))
    #Prints hints.
    game(trueWord)


def game(trueWord):
    for x in range(0,5):
        #The user has 5 guesses
        print("Guesses Left: ", 5-x)
        userInput = input("Guess: ").upper()
        #All guesses/inputs are parsed to uppercase.
        userList = list(userInput)
        #List of the letters the user inputed
        trueList = list(trueWord)
        #List of letter of 
        if userInput == trueWord:
            print("Well done, you guessed correctly")
            getWords()
            #If the user enters the correct word, quit the program
        correctGuess = 0
        for item in list(userList):
            #for each letter the user inputed
            if item == trueList[userList.index(item)]:
                #if the letter is in the same position as the answer
                correctGuess += 1
                #increment the correct amount of letters by 1
        print(correctGuess, "out of ", len(trueList), "correct.")
    print("Bad luck! The answer was: ", trueWord)
    getWords()

getWords()














        
        
