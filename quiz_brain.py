class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def check_question(self):
        return len(self.question_list) - 1 > self.question_number

    def next_question(self):
            
            lst = self.question_list[self.question_number]
            self.question_number +=  1
            user_answer = input(f"Q.{self.question_number}: {lst.text} (True/False): ")
            self.check_answer(user_answer, lst.answer, self.question_number)

    def check_answer(self, user_answer, correct_answer, count):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That answer was correct")
            print(f"score: {self.score} / {count} pogchamps\n")
        else:
            print("That answer was incorrect")
            print(f"score: {self.score} / {count} pogchamps\n")

    def final_question(self):
        if not self.check_question():
            print("You've completed the quiz")
            print(f"Your final score was: {self.score} / {self.question_number}") 
