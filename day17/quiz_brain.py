class QuizBrain:
    def __init__(self,questionBank):
        question_number = 0
        qestion_text = ""
        self.questionBank = questionBank

    def startQuiz(self):
        correctAnswers=0
        flag = True
        while(flag):
            for i in range(0 , len(self.questionBank)):
                user_answer = input(f"Q.{i+1} {self.questionBank[i].question} (True , False) : ")
                if(user_answer.lower()!=self.questionBank[i].answer.lower()):
                    flag = False
                    print("you have completed the Quiz !! ")
                    print(f"your score is : {correctAnswers} / 12 ")
                    break
                else:
                    correctAnswers+=1

