# Problem 5 - Playing a Hand
# 10/10 points (graded)
# In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in
# writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start
# coding your solution.

# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

# Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game.

 
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:
 
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
 
      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculateHandLen(hand) > 0:
        # Display the hand
        print('Current Hand: ', displayHand(hand))
        # Ask user for input
        guess = str(input("Enter the word using letters in your hand: ")
        # If the input is ".":
        if guess == ".":
            # End the game (break out of the loop)
            break 
        # Otherwise (the input is not "."):
        else:
            # If the word is valid:
            if isValidWord(guess, hand, wordList) == True:
                # Tell the user how many points the word earned,
                # and the updated total score
                total_score = getWordScore(guess,n)
                print('"'+ guess +'"', "earned", getWordScore(guess, n), "points. Total: ", total_score, "points", '\n')
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('Invalid word, please try again.', '\n')
            # update the user's hand by removing the letters of their inputted word
            hand = updateHand(hand, guess) 

    # Game is over (user entered '.' or ran out of letters),
    # so tell user the total score
    if guess == '.':
        print('Your final score: ', total_score)
    else:
        print('You ran out of letters. Your final score: ', total_score)  
