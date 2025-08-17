from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# looping every single line in the dictionary bank
for every_single_question in question_data:

    # setting question_text as (looping key "text")
    question_text = every_single_question["question"]

    # setting question_answer as (looping key "answer")
    question_answer = every_single_question["correct_answer"]

    # create a new_q as an object to link question_text and question_answer as parameter
    # in order to see variable such as new_q.text and new_q.answer of the iterations
    new_q = Question(question_text, question_answer)

    # adding every single new_q as there will be twelve of them to be added as object
    question_bank.append(new_q)

# for example question_bank[0].text will show the first line of new_q.text

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")