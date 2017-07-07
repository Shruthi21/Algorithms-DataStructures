import random


#set initial values
player1points= 0
ai= 0
userCorrectLetters= ''
aiCorrectLetters=''
wrongLetters=''
wrongPlace= ''
correctLetters = ''
notInWord = ''
endGame = False
allLetters = set(list('abcdefghijklmnopqrstuvwxyz'))
alreadyGuessed = set() 
userGuessPosition = 0
availLetters = allLetters.difference(alreadyGuessed)


#import wordlist, create mask
with open('wordlist.txt') as wordList:
    secretWord = random.choice(wordList.readlines()).strip()
print (secretWord)
secretWordLength = len(secretWord)








def displayGame():
    mask = '_'  * len(secretWord)
    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            mask = mask[:i] + secretWord[i] + mask [i+1:]
    for letter in mask:
        print (letter, end='')
    print (' ')
    print ('letters in word but not in correct location:', wrongPlace)
    print ('letters not in word:', wrongLetters)



    ##asks the user for a guess, assigns input to variable

def getUserGuess(alreadyGuessed):


    while True:
        print ('enter your letter')
        userGuess = input ()
        userGuess= userGuess.lower()
        if len(userGuess) != 1:
            print ('please enter only one letter')
        elif userGuess in alreadyGuessed:
            print ('that letter has already been guessed. try again')
        elif userGuess not in 'abcdefjhijklmnopqrstuvwxyz':
            print ('only letters are acceptable guesses. try again.')
        else:
            return userGuess

def newGame():
    print ('yay. that was great. do you want to play again? answer yes or no.')
    return input().lower().startswith('y')


userTurn=True     
while userTurn == True:
    displayGame ()
    print ('which character place would you like to guess. Enter number?')
    userGuessPosition = int(input())

    slice1 = userGuessPosition - 1  


    ##player types in letter
    guess = getUserGuess(wrongLetters + correctLetters)
    if guess== (secretWord[slice1:userGuessPosition]):
        correctLetters = correctLetters + guess
        print ('you got it right! ')
        displayGame()
        break
    elif guess in secretWord:
            wrongPlace = wrongPlace + guess 
            print ('that letter is in the word, but not in that position')
            displayGame()
            break
    else:
            wrongLetters = wrongLetters + guess
            print ('nope. that letter is not in the word')
            displayGame()
            break

print ("it's the computers turn")

aiTurn=True

while aiTurn == True:
    aiGuessPosition = random.randint(1, secretWordLength)
    print (aiGuessPosition)

    aiGuess=random.sample(availLetters, 1)
    print ('the computer has guessed', aiGuess, "in position", + aiGuessPosition)
    if str(aiGuess) == (secretWord[slice1:userGuessPosition]):
            correctLetters = correctLetters + guess
            print ('this letter is correct ')
            break
    elif str(aiGuess) in secretWord:
            aiCorrectLetters = aiCorrectLetters + guess 
            correctLetters = correctLetters + guess
            print ('that letter is in the word, but not in that position')
            break
    else:
            wrongLetters = wrongLetters + guess
            print ('that letter is not in the word')
            break   


    displayGame() 
    break 
