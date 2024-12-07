def play_quiz():
    print("Hey, welcome to my Tech CEO Quiz game! Hope you know your stuff 😀")

    #Input Validation
    playing = input("Do you want to play. Yes or No: ").lower()
    while playing not in ['yes', 'no']:
        playing = input("Invalid input. Please type Yes or No: ").lower()

    if playing != "yes":
        return
    
    #Questions
    print ("Okay! Lets Play: ")
    print ("For every answer you give, you get one point, try to get as many as you can")
    score= 0

    input("Press Enter to continue to the next question...")  # Pause before the next question
    answer = input("What is the full name of Google's CEO? ").strip().lower() 
    if answer == "sundar pichai":
        print("Correct")
        score +=1 #equivalent to: score= score + 1
    else: 
        print("Incorrect!")
    input("Press Enter to continue to the next question...")
    answer = input("What is the full name of Apple's CEO? ").strip().lower() 
    if answer == "tim cook":
        print("Correct")
        score +=1
    else: 
        print("Incorrect!")
    input("Press Enter to continue to the next question...")
    answer = input("What is the full name of Amazon's CEO? ").strip().lower() 
    if answer== "andy jassy":
        print("Correct")
        score +=1
    else: 
        print("Incorrect!")
    input("Press Enter to continue to the next question...")
    answer = input("What is the full name of Microsoft's CEO? ").strip().lower()
    if answer == "satya nadella":
        print("Correct")
        score +=1
    else: 
        print("Incorrect!")
    input("Press Enter to continue to the next question...")
    answer = input("What is the full name of Nvidia's CEO? ").strip().lower()
    if answer == "jensen huang":
        print("Correct")
        score +=1
    else: 
        print("Incorrect!")

    #Display Final Code
    print(f"You answered : {score} Questions correctly")
    print(f"You got : {(score/5)*100}%.")
    
    #Final Feedback
    if score == 5:
        print("Amazing! you got all the questions correct!")
    elif score >=3:
        print("Good job!")
    else:
        print("Better luck next time!")

    print("Thank you so much for playing! ")

while True:
    play_quiz()
    replay = input("Do you want to play again: Yes or No? ").strip().lower()  # Added a space after the question mark
    while replay not in ["yes", "no"]:
        replay = input("Invalid input. Do you want to play again: Yes or No? ").strip().lower()
    if replay != "yes":  # You don't need to call `replay.lower()` again as it's already lowercased
        print("Thank you so much for playing!")
        break 