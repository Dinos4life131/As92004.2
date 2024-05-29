def select_topic():
    topics = {
        #list of topics
        1: "Multiplication",
        2: "Addition",
        3: "Subtraction"
    }
    
    print("Select a topic:")
    for key, value in topics.items():
        print(f"{key}: {value}")
        
    while True:
        try:
            topic_choice = int(input("Enter the number of the topic you want to do: "))
            if topic_choice in topics:
                return topic_choice, topics[topic_choice]
            else:
                print("Invalid choice, please select a valid topic.")
        except ValueError:
            print("Invalid input, please enter a number.")


def print_rounds_function():
    while True:
        number_of_rounds = input("Enter the number of rounds you want to play (press Enter for infinite): ")
        
        if number_of_rounds == "":
            infinite_rounds = True
            print("Infinite rounds it is!")
            break
        elif number_of_rounds.isdigit():
            num_rounds = int(number_of_rounds)
            infinite_rounds = False
            print(f"{num_rounds} rounds it is!")
            break
        else:
            print("Invalid input! Please enter a valid number or press Enter for infinite rounds.")
    
if __name__ == "__main__":
    infinite_rounds, num_rounds = print_rounds_function()
    topic_choice, topic_name = select_topic()
    print(f"Selected topic: {topic_name}")
    print(f"Infinite rounds: {infinite_rounds}, Number of rounds: {num_rounds}")
