import random
current_word = ("b","l","u","e") # TIP: the number of letters should match the word

guesses = []
maxfails = 4
fails = 0

while fails < maxfails:
    guess = input("Guess a letter:")
    fails += 1


    if guess == "b":
        guesses.extend(guess)
        print(guesses)
        print("correct")
        print("You have "+str(maxfails - fails) + " tries left!")
    elif guess == 
        print ("wrong")
        print("You have "+str(maxfails - fails) + " tries left!")



    if guess == "l":
        guesses.extend(guess)
        print(guesses)
        print("correct")



    if guess == "u":
        guesses.extend(guess)
        print(guesses)
        print("correct")



    if guess == "e":
        guesses.extend(guess)
        print(guesses)
        print("correct")








	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!


    #fails+=1
    #print("You have " + str(maxfails - fails) + " tries left!")
