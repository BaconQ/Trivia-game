from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
data = question_data

for i in data:
    question_data = i["question"]
    answer_data = i["correct_answer"]
    question_new = Question(question_data, answer_data)
    question_bank.append(question_new)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.check_question():
    quiz_brain.next_question()
    quiz_brain.final_question()




