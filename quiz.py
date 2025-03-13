import random

with open('questions.txt', 'r') as file:
    questions = file.readlines()

with open('answers.txt', 'r') as file:
    answers = file.readlines()

levels = {
    'easy': (0, 33),       
    'moderate': (34, 66),  
    'difficult': (67, 99) 
}

num_of_questions = 10
user_score = 0
total_questions = 0

for level, (start_index, end_index) in levels.items():
    print(f"\nStarting {level.capitalize()} level...\n")
    selected_indices = random.sample(range(start_index, end_index), num_of_questions)
    for i, q_index in enumerate(selected_indices):
        print(f"Question {i+1}: {questions[q_index]}")
        user_answer = input("Your answer: ").strip().lower()
    
        correct_answer = answers[q_index].strip().lower()
    
        if user_answer == correct_answer:
            print("Correct!")
            user_score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
    print()


print(f"Quiz Completed! You scored {user_score} out of {num_of_questions}.")
