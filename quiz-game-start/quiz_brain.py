class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.list = q_list
        self.score = 0

    def still_has_question(self):
        return self.number < len(self.list)



    def next_question(self):
        current_q = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_q.text} (True/False)?")
        self.check_answer(user_answer, current_q.answer)


    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            print("you got it right!")
            self.score +=1

        else:
            print("that's wrong!")

        print(f"the correct answer is : {correct_a}.")
        print(f"your current score is {self.score }/{self.number}")
        if(self.number == len(self.list)):
            print(f"you have completed the quiz\nyour final score was:{self.score}/{self.number}")



