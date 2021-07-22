#Exercise: guess my number
#10/10 points (graded)
#ESTIMATED TIME TO COMPLETE: 15 minutes

#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

#Here is a transcript of an example session:

#Please think of a number between 0 and 100!
#Is your secret number 50?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
#Is your secret number 75?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
#Is your secret number 87?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
#Is your secret number 81?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
#Is your secret number 84?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
#Is your secret number 82?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
#Is your secret number 83?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
#Game over. Your secret number was: 83

###
print("Please think of a number between 0 and 100!")
high = 100
low = 0
while True:
    guess = (high+low)//2
    print("Is your secret number " + str(guess) + " ?")
    text = input("Enter 'h' to indicate the guess is to too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if text == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    elif text == 'l':
        low = guess
    elif text == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')
