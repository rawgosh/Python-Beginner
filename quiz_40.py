#quiz game

def new_game(): #function for a new game
    guesses = [] #to store the guessed answers
    correct = 0 #to calculate the marks obtained
    q_num = 1

    for key in questions: 
        print(key) #prints the key of the dictionatry variable (questions)
        for i in answers[q_num-1]:
            print(i) #displays option in the terminal, "i" is just a variable we can keep any thing.
        q_num += 1
        print()
        guess = input("Enter your choice (A, B, C or D) :") #asking user to choose an option.
        guess = guess.upper() #changes the choice into upper case
        guesses.append(guess) #adds the choice to the list `guesses`
        correct += check_answer(questions.get(key),guess) #calculates the total sum the `check_answer` function returns
    
    
    display_score(correct,guesses) #calls the function to display the answers

def check_answer(ans,guess): #function to check answer
    if ans == guess:
        print("CORRECT!")
        return 1 #this value gets added to the `correct` variable
    else:
        print("WRONG!")
        return 0

def display_score(correct,guesses): #function to display the score
    print()
    print()

    print("RESULTS")
    print("Answers: ",end = "")
    for value in questions: #loops until the value in question is present
        print(questions.get(value), end=" ") #displays the correct answers
    print()
    print("Guesses: ",end = "")
    for i in guesses:
        print(i, end = " ") #displays the answer guessed by the user
    print()
    print()
    score = int((correct /len(questions))*100) #calculating the percentage of the  score
    print("Your score is: "+str(score)+"%")

def play_again(): #function to play again
    print()
    play_again = input("Wanna play again? Y/YES or N/NO :").lower() #asks user to play again
    if play_again == "yes" or play_again =="y":
        return True #returns the boolean value to the function
    else:
        return False

questions = {"1) In 1768, Captain James Cook set out to explore which ocean?":"A","2) What is actually electricity?":"C","3) Which of the following is not an international organisation?":"D","4) Which of the following disorders is the fear of being alone?":"A","5) What was the first country to use tanks in combat during World War I?":"C","6) What is the main component of the sun?":"B","7) What is the speed of sound?":"B"}

answers = [["A. Pacific Ocean","B. Atlantic Ocean","C. Indian Ocean","D. Arctic Ocean"],["A. A flow of water","B. A flow of air","C. A flow of electrons","D. A flow of atoms"],["A. FIFA","B. NATO","C. ASEAN","D. FBI"],["A. Agoraphobia","B. Aerophobia","C. Acrophobia","D. Arachnophobia"],["A. France","B. Japan","C. Britain","D. Germany"],["A. Liquid lava","B. Gas","C. Molten iron","D. Rock"],["A. 120 km/h","B. 1,200 km/h","C. 400 km/h","D. 700 km/h"]]

print()
print()
print("***CHOOSE THE CORRECT OPTION***")
print()
new_game()
while play_again(): #calls the function and gets the returned value
    print()
    new_game()
    print()
    print()

print("See yaa!")


