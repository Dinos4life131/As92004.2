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
    #code that generates random questions, thus not allowing users to memorize questions.

if __name__ == "__main__":
    infinite_rounds, num_rounds = print_rounds_function()
    topic_choice, topic_name = select_topic()
    print(f"Selected topic: {topic_name}")
    #print(f"Infinite rounds: {infinite_rounds}, Number of rounds: {num_rounds}")
    print(f"You have selected {num_rounds} round of {topic_name}")
    print('If you choose to quit before the quiz is over type "End quiz". ')

    round_counter = 0
        #This counts how many rounds has been done, each time a quesiton is answered it goes up by 1
    while infinite_rounds or round_counter < num_rounds:
        questions = generate_questions(topic_choice, 1)
        for i, (question, answer) in enumerate(questions):
            print(f"Question {round_counter + 1}:\n{question}")
            #Prints the question and question number. 
        
        try:    
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct!\n")
            else:
                print("Wrong!\n")    
        except ValueError:
            print(f"Invalid input! The correct answer is {answer}.\n")
        
        round_counter += 1
        if not infinite_rounds and round_counter >= num_rounds:
            #due to infinite being a loop, the code goes forever, the bug? unable to stop the program even if you have had enough
            
            break

        #after multiple attempts, could not find a way to do what i wish to do, thus giving a night to think about it