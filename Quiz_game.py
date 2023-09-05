import random
# Define quiz questions and answers
quiz_questions = [
 {
 "question": "What is the capital of France?",
 "choices": ["A) Paris", "B) London", "C) Rome"],
 "correct_answer": "A"
 },
 {
 "question": "What is the largest planet in our solar system?",
 "choices": ["A) Mars", "B) Jupiter", "C) Venus"],
 "correct_answer": "B"
 },
 {
 "question": "The process of plants making their own food is called?",
 "correct_answer": "photosynthesis"
 }
]
# Welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice and fill-in-the-blank questions.")
print("Let's get started!\n")
# Initialize variables
score = 0
total_questions = len(quiz_questions)
# Quiz loop
for idx, question_data in enumerate(quiz_questions, start=1):
 print(f"Question {idx}: {question_data['question']}")

 if 'choices' in question_data:
 for choice in question_data['choices']:
 print(choice)

 user_answer = input("Select the correct answer (A, B, C): ")
 else:
 user_answer = input("Fill in the blank: ").lower()

 if user_answer == question_data['correct_answer'].lower():
 print("Correct!")
 score += 1
 else:
 print("Incorrect!")
 print(f"The correct answer is: {question_data['correct_answer']}\n")
# Calculate and display final score
final_score = (score / total_questions) * 100
print("\nQuiz completed!")
print(f"Your score: {final_score:.2f}%")
# Display performance message
if final_score == 100:
 print("Congratulations! You got a perfect score!")
elif final_score >= 70:
 print("Well done! You did a great job.")
else:
 print("Keep practicing! You can do better next time.")
# Play again?
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
 print("\nLet's play again!")
 print("-" * 30)
 exec(open(__file__).read()) # Restart the script
 else:
 print("Thank you for playing! Goodbye!")