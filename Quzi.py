import random
import time

class Quiz:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0
        self.start_time = None

    def start_quiz(self):
        print("Welcome to the Quiz!")
        input("Press Enter to start.")
        self.start_time = time.time()
        self.ask_question()

    def ask_question(self):
        if self.current_question < len(self.questions):
            question = random.choice(self.questions)
            print(f"\nQuestion: {question['text']}")
            for i, option in enumerate(question['options'], start=1):
                print(f"{i}. {option}")

            user_answer = input("Your answer (enter the option number): ")
            self.validate_answer(question, int(user_answer))
        else:
            self.end_quiz()

    def validate_answer(self, question, user_answer):
        correct_answer = question['correct_option']
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['options'][correct_answer - 1]}\n")
        self.current_question += 1
        self.ask_question()

    def end_quiz(self):
        end_time = time.time()
        duration = round(end_time - self.start_time, 2)
        print(f"\nQuiz completed! Your score is {self.score}/{len(self.questions)}.")
        print(f"Total time taken: {duration} seconds.")

# Sample question bank
question_bank = [
    {
        'text': 'What is the capital of France?',
        'options': ['Berlin', 'Paris', 'Madrid', 'Rome'],
        'correct_option': 2
    },
    {
        'text': 'who is present president of america?',
        'options': ['Joe Biden', 'maheshwari', 'laasya', 'nidhesh'],
        'correct_option': 1
    },
    # Add more questions as needed
]

# Create and start the quiz
quiz = Quiz(question_bank)
quiz.start_quiz()