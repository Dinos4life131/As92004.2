import random

def print_rounds_function():
    '''Ask user how many rounds, if infinite the program can handle that'''
    while True:
        # Prompt user for number of rounds
        number_of_rounds = input("Enter the number of rounds you want to play (press Enter for infinite): ")
        
        if number_of_rounds == "":
            # Handle infinite rounds
            infinite_rounds = True
            num_rounds = None  # Set num_rounds to None because it's infinite
            print("\nInfinite rounds it is!")
            print("If you want to end the quiz write 'End'\n")
            break
        elif number_of_rounds.isdigit() and int(number_of_rounds) > 0:
            # Handle finite rounds
            num_rounds = int(number_of_rounds)
            infinite_rounds = False
            print(f"{num_rounds} rounds it is!")
            break
        else:
            # Handle invalid input
            print("Invalid input! Please enter a positive number or press Enter for infinite rounds.")
    
    return infinite_rounds, num_rounds

def select_topic():
    '''Allows user to choose their topic.'''
    # Available topics to choose from
    topics = {
        1: "Multiplication",
        2: "Addition",
        3: "Subtraction"
    }
    
    # Display the list of topics
    print("Please choose a topic from the following list:")
    for key, value in topics.items():
        print(f"{key}: {value}")
    
    while True:
        try:
            # Ask the user to enter their chosen topic number
            topic_choice = int(input("Enter the number next to your chosen topic: "))
            if topic_choice in topics:
                topic_name = topics[topic_choice]
                return topic_choice, topic_name
            else:
                # Handle invalid topic choice
                print("Invalid choice! Please choose a valid topic number.")
        except ValueError:
            # Handle non-integer input
            print("Invalid input! Please enter a number.")

def generate_questions(topic, num_questions):
    '''Generate questions based on the chosen topic and number of questions.'''
    questions = []
    for _ in range(num_questions):
        if topic == 1:  # Multiplication
            num3 = random.randint(1, 10)    # Generate random numbers for multiplication
            num4 = random.randint(1, 10)    # Ensure non-negative numbers for multiplication
            question = f"What is {num3} * {num4}?"
            answer = num3 * num4
        elif topic == 2:  # Addition
            num1 = random.randint(0, 100)   # Generate random numbers for addition
            num2 = random.randint(0, 100)   # Ensure non-negative numbers for addition
            question = f"What is {num1} + {num2}?"
            answer = num1 + num2
        elif topic == 3:  # Subtraction
            num1 = random.randint(0, 100)   # Generate random numbers for subtraction
            num2 = random.randint(0, 100)   # Ensure non-negative result for subtraction
            if num1 < num2:
                num1, num2 = num2, num1  # Swap if necessary to ensure non-negative result
            question = f"What is {num1} - {num2}?"
            answer = num1 - num2
        questions.append((question, answer))
    return questions

def answer_questions(infinite_rounds, num_rounds, topic_choice):
    '''Administers the quiz, tracks user's responses, and provides feedback.'''
    correct_count = 0
    wrong_answers = []
    unanswered_questions = []
    all_answers = []
    invalid_questions_count = 0
    round_counter = 0
    
    while infinite_rounds or (num_rounds is not None and round_counter < num_rounds):
        questions = generate_questions(topic_choice, 1)
        
        for i, (question, answer) in enumerate(questions):
            print(f"Question {round_counter + 1}:\n{question}")
            invalid_attempts = 0
            
            while invalid_attempts < 2:
                try:
                    user_input = input("Your answer: ").strip()
                    
                    if user_input.lower() == "end":
                        # Handle quiz termination for infinite rounds
                        infinite_rounds = False
                        num_rounds = round_counter  # Ensure loop termination
                        break
                    elif user_input == "":
                        user_input = "not answered"
                    elif not user_input.isdigit() and user_input != "not answered":
                        raise ValueError("Invalid input! Please enter a positive number.")
                    
                    user_answer = int(user_input) if user_input.isdigit() else user_input
                    
                    if user_input == "not answered":
                        unanswered_questions.append((question, user_input, answer))
                        print("You chose not to answer this question.\n")
                    elif user_answer == answer:
                        print("Correct!\n")
                        correct_count += 1
                    else:
                        print(f"Wrong! The correct answer is {answer}.\n")
                        wrong_answers.append((question, user_answer, answer))
                    
                    all_answers.append((question, user_answer, answer))
                    break  # Exit input validation loop upon valid input
                except ValueError as ve:
                    print(ve)
                    invalid_attempts += 1
                    
                    if invalid_attempts == 2:
                        print("You did not provide a valid answer. This question will not count towards your percentage.")
                        invalid_questions_count += 1
                        unanswered_questions.append((question, "invalid", answer))
                        all_answers.append((question, "invalid", answer))
        
        round_counter += 1
        
        if not infinite_rounds and round_counter >= num_rounds:
            break
    
    return correct_count, wrong_answers, unanswered_questions, invalid_questions_count, all_answers

def review_history(all_answers):
    '''Displays a review of all questions asked and user responses.'''
    print("\nHere is the full history of your answers:\n")
    for i, (question, user_answer, correct_answer) in enumerate(all_answers):
        if user_answer == "invalid":
            print(f"{i + 1}. {question} \nYour answer: INVALID \nCorrect answer: {correct_answer}\n")
        elif user_answer == "not answered":
            print(f"{i + 1}. {question} \nYour answer: NOT ANSWERED \nCorrect answer: {correct_answer}\n")
        else:
            print(f"{i + 1}. {question} \nYour answer: {user_answer} \nCorrect answer: {correct_answer}\n")

def review_wrong_answers(wrong_answers, unanswered_questions, all_answers):
    '''Allows user to review questions they answered incorrectly or left unanswered.'''
    if wrong_answers or unanswered_questions:
        while True:
            try:
                print("You have some wrong answers and unanswered questions. Do you want to review them? (yes/no)")
                review = input().strip().lower()
                if review.startswith("y"):
                    print("\nHere are the questions you got wrong and unanswered questions:\n")
                    for i, (question, user_answer, correct_answer) in enumerate(wrong_answers + unanswered_questions):
                        print(f"{i + 1}. {question} \nYour answer: {user_answer} \nCorrect answer: {correct_answer}\n")
                    break
                elif review.startswith("n"):
                    break
                else:
                    raise ValueError("Invalid input! Please enter Yes or No.")
            except ValueError as ve:
                print(ve)
    
    while True:
        try:
            print("\nDo you want to see the full history of your answers? (yes/no)")
            view_history = input().strip().lower()
            if view_history.startswith("y"):
                review_history(all_answers)
                break
            elif view_history.startswith("n"):
                break
            else:
                raise ValueError("Invalid input! Please enter Yes or No.")
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    '''Main entry point of the math quiz program.'''
    while True:
        print("Welcome to the math quiz.\nPlease follow the instructions provided.\nGood luck 😉")
        
        # Determine number of rounds to play
        infinite_rounds, num_rounds = print_rounds_function()
        
        # Choose a topic for the quiz
        topic_choice, topic_name = select_topic()
        print(f"Selected topic: {topic_name}")
        print(f"You have selected {num_rounds if num_rounds is not None else 'infinite'} round(s) of {topic_name}")
        
        # Answer questions based on user's choices
        correct_count, wrong_answers, unanswered_questions, invalid_questions_count, all_answers = answer_questions(infinite_rounds, num_rounds, topic_choice)
        
        # Calculate total valid questions answered
        total_valid_questions = correct_count + len(wrong_answers) + len(unanswered_questions) - invalid_questions_count
        print(f"You answered {correct_count} out of {total_valid_questions} valid questions correctly.")
        
        # Calculate and display percentage of correct answers
        if total_valid_questions > 0:
            percentage_correct = (correct_count / total_valid_questions) * 100
            rounded_percentage = round(percentage_correct)
            print(f"You got {rounded_percentage}% correct!\n")
        
        # Review wrong answers and unanswered questions
        review_wrong_answers(wrong_answers, unanswered_questions, all_answers)
        
        # Ask if the user wants to play again
        while True:
            play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again_input.startswith("y"):
                break
            elif play_again_input.startswith("n"):
                break
            else:
                print("Invalid input! Please enter Yes or No.")
        
        # Exit the loop if user chooses not to play again
        if play_again_input.startswith("n"):
            break

    # End of program message
    print("\nThank you for playing!\nWe hope you had fun and learned something new.\nSee you next time!")




#to add, invaild gives1 mroe chance, the first invail does nto count rtoward score.--- done
#- counts as invaid and another chance. --- done
#comment on every def and loop
#clarify invaild inputs do not count towards final score --- done



''' 
Need help---
it says the user only did 5 question even if it was 3 etc
the invailds are counting 2x even if they shouldnt be counting once.
ie 3 questions selected, put it is then saying 3 of 7 correct
the first invaild try is counting towards socre (percentage) how i think its working
skipped questions aka enter is sometimes working towards score and sometimes not- sometimes they count and sometimes not
'''



#add unexpected for seeing full history === done
#round answer to nearest full number === done
