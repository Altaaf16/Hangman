import random 

print("Welcome to Hangman")
print("-----------------------------------------------")


#list that contains some words that can be used for the game
Worddictionary =["Mauritius","France","England","Italy"]

#choose from random 
randomWord = random.choice(Worddictionary)

#The for loop prints underscores for each letter in the randomWord variable to represent the hidden letters of the word.
for x in randomWord:
    print("_", end=" ")

#To print the hangman drawing based on the number of wrong guesses.
def print_hangman(wrong):
    if (wrong ==0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong ==1):
        print("\n+---+")
        print("O    |")
        print("     |")
        print("     |")
        print("    ===") 
    elif(wrong ==2):
        print("\n+---+")
        print("O    |")
        print("|    |")
        print("     |")
        print("    ===")
    elif(wrong ==3):
        print("\n+---+")
        print(" O    |")
        print("/|    |")
        print("      |")
        print("     ===")
    elif(wrong ==4): 
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("     ===")
    elif(wrong ==5): 
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif(wrong ==6):  
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===") 

#Takes a list of guessed letters and prints the word with the guessed letters revealed and the unguessed letters hidden.             
def prinword(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter],end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters

#To clear the previous line and print a new one for the hangman drawing.
def printLines():
    print("\r")
    for char in randomWord:
     print("\u203E",end=" ")

#length_of_word_to_guess stores the length of the word to be guessed
#amount_of_times_worng stores the number of times the user has guessed the wrong letter
#current_guess_index stores the index of the current letter being guessed.
#current_letters_guessed is a list that stores all the letters guessed so far.
#current_Letters_right stores the number of letters that have been guessed correctly so far.
length_of_word_to_guess=len(randomWord)
amount_of_times_worng =0
current_guess_index=0
current_letters_guessed=[]
current_Letters_right=0

#The while loop runs until either the user has guessed the word or they have run out of guesses
while(amount_of_times_worng !=6 and current_Letters_right != length_of_word_to_guess):
    print("/nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter,end=" ")
    #prompt used for input 
    letterGuessed = input("\nGuess a letter: ")
    #user is right 
    if(randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_worng)
        #print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_Letters_right= prinword(current_letters_guessed)
        printLines()
    
    #user was wrong 
    else:
        amount_of_times_worng+=1
        current_letters_guessed.append(letterGuessed)
        #update the drawing 
        print_hangman(amount_of_times_worng)
        #print word
        current_Letters_right= prinword(current_letters_guessed)
        printLines()
        
#Once the while loop ends, the game is over and a message is printed    
print("Game is over")
