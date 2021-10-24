# Python Challenge - MSP (ENGR4)
# Justyn Reyes
# 10.14.21

def hangman(miss): # creates hangman as misses increase
    if miss == 0:
        print("  ---  \n"
              "    |  \n")
        
    if miss == 1:
        print("  ---  \n"
              "    |  \n"
              "    0  \n")
    
    if miss == 2:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /   \n")
       
    if miss == 3:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|  \n")
        
    if miss == 4:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n")
    if miss == 5:
         print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n")
    if miss == 6:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n"
              "   /   \n")
    if miss == 7:
        print("  ---  \n"
              "    |  \n"
              "    0  \n"
              "   /|\\\n"
              "    |  \n"
              "   / \\\n")

        
guessAgain = "yes"   # enables continuous guesses
correct = "" # makes correct a variable
wrong = "" # makes wrong a variable 
miss = 0 # missed guesses starts at 0
word = input(str("Player 1, enter word:")) # input for key word
print("\n" * 50) # clears screen by adding 50 blank lines

hangman(miss) # prints hangman
blanks = "-" * len(word) # makes dashes for letters in word (lines that go under the word/length of word)
print(blanks) # prints blank.
def check(word, correct, blanks): # replaces blanks with letters
    for i in range(len(word)): # position of letter in number mode for the range of number for the letters
        if word[i] in correct: # letter guessed in word...
            blanks = blanks[:i] + word[i] + blanks[i + 1:] 
            # go to position of letter and replace that letter. 
            # move to next position
    print(blanks) # prints blanks
            
while guessAgain != "x": # keep guessing
    guess = input("Player 2, enter guess:") # input for guess
    if guess in word: # checks word for entered guess, if correct...
        print("correct!") # print correct
        correct = correct + guess # store guess in correct guesses section
    else: # if incorrect...
        print("letter not in word") # print letter not in word
        miss = miss + 1 # add one number to guesses wrong
        wrong = wrong + guess # store guess in wrong guesses
        print(wrong) # print missed guesses
    if miss >= 7: # if there are more than 7 wrong answers, the hangman is made
        guessAgain = "x" # exit out of loop
        print("you lost :(") # prints you lost
        
    hangman(miss) # calls function to print hangman according to miss number
    check(word, correct, blanks) # calls function to replace blanks with correct guesses
