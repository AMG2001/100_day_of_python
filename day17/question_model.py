from data import question_data
class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer


questionsBank=[]


# loading data from questions to question bank .
for i in range(0,len(question_data)):
    questionsBank.append(Question(question_data[i]['text'],question_data[i]['answer']))