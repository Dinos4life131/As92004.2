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
        if topic == 1:  # Multiplication
            question = f"What is {num1} * {num2}?"
            answer = num1 * num2
        elif topic == 2:  # Addition
            question = f"What is {num1} + {num2}?"
            answer = num1 + num2
        elif topic == 3:  # Subtraction
            question = f"What is {num1} - {num2}?"
            answer = num1 - num2
        questions.append((question, answer))
    return questions

if __name__ == "__main__":
    infinite_rounds, num_rounds = print_rounds_function()
    topic_choice, topic_name = select_topic()
    print(f"Selected topic: {topic_name}")
    #print(f"Infinite rounds: {infinite_rounds}, Number of rounds: {num_rounds}")
    print(f"You have selected {num_rounds} round of {topic_name}")

    round_counter = 0

    while infinite_rounds or round_counter < num_rounds:
        questions = generate_questions(topic_choice, 1)
        for i, (question, answer) in enumerate(questions):
            print(f"Question {round_counter + 1}: {question}")
            
            user_answer = int(input("Your answer: "))
        
            if user_answer == answer:
                print("Correct!\n")
            else:
                print("Wrong!\n")
        #Issue here is that if they enter a letter or non number it breaks the code.
        '''
        Correct code would be 
        try:
        print(f"Question {round_counter + 1}: {question}")
        try:    
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct!\n")
            else:
                print("Wrong!\n")    
        except ValueError:
            print(f"Invalid input! The correct answer is {answer}.\n")
        This would make the user automatically fail the question and move on.
        '''
        round_counter += 1
        if not infinite_rounds and round_counter >= num_rounds:
            break