import random

def print_rounds_function():
    '''Ask user how many rounds, if infinite the program can handle that'''
    while True:
        number_of_rounds = input("Enter the number of rounds you want to play (press Enter for infinite): ")
        
        if number_of_rounds == "":
            infinite_rounds = True
            num_rounds = 'infinite'  # Set num_rounds to None cos it's infinite
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
    '''Allows user to choose their topic.'''
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
            topic_choice = int(input("Enter the number next to your chosen topic: "))
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
        num1 = random.randint(0, 100)   # Addition & Subtraction
        num2 = random.randint(0, 100)   # Addition & Subtraction
        num3 = random.randint(0, 10)    # Multiplication
        num4 = random.randint(0, 10)    # Multiplication
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

def review_wrong_answers(wrong_answers):
    if wrong_answers:
        try:
            print("You have some wrong answers. Do you want to review them? (yes/no)")
            review = input().strip().lower()
            review_first_letter = review[0]

            if review_first_letter == "y":
                print("\nHere are the questions you got wrong:\n")
                for i, (question, user_answer, correct_answer) in enumerate(wrong_answers):
                    print(f"{i + 1}. {question} \nYour answer: {user_answer} \nCorrect answer: {correct_answer}\n")

        except ValueError:
            print("Invalid input! Please enter Yes or No.")
    else:
        print("Great job! You got all the questions correct!")

if __name__ == "__main__":
    play_again = True

    while play_again:
        print("Welcome to the math quiz.\nPlease follow the instructions provided.\nGood luck 😉")
        infinite_rounds, num_rounds = print_rounds_function()
        topic_choice, topic_name = select_topic()
        print(f"Selected topic: {topic_name}")
        print(f"You have selected {num_rounds} round of {topic_name}")

        correct_count = 0
        wrong_answers = []
        round_counter = 0

        while infinite_rounds or round_counter < num_rounds:
            questions = generate_questions(topic_choice, 1)
            for i, (question, answer) in enumerate(questions):
                print(f"Question {round_counter + 1}:\n{question}")
                try:
                    user_input = input("Your answer: ")
                    if user_input == "end":
                        break
                    elif not user_input.isdigit():
                        raise ValueError("Invalid input! Please enter a number.")
                    user_answer = int(user_input)

                    if user_answer == answer:
                        print("Correct!\n")
                        correct_count += 1
                    else:
                        print(f"Wrong! The correct answer is {answer}.\n")
                        wrong_answers.append((question, user_answer, answer))

                except ValueError as ve:
                    print(ve)

            round_counter += 1
            if not infinite_rounds and round_counter >= num_rounds:
                break

        print(f"You answered {correct_count} out of {round_counter} questions correctly.")
        percentage_correct = (correct_count / round_counter) * 100
        print(f"You got {percentage_correct:.2f}% correct!\n")

        review_wrong_answers(wrong_answers)
        
        play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
        if len(play_again_input) > 0:
            play_again = play_again_input[0] == "y"
        else:
            play_again = False

    print("Thanks for playing!")
