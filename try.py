import random

def print_rounds_function():
    '''Prompt the user to enter the number of rounds and handle infinite rounds if desired.'''
    while True:
        number_of_rounds = input("Enter the number of rounds you want to play (press Enter for infinite): ")
        
        if number_of_rounds == "":
            infinite_rounds = True
            num_rounds = 'infinite'  # Set num_rounds to None since it's infinite
            print("Infinite rounds it is!")
            break
        elif number_of_rounds.isdigit():
            num_rounds = int(number_of_rounds)
            infinite_rounds = False
            print(f"{num_rounds} rounds it is!")
            break
        else:
            print("Invalid input! Please enter a valid number or press Enter for infinite rounds.")
    
    return infinite_rounds, num_rounds

def select_topic():
    '''Function to let the user choose a topic from predefined topics.'''
    topics = {
        1: "Multiplication",
        2: "Addition",
        3: "Subtraction"
    }
    
    print("Please choose a topic from the following list:")
    for key, value in topics.items():
        print(f"{key}: {value}")
    
    while True:
        try:
            topic_choice = int(input("Enter the number corresponding to your chosen topic: "))
            if topic_choice in topics:
                topic_name = topics[topic_choice]
                return topic_choice, topic_name
            else:
                print("Invalid choice! Please choose a valid topic number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def generate_questions(topic, num_questions):
    questions = []
    for _ in range(num_questions):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 10)
        num4 = random.randint(1, 10)
        if topic == 1:  # Multiplication
            question = f"What is {num3} * {num4}?"
            answer = num3 * num4
        elif topic == 2:  # Addition
            question = f"What is {num1} + {num2}?"
            answer = num1 + num2
        elif topic == 3:  # Subtraction
            question = f"What is {num1} - {num2}?"
            answer = num1 - num2
        questions.append((question, answer))
    return questions
    #code that generates random questions, thus not allowing users to memorize questions.
    #fixed it so its only 1-10 times tables

def review_wrong_answers(wrong_answers):
    while True:
        try:
            print("You have some wrong answers. Do you want to review them? (yes/no)")
            review = input().strip().lower()
            review_first_letter = review[0]

            if review_first_letter == "y":
                print("\nHere are the questions you got wrong:")
                for i, (question, user_answer, correct_answer) in enumerate(wrong_answers):
                    print(f"{i + 1}. {question} \nYour answer: {user_answer} \nCorrect answer: {correct_answer}")
                break  # Exit the loop if the user wants to review
            elif review_first_letter == "n":
                print("Great job! You got all the questions correct!")
                break  # Exit the loop if the user doesn't want to review
            else:
                print("Invalid input! Please enter Yes or No.")
        except ValueError:
            print("Invalid input! Please enter Yes or No.")



if __name__ == "__main__":
    infinite_rounds, num_rounds = print_rounds_function()
    topic_choice, topic_name = select_topic()
    print(f"Selected topic: {topic_name}")
    #print(f"Infinite rounds: {infinite_rounds}, Number of rounds: {num_rounds}")
    print(f"You have selected {num_rounds} round of {topic_name}")

    correct_count = 0
    wrong_answers = []
    round_counter = 0

        #This counts how many rounds has been done, each time a quesiton is answered it goes up by 1
    while infinite_rounds or round_counter < num_rounds:
        questions = generate_questions(topic_choice, 1)
        for i, (question, answer) in enumerate(questions):
            print(f"Question {round_counter + 1}:\n{question}")
            #Prints the question and question number. 
        try:    
            user_answer = int(input("Your answer: "))
            if user_answer == 'answer':
                print("Correct!\n")
                correct_count += 1
            else:
                print("Wrong!\n")    
                wrong_answers.append((question, user_answer, answer))
        except ValueError:
            print(f"Invalid input! The correct answer is {answer}.\n")
        
        round_counter += 1
        if not infinite_rounds and round_counter >= num_rounds:
            break

    print(f"You answered {correct_count} out of {round_counter} questions correctly.\n")

    if correct_count != round_counter:
        review_wrong_answers(wrong_answers)
    else:
        print("Well done you got them all correct")

    